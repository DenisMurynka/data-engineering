from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from reddit_etl import run_reddit_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 4, 18),
    'email': ['kyiv@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='DAG to scrap 50 Reddit posts and save to csv!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_reddit_etl',
    python_callable=run_reddit_etl,
    dag=dag, 
)

run_etl