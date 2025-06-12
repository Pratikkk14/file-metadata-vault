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

☁️ Enable Required GCP APIs
