#!/usr/bin/env python

import json
import pika
from utils import finbot

connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='finbot_queue')


def on_request(ch, method, props, body):

    body = body.decode('utf-8')

    print(" [.] finbot(%s)" % body)
    response = finbot(body)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=json.dumps(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='finbot_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
