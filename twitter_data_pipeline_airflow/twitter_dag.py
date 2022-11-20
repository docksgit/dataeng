from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl

twitter_uname = 'ecommurz'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 6, 1),
    'email': ['southgatecox@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Twitter data pipeline using Airflow of {} account'.format(twitter_uname),
    schedule_interval=timedelta(days=1), 
)

run_etl = PythonOperator(
    task_id='{}_twitter_etl'.format(twitter_uname),
    python_callable=run_twitter_etl(twitter_uname),
    dag=dag, 
)

run_etl