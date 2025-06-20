# file-metadata-vault
---
File Structure
project-root/                                                                                                                         
├── backend/ ← Flask/FastAPI app                         
│ │      ├──templates                                                                                                                         
│ │            ├──index.html ← to send file from frontend  ← to send file from frontend                                                 
│ ├── main.py ← routes + upload logic                                                                                                             
│ └── requirements.txt                                                                                                
├── functions/ ← Cloud Function code                                                                                                      
│ ├── main.py                                                                  
│ └── requirements.txt                                                                                                           
├── scripts/                                                                                                                     
│ └── setup.sh ← gcloud CLI to create bucket, topic                                                                        
├── .env                                                                                                                
├── README.md                                                  

# 📦 GCS File Metadata Reader (Cloud Run + Eventarc + Pub/Sub)

This repository contains a Python-based Cloud Run service that listens to **Google Cloud Storage object creation events** (via Eventarc), extracts file metadata, and **publishes it to a Pub/Sub topic**.



## 🐍 Python Compatibility

This project supports **Python versions 3.8 through 3.12**.



## 🔧 Setup Instructions

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/Pratikkk14/file-metadata-vault.git
cd file-metadata-vault
```

# Enable Required GCP APIs

```bash
gcloud services enable run.googleapis.com \
    pubsub.googleapis.com \
    storage.googleapis.com \
    eventarc.googleapis.com \
    logging.googleapis.com
```
This can be done by both ways either through **CLI** or through **GCP CONSOLE** 


# 🛠️ Set Required Environment Variables
You can export them in your terminal session or configure them in Cloud Run.
```bash
export PROJECT_ID="your-project-id"
export REGION="asia-south1"
export BUCKET_NAME="file-metadata-vault"
export TOPIC_NAME="file-metadata"
export SERVICE_NAME="file-metadata-vault"
```
# ☁️ Deploy to Cloud Run
```bash
gcloud run deploy $SERVICE_NAME \
  --source . \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars PROJECT_ID=$PROJECT_ID,TOPIC_NAME=$TOPIC_NAME \
  --runtime python312 \
  --entry-point handle_gcs_event
  ```

💡 You may replace python312 with another version like python311, python310, etc., based on your preference.

# 🔁 Create Pub/Sub Topic
```bash
gcloud pubsub topics create $TOPIC_NAME
```

# ⚡ Create Eventarc Trigger

This trigger listens to object finalization events in your GCS bucket:
```bash
gcloud eventarc triggers create obj-creation-trigger \
  --location=$REGION \
  --destination-run-service=$SERVICE_NAME \
  --destination-run-region=$REGION \
  --event-filters="type=google.cloud.storage.object.v1.finalized" \
  --event-filters="bucket=$BUCKET_NAME" \
  --service-account="your-service-account@${PROJECT_ID}.iam.gserviceaccount.com"
  ```

# 🪵 Logging and Debugging

All logs (file name, size, format, Pub/Sub status) will appear in:

---


### 📍 Cloud Run Logs:
Navigate to: ```Cloud Run > [Your Service] > Logs```

Example log output:

```json
{
  "severity": "INFO",
  "message": "File uploaded to GCS",
  "file_name": "example.txt",
  "file_size": "unknown",
  "file_type": "unknown",
  "bucket": "file-metadata-vault"
}
```
##### 💡 Tip: You can use timestamps like ```print(f"[{datetime.now()}] message")``` for better traceability.

# ✅ Success Criteria
✅ Eventarc triggers on object creation in GCS.

✅ Cloud Run receives and logs file metadata.

✅ Metadata is successfully published to the Pub/Sub topic.

✅ Logs contain structured and useful debugging info.

# 📎 Notes
Ensure your Cloud Run service account has the Pub/Sub Publisher role.

This project assumes you're using Audit Log-based Eventarc triggers.



# 💬 Want More?
Let me know if you'd like:

🛠️ A GitHub Actions CI workflow

🖥️ A simple Pub/Sub subscriber script

📸 Screenshots of the GCP console setup steps