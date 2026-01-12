from kafka import KafkaProducer
import json
import time
import random

# الاتصال بجميع الـ Brokers المتاحين
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092', 'localhost:9094', 'localhost:9096'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks='all'  # التأكد من وصول الرسالة لجميع النسخ لضمان الأمان
)

print("Sensors are streaming data to Kafka Cluster...")

try:
    while True:
        data = {
            "machine": random.choice(["Crane_01", "Excavator_05", "Truck_12"]),
            "fuel_level": random.randint(5, 100),
            "engine_temp": random.uniform(70, 120),
            "timestamp": time.ctime()
        }
        producer.send('site_sensors', value=data)
        print(f"Sent to Kafka: {data}")
        time.sleep(1)
except KeyboardInterrupt:
    producer.close()