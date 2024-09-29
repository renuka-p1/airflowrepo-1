from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='test-dg-ls',
    default_args=default_args,
    description='This is our first dag',
    start_date= days_ago(2),
    schedule_interval=None,
    #start_date=datetime(2023, 9, 12, 2),
    #schedule_interval='@daily'
    access_control={
        'role_ashis': {
            'can_read'
        },
        'role_shashank': {
            'can_read',
            'can_edit',
            'can_delete'
        },
        'role_hpedemo-user01': {
            'can_read'
        },
        'role_demo-admin': {
            'can_read',
            'can_delete'
        },
        'role_rohit': {
            'can_read'
        }
}
) as dag: 
    task1=BashOperator(
        task_id='first_task',
        bash_command="ls /mnt/datasources/datafabric/testedfbeforeupgrade1"
    )

    task1
