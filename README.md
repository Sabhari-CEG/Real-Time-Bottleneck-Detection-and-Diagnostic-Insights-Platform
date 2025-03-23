# Real-Time Log Analysis Platform

This project demonstrates the implementation of a real-time log analysis platform using **Google Cloud Pub/Sub**, **Python**, and **Socket APIs**. It offers real-time log ingestion, processing, and metric extraction, aligning with common data pipeline debugging and log analysis responsibilities.

---

## 🚀 **Project Overview**

### **Goal**
- Identify bottlenecks in real time.  
- Analyze logs and diagnostic data for actionable insights.  
- Provide real-time metrics via a socket API.

### **Tech Stack**
- **Google Cloud Pub/Sub**: Real-time message ingestion and streaming.  
- **Python**: Log processing, analysis, and socket API server.  
- **Socket API**: Exposes real-time metrics for external consumption.

---

## 🛠️ **Technology Selection**

### **Why Google Cloud Pub/Sub?**
- ⚡ **Real-Time Streaming:** Low-latency message delivery, ideal for log ingestion.  
- 🔥 **Scalability:** Automatically handles high-throughput workloads.  
- 🔌 **Integration:** Easily integrates with other GCP services.  

### **Why Python?**
- 🐍 **Ease of Use:** Simple and fast development of log processing scripts.  
- 📚 **Libraries:** Uses `google-cloud-pubsub` for seamless interaction.  
- 🔥 **Object-Oriented Design:** Ensures modular, maintainable code.

### **Why Socket API?**
- 🚀 **Real-Time Access:** Exposes live metrics to external applications.  
- ⚙️ **Simplicity:** Lightweight and easy to implement.  

---

## 🔧 **Project Setup**

### **Step 1: Enable Google Cloud Pub/Sub API**
1. Go to [Google Cloud Console](https://console.cloud.google.com).  
2. Navigate to **APIs & Services > Library**.  
3. Enable the **Pub/Sub API**.  

### **Step 2: Create Pub/Sub Components**
1. Go to **Pub/Sub > Topics**.  
2. Create a topic named:  data-provider
3. Create a subscription attached to the topic: logs-subscription

### **Step 3: Service Account Key**
1. Go to IAM & Admin > Service Accounts.
2. Create a service account with the following roles:
    #### Pub/Sub Publisher
    #### Pub/Sub Subscriber
3. Download the JSON key file.

## 🛠️ **Implementation Steps**
### Step 4: Publisher
1. Reads logs from a file.
2. Publishes them to the data-provider topic at regular intervals.

### Step 5: Subscriber
1. Listens to the data-provider topic.
2. Processes logs in real time.
3. Updates metrics like bottlenecks, errors, and insights.

### Step 6: Insights Extracted
1. ✅ Total logs processed
2. 🚫 Error count (based on HTTP status codes)
3. ⏱️ Average processing time per log
4. 🌐 Frequent IP addresses accessing resources
5. 🔥 Status code distribution (e.g., 200, 404, 500)


## ⚙️ **Testing the Platform**
1. Run the Publisher:
 ```bash
   python publisher.py
```
2. Run the Subscriber:
```bash
python subscriber.py
   ```
3. Test the Socket API:
```bash
python client.py
   ```

## 📊 **Why This Approach?**
1. ✅ Real-time analysis using Pub/Sub's low-latency messaging system.
2. 🔧 Scalable solution for handling large volumes of logs.
3. 🌐 Actionable insights via an API for external tools or dashboards.

