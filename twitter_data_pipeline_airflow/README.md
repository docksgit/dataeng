# Basic Twitter Data Pipeline Project

## Overview
This project is initiated to make a data pipeline to perform ETL process from a public/unprotected Twitter account timeline as being scrapped and then being placed in a cloud storage (AWS S3 Bucket) as parquet file through Airflow running on cloud server (AWS EC2 Instance).

## Main Requirements
1. AWS EC2 Instance -> Airflow server
2. AWS S3 Bucket -> data storage
3. Python file for ETL dan DAG definition

## Steps

1. Create new virtual environment for this project -> `twt-env` (included in `.gitignore`)
2. Install `requirements.txt`
3. Draft the `twitter_etl.py` file
4. Setup AWS EC2 Instance as Airflow server -> Create key pair and set rule for incoming traffic control 
5. Install package in the server -> `package_install.sh`
6. Draft the `twitter_dag.py`
7. Setup AWS S3 Bucket as data storage 
8. Setup IAM role for EC2 and S3 access
9. Create `twitter_dag` folder in Airflow server
10. Copy and paste `twitter_etl.py` and `twitter_dag.py` to the aforementioned folder
11. In a new terminal, run `airflow standalone` to get Airflow username and password
12. Open `Public IPv4 DNS`+`:8080` in a browser
13. Login using Airflow credential 
14. The DAG should be included over there and ready to manage
