Install Apache Kafka on Windows
# By Docker 

1/ Run Docker 

2/ Create Folder D:\Master_TP\BIGDATA\Kafka\

3/ then create file docker-compose.yml  from this folder

4/ Open Windows Powershell and goto this folder and run command : docker-compose up -d

<img width="549" height="169" alt="image" src="https://github.com/user-attachments/assets/1b3180f5-eb41-4cd5-866f-d9238fee574b" />


5/ On Internet Browser open  : http://localhost:8080/

<img width="1151" height="631" alt="image" src="https://github.com/user-attachments/assets/093d85b3-91e4-4d6f-a314-4915c2d2d1d4" />



لخطوة الأولى: إنشاء الـ Topic بنظام النسخ الاحتياطي

docker exec -it kafka-1 kafka-topics --create --topic site_sensors --bootstrap-server localhost:9092 --partitions 3 --replication-factor 3

<img width="713" height="337" alt="image" src="https://github.com/user-attachments/assets/71da4be2-9596-4d3d-906d-5b1dd492e28b" />


<img width="780" height="439" alt="image" src="https://github.com/user-attachments/assets/2f120224-b249-4ebc-915d-27776f791858" />


6/ I create python code TP_Kafka_Producer.py

<img width="1152" height="864" alt="image" src="https://github.com/user-attachments/assets/62454082-a3a8-4d3e-bc30-9919f399672b" />
        
7/ I create python code TP_Kafka_Consumer.py

<img width="1152" height="864" alt="image" src="https://github.com/user-attachments/assets/f0399dbd-dd49-45d9-8f98-d6c4f316de61" />
