# Management 2: Create a New Workgroup in Athena

Athena requires an S3 bucket to store query results and metadata, such as logs. This exercise focuses on creating and configuring an S3 bucket for that purpose.

## Objectives

* Create a new workgroup with customized settings.
* Configure a different query result location.
* Set cost control limits for the workgroup.

## Steps

1. Go to the AWS Athena Console.
2. Click on Workgroups in the left panel.
3. Click Create workgroup and provide a name (e.g., analytics_team_workgroup).
4. Under Query result location, specify a different S3 bucket from the default one, or create a new S3 bucket (like in Exercise 1).
5. Enable cost controls by specifying a per-query or per-workgroup data scanning limit. Set a low limit for testing (e.g., 1 GB).
6. Click Create workgroup.
