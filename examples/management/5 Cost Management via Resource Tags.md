# Management 5: Set Up Resource Tags for Athena Cost Management

Athena allows you to add resource tags to help track and allocate costs for Athena usage, such as different teams or projects.

## Objectives

* Add resource tags to track Athena costs.
* Use key-value pairs to categorize Athena usage by teams or projects.

## Steps

1. In the AWS Management Console, navigate to Athena.
2. Click on Workgroups and select the workgroup you created earlier.
3. Go to the Tags section and click Add tags.
4. Add key-value pairs that identify which department or project this workgroup belongs to. For example:
    * Key: `Project`, Value: `SalesAnalytics`
    * Key: `Department`, Value: `Marketing`
5. Save the tags.
6. Later, use AWS Cost Explorer to filter costs by tags and see how much each project or team is spending on Athena.
