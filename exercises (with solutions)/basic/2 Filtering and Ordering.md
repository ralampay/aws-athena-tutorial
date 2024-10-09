# Exercise 2: Filtering and Ordering

You will create a table in AWS Athena, upload sales data to an S3 bucket, and run queries that filter and order the data.

## Step 1: Upload Sales Data to S3

First, create and upload the following CSV data to your S3 bucket:

```
product_id,product_name,category,quantity_sold,price
1,Smartphone,Electronics,50,700
2,Headphones,Electronics,100,100
3,T-shirt,Clothing,200,20
4,Jeans,Clothing,150,50
5,Microwave,Home Appliances,30,150
6,Blender,Home Appliances,80,80
7,Laptop,Electronics,30,1200
8,Jacket,Clothing,120,100
9,Refrigerator,Home Appliances,10,500
```

## Step 2: Create an Athena Table

Provide the `CREATE TABLE` query.

```
CREATE EXTERNAL TABLE IF NOT EXISTS product_sales (
    product_id INT,
    product_name STRING,
    category STRING,
    quantity_sold INT,
    price DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '"'
)
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/path-to-your-csv/'
TBLPROPERTIES ('has_encrypted_data'='false');
```

## Step 3: Filter and Order 1

Filter the sales data to show only products in the Clothing category.

```
SELECT product_name, category, quantity_sold, price
FROM product_sales
WHERE category = 'Clothing';
```

## Step 4: Filter and Order 2

Filter the data to show only products in the Electronics category, then order the results by price in descending order.

```
SELECT product_name, category, quantity_sold, price
FROM product_sales
WHERE category = 'Electronics'
ORDER BY price DESC;
```

## Step 5: Combined Filtering and Ordering

Now, filter the data to show products where the quantity_sold is greater than 50, and order the results by quantity_sold in ascending order.

```
SELECT product_name, category, quantity_sold, price
FROM product_sales
WHERE quantity_sold > 50
ORDER BY quantity_sold ASC;
```
