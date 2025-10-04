# file-metadata-vault
---

## 📝 Setting Up Environment Variables

Create a `.env` file in your project root with the following variables (replace the placeholder values with your actual configuration):

```env
PROJECT_ID="your-gcp-project-id"
REGION="your-gcp-region"
BUCKET_NAME="your-gcs-bucket-name"
TOPIC_NAME="your-pubsub-topic-name"
SUBSCRIPTION_NAME="your-pubsub-subscription-name"
STORAGE_CLASS="your-gcs-storage-class"
```

**Tip:**  
- The `.env` file is for local development and should not be committed to version control.
- For Cloud Run, set environment variables using the `--set-env-vars` flag during deployment.
