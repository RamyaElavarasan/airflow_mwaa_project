from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_mwaa():
    print("Hello MWAA!")

with DAG(
    'example_dag_mwaa',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='hello_task',
        python_callable=hello_mwaa
    )
