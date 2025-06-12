# file-metadata-vault
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

