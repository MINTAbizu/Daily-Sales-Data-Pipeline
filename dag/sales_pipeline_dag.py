from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from extract.extract import extract_data
from transform.transform import transform_data
from load.load import load_data

def etl_pipeline():
    df = extract_data()
    df = transform_data(df)
    load_data(df)

with DAG(
    dag_id="daily_sales_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=etl_pipeline
    )
