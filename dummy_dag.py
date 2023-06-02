
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments

default_args = {
    'owner': 'Joe',
    'start_date': days_ago(0),
    'email': ['Joe@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'dummy_dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(minutes=1),
)

# define the tasks
task1 = BashOperator(
    task_id='task1',
    bash_command='sleep 1',
    dag=dag,
)
task2 = BashOperator(
    task_id='task2',
    bash_command='sleep 2',
    dag=dag,
)
task3 = BashOperator(
    task_id='task3',
    bash_command='sleep 3',
    dag=dag,
)

# task pipeline
task1 >> task2 >> task3
