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

---

## 🐍 Python Compatibility

This project supports **Python versions 3.8 through 3.12**.

---

## 🔧 Setup Instructions

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/Pratikkk14/file-metadata-vault.git
cd file-metadata-vault
```

# Enable Required GCP APIs
---
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
