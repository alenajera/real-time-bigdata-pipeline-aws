# Real-Time Big Data Pipeline on AWS 

This project implements a **real-time Big Data pipeline** using AWS services.  
It simulates user events, processes them **serverlessly**, stores them in **Amazon S3**, and allows interactive analytics with **Athena and QuickSight**.

---

## **Project Architecture**

```text
[Docker + Python]  --->  [AWS Kinesis Data Stream]  --->  [AWS Lambda]  --->  [S3 - Raw Data]
                                                               |
                                                        [AWS Glue Crawler]
                                                               |
                                                        [Athena + QuickSight]

Tech Stack:
AWS S3: Raw data storage (Data Lake)
AWS Kinesis Data Stream: Real-time data ingestion
AWS Lambda: Serverless data processing
AWS Glue Crawler: Automatic schema discovery
AWS Athena: SQL-based analytics on S3
Amazon QuickSight: Interactive dashboards
Docker + Python: Local event simulator
IAM Roles: Secure resource access control

Key Results:
A fully functional real-time Big Data pipeline that:
-Ingests and processes user events in real time
-Stores events in S3 for cost-effective storage
-Provides SQL-based analytics with Athena
-Enables interactive dashboards in QuickSight

This project demonstrates Big Data, Cloud Architecture, and Serverless Computing skills.

Author
Douglas Alejandro Nájera
🔗 LinkedIn Profile: https://www.linkedin.com/in/dnajera26/
