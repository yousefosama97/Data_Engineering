# import the libraries

from datetime import timedelta
# The DAG object; to instantiate a DAG
from airflow import DAG
# Operators to write tasks!
from airflow.operators.bash_operator import BashOperator
# forscheduling
from airflow.utils.dates import days_ago

#defining DAG arguments

default_args = {
    'owner': 'Joe,
    'start_date': days_ago(0),
    'email': ['Joe@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'yet-another-dag',
    default_args=default_args,
    description='DAG to extract fields from /etc/passwd and transforms and loads data into a file',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define the first task

extract = BashOperator(
    task_id='extract',
    bash_command='cut -d":" -f1,3,6 /etc/passwd > /home/project/airflow/dags/extracted-data.txt',
    dag=dag,
)

# define the second task
transform_and_load = BashOperator(
    task_id='transform',
    bash_command='tr ":" "," < /home/project/airflow/dags/extracted-data.txt > /home/project/airflow/dags/transformed-data.csv',
    dag=dag,
)

# task pipeline
extract >> transform_and_load
