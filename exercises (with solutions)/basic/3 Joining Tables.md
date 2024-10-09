# Exercise 3: Joining Tables

This exercise will guide you through the steps of creating two related tables, and performing a join to retrieve meaningful combined data.

## Step 1: Create and upload data

### `product_sales.csv`

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
```

### `product_details.csv`

```
product_id,manufacturer,product_type
1,Samsung,Smartphone
2,Sony,Accessory
3,Nike,Apparel
4,Levi's,Apparel
5,LG,Appliance
6,Ninja,Appliance
7,Apple,Smartphone
8,Adidas,Apparel
```

## Step 2: Create Tables

### `product_sales`

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
LOCATION 's3://your-bucket-name/path-to-product-sales-csv/'
TBLPROPERTIES ('has_encrypted_data'='false');
```

### `product_details`

```
CREATE EXTERNAL TABLE IF NOT EXISTS product_details (
    product_id INT,
    manufacturer STRING,
    product_type STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '"'
)
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/path-to-product-details-csv/'
TBLPROPERTIES ('has_encrypted_data'='false');
```

## Step 3: Perform the Join

Join the tables together via `product_id`.

```
SELECT
    ps.product_id,
    ps.product_name,
    ps.category,
    ps.quantity_sold,
    ps.price,
    pd.manufacturer,
    pd.product_type
FROM product_sales ps
JOIN product_details pd
ON ps.product_id = pd.product_id;
```

## Step 4: Filter the Results from the Join

Next, filter the results to show only products in the Electronics category.

```
SELECT
    ps.product_id,
    ps.product_name,
    ps.category,
    ps.quantity_sold,
    ps.price,
    pd.manufacturer,
    pd.product_type
FROM product_sales ps
JOIN product_details pd
ON ps.product_id = pd.product_id
WHERE ps.category = 'Electronics';
```

## Step 5: Other Business Requirements

1. Modify the join query to show only products where the quantity_sold is greater than 50.
2. Write a query to join the tables and calculate the total sales (quantity sold multiplied by price) for each product.
3. Modify the join query to show only Clothing products and order the result by price in descending order.
