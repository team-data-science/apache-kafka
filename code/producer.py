
from kafka import KafkaProducer

# Create Message
msg = 'Hello this is a test message'

# Create a producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Function to send messages into Kafka
def kafka_python_producer_async(producer, msg):
    
    producer.send('mytesttopic', msg).add_callback(success).add_errback(error)
    producer.flush()

def success(metadata):
    print(metadata.topic)

def error(exception):
    print(exception)  

print("start producing")

# Produce the message, but serialize into bytes
kafka_python_producer_async(producer,bytes(msg, 'utf-8'))

print("done")
 

'''
def kafka_python_producer_sync(producer, size):
    for _ in range(size):
        future = producer.send('topic', msg)
        result = future.get(timeout=60)
    producer.flush()    
'''