from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import ssl
import json
import myes
 
#project_id = "speedy-victory-336109"
#subscription_id = "glb-log-sub"
project_id="gcp-wow"
subscription_id="mysql-log-sub"
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    data = json.loads(message.data)
    print(data)
    #myes.insert(data)
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()
