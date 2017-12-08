__author__ = "xiaoyu hao"
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

def callback(ch,method,propertise,body):
    print("---->",ch,method,propertise)
    time.sleep(30)
    print(" [x] Received %r" % body)

    ch.basic_ack(delivery_tag=method.delivery_tag)   #确认消息已经执行完成

channel.basic_qos(prefetch_count=1)   #消息分发

channel.basic_consume(#消费消息
                    callback, #如果收到消息，就调用CALLBACK 函数来处理消息
                    queue='hello',
                    #no_ack=True    #不加，如果消费者断掉，会转移到其他的消费者队列，消息不会释放
                    )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()