# Lambda Invoke Athena

From a lambda function, invoke a saved query.

```python
import json
import boto3
import time

def lambda_handler(event, context):
    # Define the necessary parameters
    saved_query_id = 'your_saved_query_id'  # Replace with your saved query ID
    output_location = 's3://your-bucket-name/path/to/store/results/'  # Output location

    # Initialize the Athena client
    client = boto3.client('athena')

    # Retrieve the saved query
    saved_query = client.get_named_query(NamedQueryId=saved_query_id)
    query_string = saved_query['NamedQuery']['QueryString']
    print(f'Executing saved query: {query_string}')

    # Start the query execution
    response = client.start_query_execution(
        QueryString=query_string,
        QueryExecutionContext={
            'Database': saved_query['NamedQuery']['Database']  # Use the database from the saved query
        },
        ResultConfiguration={
            'OutputLocation': output_location,
            'EncryptionConfiguration': {
                'EncryptionOption': 'SSE_S3'  # Change as needed
            }
        }
    )

    # Get the query execution ID
    query_execution_id = response['QueryExecutionId']
    print(f'Started query with execution ID: {query_execution_id}')

    # Wait for the query to complete
    while True:
        query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
        status = query_status['QueryExecution']['Status']['State']
        
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            print(f'Query status: {status}')
            break
        
        print('Waiting for query to complete...')
        time.sleep(2)

    # If the query succeeded, fetch the results
    if status == 'SUCCEEDED':
        results = client.get_query_results(QueryExecutionId=query_execution_id)
        # Process the results as needed
        return {
            'statusCode': 200,
            'body': json.dumps(results['ResultSet']['Rows'])
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Query failed'})
        }
```
