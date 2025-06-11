# file-metadata-vault
File Structure
project-root/
├── backend/ ← Flask/FastAPI app
│ ├── main.py ← routes + upload logic
│ └── requirements.txt
├── functions/ ← Cloud Function code
│ ├── main.py
│ └── requirements.txt
├── scripts/
│ └── setup.sh ← gcloud CLI to create bucket, topic
├── .env.example
├── README.md

