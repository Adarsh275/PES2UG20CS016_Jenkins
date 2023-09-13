import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka:9092')

for i in range(1000):
    producer.send('my-topic', bytes(str(i), 'utf-8'))
    time.sleep(0.1)

producer.close()
