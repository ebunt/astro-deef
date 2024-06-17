from airflow.models import Variable
from airflow.providers.amazon.aws.notifications.sns import send_sns_notification


SNS_ARN = Variable.get("sns_arn")
DEFAULT_REGION = "us-east-1"

dag_failure_sns_notification = send_sns_notification(
    aws_conn_id="aws_default",
    region_name=DEFAULT_REGION,
    message="The DAG {{ dag.dag_id }} failed",
    target_arn=SNS_ARN
)

task_failure_sns_notification = send_sns_notification(
    aws_conn_id="aws_default",
    region_name=DEFAULT_REGION,
    message="The task {{ ti.task_id }} failed",
    target_arn=SNS_ARN
)
