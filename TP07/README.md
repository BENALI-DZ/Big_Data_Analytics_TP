Install Apache Kafka on Windows
# By Docker 

1/ Run Docker 

2/ Create Folder D:\Master_TP\BIGDATA\Kafka\

3/ then create file docker-compose.yml  from this folder

4/ Open Windows Powershell and goto this folder and run command : docker-compose up -d

<img width="549" height="169" alt="image" src="https://github.com/user-attachments/assets/1b3180f5-eb41-4cd5-866f-d9238fee574b" />


5/ On Internet Browser open  : http://localhost:8080/

<img width="1151" height="631" alt="image" src="https://github.com/user-attachments/assets/093d85b3-91e4-4d6f-a314-4915c2d2d1d4" />

6/ I create python code TP_Kafka_Producer.py

<img width="1152" height="864" alt="image" src="https://github.com/user-attachments/assets/62454082-a3a8-4d3e-bc30-9919f399672b" />

    from kafka import KafkaConsumer
    import json
    import time
    import random
     
    
    consumer = KafkaConsumer(
        'site_sensors',
        bootstrap_servers=['localhost:9092', 'localhost:9094', 'localhost:9096'],
        auto_offset_reset='earliest',       # هذا سيجعله يقرأ البيانات القديمة أيضاً
        group_id=None,                      # اجعله None مؤقتاً للتأكد من وصول البيانات
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
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
            consumer.send('site_sensors', value=data)
            print(f"Sent to Kafka: {data}")
            time.sleep(1)
    except KeyboardInterrupt:
        consumer.close()
        
  /***** 
  Result after axecution 
  
        
7/ I create python code TP_Kafka_Consumer.py

<img width="1152" height="864" alt="image" src="https://github.com/user-attachments/assets/f0399dbd-dd49-45d9-8f98-d6c4f316de61" />
