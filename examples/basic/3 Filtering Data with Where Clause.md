# Example 3: Filtering Data with `WHERE` Clause

## `customer_orders.csv`

```
order_id,customer_name,product_id,order_date,quantity
5001,Alice Smith,1,2024-01-10,2
5002,Bob Johnson,3,2024-02-15,1
5003,Charlie Davis,2,2024-03-20,5
5004,Dana Lee,1,2024-04-18,3
5005,Eva Brown,5,2024-04-22,2
```

## Create Table Query

```
CREATE EXTERNAL TABLE IF NOT EXISTS customer_orders (
    order_id INT,
    customer_name STRING,
    product_id INT,
    order_date STRING,
    quantity INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '"'
)
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/customer_orders/'
TBLPROPERTIES ('skip.header.line.count'='1');
```
