# Management 1: Create S3 Bucket for Athena Query Results

Athena requires an S3 bucket to store query results and metadata, such as logs. This exercise focuses on creating and configuring an S3 bucket for that purpose.

## Objectives

* Create and configure an S3 bucket for Athena query results.
* Set the correct S3 bucket path in Athena settings.

## Steps

1. Log in to the AWS Management Console and navigate to the S3 service.
2. Click on Create bucket and give it a unique name, such as `athena-query-results-<your-name>`.
3. Set the Region (choose the same region where you plan to run your Athena queries).
4. Under Bucket settings, leave default configurations for this exercise.
5. After creating the bucket, open Athena and go to Settings (click the gear icon).
6. Set the Query result location to the S3 bucket you just created (e.g., `s3://athena-query-results-<your-name>`).
