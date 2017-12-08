__author__ = "xiaoyu hao"

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

# 声明一个管道
channel = connection.channel()

#声明queue
channel.queue_declare(queue='hello',durable=True)   #durable=True 让队列持久化

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  #消息持久化，进程挂掉消息不会丢失
                      ))

print("[x] Sent 'Hello World!'")

connection.close()