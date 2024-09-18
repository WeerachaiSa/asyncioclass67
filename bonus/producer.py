# https://aiokafka.readthedocs.io/en/stable/
from aiokafka import AIOKafkaProducer
import asyncio
import json
import random

def serializer(value):
    return json.dumps(value).encode()

async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=serializer)
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    while True:
        try:
            # Produce message
            data = {'a': 123.4, 'b':'Some string'}
            res = await producer.send_and_wait(topic="my_topic", value=data)
            print(res)
            await asyncio.sleep(1)
        except:
            # Wait for all pending messages to be delivered or expire.
            await producer.stop()
            raise

asyncio.run(send_one())
