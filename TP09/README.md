
## Table of Contents

- [1. Install Docker](#1-Install_Docker)
- [2. docker-compose yml ](#https://github.com/BENALI-DZ/Big_Data_Analytics_TP/blob/main/TP09/docker-compose.yml)
- [3. Install Hadoop , Spark by docker compose](#3-Install_Hadoop_Spark)
- [4. Call Hadoop_Spark  ](#4-Call_Hadoop)
  - [4.1 Call Hadoop http://localhost:9870/dfshealth.html#tab-datanode )](#41-name-process-or-service)
  - [4.2  Call Spark   http://localhost:8080/](#42-pid)
 
  #1-Install Docker
  
 1-  Install Docker  
 
 #2-docker-compose
 
 2- I create folder from my computer exemple
 - E:\Master_TP\BIGDATA\Docker_HadoopSpark
 -  create file docker-compose.yml

 #3-Install_Hadoop_Spark
 
 3- Open PowerShell and  run command
    
     - Goto folder --> cd E:\Master_TP\BIGDATA\Docker_HadoopSpark
     - 
     -  docker compose down
     -  docker compose up -d




 
 
 <img width="775" height="470" alt="powerShell_start" src="https://github.com/user-attachments/assets/bb73f85f-8181-44fb-a2a8-e0fc39dc6fba" />

   #4-Call_Hadoop
   
Call Hadoop From Browse
- http://localhost:9870/dfshealth.html#tab-datanode

 <img width="1582" height="1236" alt="Screenshot 2025-12-28 at 15-39-13 Namenode information" src="https://github.com/user-attachments/assets/1ecf7abf-6f99-41ed-b676-310b8d801c4e" />
 
   #5-Call_Spark
Call Spark From Browse
- http://localhost:8080/

<img width="1600" height="738" alt="Screenshot 2025-12-28 at 15-38-05 Spark Master at spark __spark-master 7077" src="https://github.com/user-attachments/assets/64b92c35-0e7e-4d5c-92e3-5e6be59a5d89" />
