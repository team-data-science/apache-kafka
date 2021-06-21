from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')

# define a consumer that waits for new messages
def kafka_python_consumer():
    
    # Consumer using the topic name and setting a group id
    consumer = KafkaConsumer('mytesttopic', group_id='mypythonconsumer')
    for msg in consumer:
      print(msg)

print("start consuming")

# start the consumer
kafka_python_consumer()

print("done")
