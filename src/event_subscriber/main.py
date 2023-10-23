import os
from pika import BlockingConnection, ConnectionParameters
from resources.alerts.alert_service import create_threshold_alert_event_record
from dotenv import load_dotenv
load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE')


def init_subscriber():
    connection = BlockingConnection(ConnectionParameters(host=RABBITMQ_HOST))
    return connection.channel()


def on_event(ch, method, properties, body):
    print(f"Received: {body}")
    create_threshold_alert_event_record("Threshold Alert Event")


if __name__ == "__main__":
    channel = init_subscriber()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.exchange_declare(exchange='logs', exchange_type='topic')
    channel.basic_consume(queue=RABBITMQ_QUEUE,
                          on_message_callback=on_event, auto_ack=True)
    channel.start_consuming()
