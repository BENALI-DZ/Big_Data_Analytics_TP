from kafka import KafkaConsumer
import json

# الاتصال بـ Cluster كافكا
consumer = KafkaConsumer(
    'site_sensors',
    bootstrap_servers=['localhost:9092', 'localhost:9094', 'localhost:9096'],
    auto_offset_reset='latest',  # البدء بقراءة أحدث الرسائل فقط
    group_id='site-monitoring-group', # معرف المجموعة لضمان توزيع المهام
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("🚀 Dashboard: Monitoring machine health in real-time...")

try:
    for message in consumer:
        data = message.value
        machine = data['machine']
        temp = data['engine_temp']
        fuel = data['fuel_level']
        
        # منطق التنبيه (Alert Logic)
        status = "✅ OK"
        if temp > 100:
            status = "⚠️ OVERHEATING"
        elif fuel < 20:
            status = "⛽ LOW FUEL"
            
        print(f"[{data['timestamp']}] {machine:12} | Temp: {temp:6.2f}°C | Fuel: {fuel:3}% | Status: {status}")

except KeyboardInterrupt:
    print("Stopping monitor...")
    consumer.close()