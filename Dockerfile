FROM quay.io/astronomer/astro-runtime:11.5.0

# connections
ENV AIRFLOW_CONN_AWS_DEFAULT='{"conn_type":"aws"}'

# variables
ENV AIRFLOW_VAR_SNS_ARN='arn:aws:sns:us-east-1:123456789012:my-sns-topic'