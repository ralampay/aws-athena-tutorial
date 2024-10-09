# Management 3: Setup Cloudtrail for Logging

Athena integrates with AWS CloudTrail to log activity, such as when queries are run or results are fetched. This exercise focuses on configuring CloudTrail to monitor and log Athena actions.

## Objectives

* Set up AWS CloudTrail to log Athena activity.
* Create a trail to store logs in an S3 bucket.
* Verify that query activities are being logged.

## Steps

1. Navigate to AWS CloudTrail in the Management Console.
2. Click Create trail.
3. Name the trail (e.g., athena-query-logging-trail).
4. In the Management Events section, select Read/Write events and choose both read and write.
5. In the S3 section, choose or create an S3 bucket for CloudTrail logs.
6. Save and enable the trail.
7. Return to Athena and run some test queries. Then, go back to CloudTrail to check if the events (like the queries run) are being logged.
