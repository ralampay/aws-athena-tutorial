# Management 4: Configure Data Compression for Athena Query Results

This exercise focuses on enabling data compression for query results to reduce storage costs and improve performance when storing query results in S3.

## Objectives

* Enable compression for query results
* Test different compression formats
* Verify compressed query results in S3

## Steps

1. Open the Athena Console.
2. Go to Workgroups and select your workgroup.
3. Click Edit on the workgroup’s configuration.
4. Scroll down to Query result configuration and look for the Compression setting.
5. Select a compression format, such as GZIP or Snappy.
6. Save the configuration.
7. Run a query and check the S3 bucket where the results are stored. The result files should now be compressed.
