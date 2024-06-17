from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

from include.callbacks.aws import dag_failure_sns_notification, task_failure_sns_notification


with DAG(
    dag_id="sns_notifications",
    schedule="@once",
    start_date=datetime(2023, 1, 1),
    on_failure_callback=[dag_failure_sns_notification],
    catchup=False,
):
    BashOperator(
        task_id="failing_task",
        on_failure_callback=[task_failure_sns_notification],
        bash_command="fail",
    )
