import os
import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from main import main



def run_etl(db_type):
    main(db_type)


# DAG arguments with default parameters
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 4, 22, 20, 0),  # Start at 8 PM
    "depends_on_past": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "params": {
        "db_type": "mysql",
    },
}

# Create the DAG
dag = DAG(
    "stock_etl_dag",
    default_args=default_args,
    description="My DAG for executing functions once a day at 8 PM",
    schedule="@daily",
    render_template_as_native_obj=True,
)

# Define a task to run the ETL function
task_run_etl = PythonOperator(
    task_id="run_load_stock_data_etl",
    python_callable=run_etl,
    op_args=[
        "{{ params.db_type}}",
    ],
    dag=dag,
)

# Set the task dependencies to define the execution order
task_run_etl
