import time
from google.cloud import pubsub_v1

service_account_key_path = "service-acc.json"
project_id = "testing"
topic_id = "data-provider"

publisher = pubsub_v1.PublisherClient.from_service_account_file(service_account_key_path)
topic_path = publisher.topic_path(project_id, topic_id)

file_path = "access_log_Jul95.txt" 

try:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as log_file:
        logs = log_file.readlines()  


    for log in logs:
        log = log.strip()  
        if log:  
            # print(log)
            publisher.publish(topic_path, data=log.encode("utf-8"))
            print(f"Published log: {log}")
            time.sleep(0.3)

except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")