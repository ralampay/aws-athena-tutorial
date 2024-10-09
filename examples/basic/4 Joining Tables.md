# Example 4: Joining Tables

## `customers.csv`

```
customer_id,customer_name,city
101,Alice Smith,New York
102,Bob Johnson,Los Angeles
103,Charlie Davis,Chicago
104,Dana Lee,Seattle
```

## `orders.csv`

```
order_id,customer_id,product,quantity
5001,101,Laptop,1
5002,102,Headphones,3
5003,103,Smartphone,2
5004,104,Desk Chair,1
```

## Create Table Queries

### Customers

```
CREATE EXTERNAL TABLE IF NOT EXISTS customers (
    customer_id INT,
    customer_name STRING,
    city STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '"'
)
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/customers/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

### Orders

```
CREATE EXTERNAL TABLE IF NOT EXISTS orders (
    order_id INT,
    customer_id INT,
    product STRING,
    quantity INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '"'
)
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/orders/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

## Query: Find all orders along with customer names and cities by joining the customers and orders tables.

```
SELECT o.order_id, c.customer_name, c.city, o.product, o.quantity
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
```
