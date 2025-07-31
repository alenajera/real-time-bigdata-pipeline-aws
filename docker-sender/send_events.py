import boto3
import json
import time
import random
import uuid
from datetime import datetime

# Nombre de tu stream en Kinesis
stream_name = 'UserEventStream'
region_name = 'us-east-1'

# Cliente de Kinesis
kinesis = boto3.client('kinesis', region_name=region_name)

def generate_event():
    return {
        'event_id': str(uuid.uuid4()),
        'user_id': random.randint(1000, 9999),
        'event_type': random.choice(['click', 'view', 'purchase']),
        'timestamp': datetime.utcnow().isoformat()
    }

# Bucle infinito: 1 evento/segundo
while True:
    event = generate_event()
    print("Enviando:", event)
    kinesis.put_record(
        StreamName=stream_name,
        Data=json.dumps(event),
        PartitionKey=str(event['user_id'])
    )
    time.sleep(1)