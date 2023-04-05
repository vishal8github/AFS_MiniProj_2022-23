import pika, json

params = pika.URLParameters('amqps://ckqhiwfs:oFpxX5NZlfBF2wVDdoCOnYxy9mZzod2a@puffin.rmq2.cloudamqp.com/ckqhiwfs')

conn = pika.BlockingConnection(params)

channel = conn.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
