""" RabbitMQ Publisher """
"""_summary_
This script to connect to RabbitMQ and publish a 'THRESHOLD_ALERT' event.
"""


import os
import json
from amqpstorm import Connection, Message
from dotenv import load_dotenv
load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')
RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE')

connection = Connection(RABBITMQ_HOST, RABBITMQ_USER, RABBITMQ_PASSWORD)
channel = connection.channel()
channel.queue.declare(RABBITMQ_QUEUE)


def publish_threshold_alert(message_body='THRESHOLD_ALERT', data=None):
    message_content = {'type': message_body}
    if data:
        message_content.update(data)
    message_string = json.dumps(message_content)
    message = Message.create(channel, message_string)
    message.publish(RABBITMQ_QUEUE)


if __name__ == "__main__":
    publish_threshold_alert()
    print("THRESHOLD_ALERT event has been published!")
