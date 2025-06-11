from flask import Flask, request, render_template
from google.cloud import storage
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure your bucket name
BUCKET_NAME = os.environ.get("BUCKET_NAME")
if BUCKET_NAME is None:
    raise ValueError("BUCKET_NAME environment variable not set.  Please configure .env file")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Upload to GCP
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    return f'File {file.filename} uploaded to {BUCKET_NAME}.'

if __name__ == '__main__':
    app.run(debug=True)