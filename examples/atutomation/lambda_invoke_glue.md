# Lambda Invoke Glue Job

From a lambda function invoke a glue job

```python
import json
import boto3

def lambda_handler(event, context):
    # Define the Glue job name
    glue_job_name = 'your_glue_job_name'  # Replace with your Glue job name

    # Initialize the Glue client
    glue_client = boto3.client('glue')

    try:
        # Start the Glue job
        response = glue_client.start_job_run(JobName=glue_job_name)

        # Get the Job Run ID
        job_run_id = response['JobRunId']
        print(f'Started Glue job with Job Run ID: {job_run_id}')

        # Optionally, you can return the Job Run ID
        return {
            'statusCode': 200,
            'body': json.dumps({'JobRunId': job_run_id})
        }

    except Exception as e:
        print(f'Error starting Glue job: {str(e)}')
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
```
