#!/bin/bash

ENV_FILE="$(dirname "$0")/../.env"
if [ ! -f "$ENV_FILE" ]; then
echo ".env file not found. Please create one at $ENV_FILE"
exit 1
fi

set -o allexport
source "$ENV_FILE"
set +o allexport

#exit if any command fails
set -e

#configuration of the resources
echo "Project ID: $PROJECT_ID"
echo "Region: $REGION"
echo "Bucket: $BUCKET_NAME"
echo "Topic: $TOPIC_NAME"
echo "Subscription: $SUBSCRIPTION_NAME"

#checking if resources already exist
BUCKET_EXISTS=false
TOPIC_EXISTS=false
SUB_EXISTS=false

if gsutil ls -b "gs://$BUCKET_NAME" >/dev/null 2>&1; then
BUCKET_EXISTS=true
fi

if gcloud pubsub topics describe "$TOPIC_NAME" --project="$PROJECT_ID" >/dev/null 2>&1; then
TOPIC_EXISTS=true
fi

if gcloud pubsub subscriptions describe "$SUBSCRIPTION_NAME" --project="$PROJECT_ID" >/dev/null 2>&1; then
SUB_EXISTS=true
fi

if $BUCKET_EXISTS && $TOPIC_EXISTS && $SUB_EXISTS; then
echo "All resources already exist. Skipping creation."
exit 0
fi


echo "Enabling required services..."
gcloud services enable storage.googleapis.com pubsub.googleapis.com --project="$PROJECT_ID"

#setup initialization
gcloud services enable
storage.googleapis.com
pubsub.googleapis.com

echo "Services enabled."

#create GCS bucket
if ! $BUCKET_EXISTS; then
  echo "Creating GCS bucket..."
  gsutil mb -p $PROJECT_ID -c $STORAGE_CLASS -l $REGION gs://$BUCKET_NAME
  echo "GCS bucket created."
else
  echo "GCS bucket already exists. Skipping creation."
fi

#Adding bucket policy to restrict public access
echo "Enforcing public access prevention..."
gsutil uniformbucketlevelaccess set on gs://$BUCKET_NAME
gsutil iam set publicAccessPrevention enforced gs://$BUCKET_NAME

#Creating the Pub/Sub topic
if ! $TOPIC_EXISTS; then
  echo "Creating Pub/Sub topic..."
  gcloud pubsub topics create "$TOPIC_NAME" --project="$PROJECT_ID"
else
  echo "Pub/Sub topic already exists. Skipping creation."
fi

#Creating a subscription
if ! $SUB_EXISTS; then
  echo "Creating Pub/Sub subscription..."
  gcloud pubsub subscriptions create "$SUBSCRIPTION_NAME" --topic="$TOPIC_NAME" --project="$PROJECT_ID"
else
  echo "Pub/Sub subscription already exists. Skipping creation."
fi

echo "All resources created successfully!"
