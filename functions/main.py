import os
import json
from google.cloud import pubsub_v1
import functions_framework

# Get environment variables
PROJECT_ID = os.environ.get("PROJECT_ID")
TOPIC_NAME = os.environ.get("TOPIC_NAME")

# Initialize Pub/Sub publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_NAME)

@functions_framework.cloud_event
def handle_gcs_event(cloudevent):
    """
    Triggered by a Cloud Storage event via Eventarc.
    Publishes file metadata (name, size, format) to a Pub/Sub topic.
    """

    data = cloudevent.data

    # Extract metadata
    file_name = data.get("name")
    file_size = data.get("size")
    file_type = data.get("contentType")

    # Log for verification
    print(f"File uploaded: {file_name}")
    print(f"Size: {file_size} bytes")
    print(f"Type: {file_type}")

    # Compose metadata message
    metadata = {
        "file_name": file_name,
        "file_size": file_size,
        "file_format": file_type
    }

    # Publish to Pub/Sub
    data = publisher.publish(
        topic_path,
        json.dumps(metadata).encode("utf-8")
    )
    print(f"✅ Published message ID: {data.result()}")
