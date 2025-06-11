# file-metadata-vault
File Structure
project-root/
├──frontend ← to send file from frontend 
├── backend/ ← Flask/FastAPI app
│ ├── main.py ← routes + upload logic
│ └── requirements.txt
├── functions/ ← Cloud Function code
│ ├── main.py
│ └── requirements.txt
├── scripts/
│ └── setup.sh ← gcloud CLI to create bucket, topic
├── .env
├── README.md

