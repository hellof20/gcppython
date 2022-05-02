from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1

project_id = "speedy-victory-336109"
subscription_id = "mysql-slow-query"
#project_id = "ultra-compound-305409"
#subscription_id = "mysub"
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(message.data)
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.subscription_id = "mysql-slow-query"
