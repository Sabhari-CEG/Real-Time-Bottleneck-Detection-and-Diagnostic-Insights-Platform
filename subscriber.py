from google.cloud import pubsub_v1
import socket
import threading
from collections import Counter
import time

service_account_key_path = "serviceacc.json"

project_id = "testing"
subscription_id = "logs-subscription"

subscriber = pubsub_v1.SubscriberClient.from_service_account_file(service_account_key_path)
subscription_path = subscriber.subscription_path(project_id, subscription_id)

metrics = {
    "total_logs_processed": 0,
    "error_count": 0,
    "average_processing_time": 0.0,
    "last_log": None,
    "frequent_ips": Counter(),
    "status_code_distribution": Counter(),
}
lock = threading.Lock()  


def update_metrics(log):
    """Update metrics based on the incoming log."""
    with lock:
        metrics["total_logs_processed"] += 1
        metrics["last_log"] = log

        try:
            parts = log.split(" ")
            ip_address = parts[0]
            status_code = parts[-2]

            metrics["frequent_ips"][ip_address] += 1
            metrics["status_code_distribution"][status_code] += 1

            if status_code.startswith("4") or status_code.startswith("5"):
                metrics["error_count"] += 1

        except IndexError:
            print(f"Error parsing log: {log}")

        metrics["average_processing_time"] = (
            metrics["average_processing_time"] * (metrics["total_logs_processed"] - 1)
            + 0.3 
        ) / metrics["total_logs_processed"]


def callback(message):
    """Callback function for Pub/Sub subscriber."""
    log = message.data.decode("utf-8")
    print(f"Received log: {log}")
    update_metrics(log)
    message.ack()


def start_pubsub_subscriber():
    """Start the Pub/Sub subscriber."""
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...")

    try:
        streaming_pull_future.result()  
    except KeyboardInterrupt:
        streaming_pull_future.cancel()


def handle_client(client_socket):
    """Handle incoming socket client connections."""
    while True:
        try:
            request = client_socket.recv(1024).decode("utf-8")
            if request.lower() == "get_metrics":
                response = str(metrics).encode("utf-8")
                client_socket.send(response)
            elif request.lower() == "close":
                client_socket.send("Connection closed".encode("utf-8"))
                break
            else:
                client_socket.send("Invalid command".encode("utf-8"))
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    client_socket.close()


def start_socket_server():
    """Start the socket server to expose metrics."""
    server_ip = "127.0.0.1"
    port = 8000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    server.listen(5) 
    print(f"Socket server listening on {server_ip}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    pubsub_thread = threading.Thread(target=start_pubsub_subscriber)
    pubsub_thread.start()

    start_socket_server()
