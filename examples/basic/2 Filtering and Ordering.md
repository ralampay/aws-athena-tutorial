# Example 2: Filtering and Ordering

## `product_sales.csv`

```
product_id,product_name,category,quantity_sold,price
1,Laptop,Electronics,100,1000
2,Headphones,Electronics,200,150
3,Desk Chair,Furniture,50,250
4,Coffee Table,Furniture,40,300
5,Smartphone,Electronics,150,800
```

## Create Table Query

```
CREATE EXTERNAL TABLE IF NOT EXISTS product_sales (
    product_id INT,
    product_name STRING,
    category STRING,
    quantity_sold INT,
    price INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '"'
)
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/product_sales/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

## Query

```
SELECT product_name, quantity_sold * price AS revenue
FROM product_sales
ORDER BY revenue DESC
LIMIT 3;
```
