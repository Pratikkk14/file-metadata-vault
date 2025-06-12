import os
import json
import google.auth
from datetime import datetime
from google.cloud import pubsub_v1
import functions_framework

# Get default project ID
_, default_project_id = google.auth.default()
PROJECT_ID = os.environ.get("PROJECT_ID", default_project_id)
TOPIC_NAME = os.environ.get("TOPIC_NAME", "file-metadata")

# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_NAME)

@functions_framework.cloud_event
def handle_gcs_event(cloudevent):
    """
    Triggered by a GCS object finalization event (via Eventarc).
    Extracts object metadata and publishes it to Pub/Sub.
    """
    trigger_time = datetime.utcnow().isoformat() + "Z"

    print(json.dumps({
        "severity": "INFO",
        "message": "Function triggered by GCS event",
        "trigger_time": trigger_time,
        "event_type": cloudevent["type"]
    }))

    data = cloudevent.data

    file_name = data.get("name")
    file_size = data.get("size")
    file_type = data.get("contentType")
    bucket = data.get("bucket")

    print(json.dumps({
        "severity": "INFO",
        "message": "File metadata extracted",
        "bucket": bucket,
        "file_name": file_name,
        "file_size": file_size,
        "file_type": file_type
    }))

    metadata = {
        "bucket": bucket,
        "file_name": file_name,
        "file_size": file_size,
        "file_format": file_type,
        "trigger_time": trigger_time
    }

    try:
        future = publisher.publish(
            topic_path,
            json.dumps(metadata).encode("utf-8")
        )
        message_id = future.result()

        print(json.dumps({
            "severity": "INFO",
            "message": "Published to Pub/Sub",
            "topic": topic_path,
            "message_id": message_id
        }))

    except Exception as e:
        print(json.dumps({
            "severity": "ERROR",
            "message": "Failed to publish to Pub/Sub",
            "error": str(e)
        }))
