# Mini Capstone Project

## Objective:

You will work with a dataset of insurance transactions containing null values that need to be imputed. The workflow will involve:

1. Uploading the dataset to an S3 bucket.
2. Triggering an AWS Lambda function that processes the data by imputing missing values using PySpark and re-uploading it to another S3 bucket.
3. Triggering another Lambda function that starts an AWS Glue job to perform aggregation on the processed data and store the results in a third S3 bucket.
4. Verifying the results using AWS Athena.

## Dataset Prepartaion

1. Create a CSV file named `insurance_transactions.csv` with the following schema:

```
transaction_id,customer_id,policy_type,transaction_amount,transaction_date
1,1001,Home,1200.50,2024-01-01
2,1002,Auto,,2024-01-02
3,,Auto,750.00,2024-01-03
4,1004,Life,400.00,
5,1005,,900.00,2024-01-05
```
Notice that `transaction_amount`, `customer_id`, `policy_type`, and `transaction_date` have missing values.

2. Upload to S3 (Bucket A):

Upload the CSV file to an S3 bucket (e.g., `insurance-raw-bucket`).

## Lambda Function for Triggering AWS Glue

1. Create a lambda function that is triggered upon uploading of raw insurance transactions.

2. The lambda function will have to then trigger an AWS Glue Job which contains the following logic:

* Check if the uploaded file has null values.
* If yes, then perform imputation before uploading to `insurance-processed-bucket`
* If no, then simply upload the file to `insurance-procssed-bucket`

## Lambda Function for Triggering AWS Glue for aggregation

1. Create a lambda function that is triggered upon uploading of `insurance-processed-bucket`

2. The lambda function will have to then trigger another AWS Glue Job which contains the following logic:

* Perform aggregation to group by `policy_type`.
* Upload the results to another bucket `insurance-final-bucket`

## Athena Query

Use athena to verify that the results have indeed been triggered.

1. Create a database in athena.
2. Create a table in athena that points to `insurance-final-bucket`.
3. Perform a `SELECT` statement that verifies if the files have been uploaded.
