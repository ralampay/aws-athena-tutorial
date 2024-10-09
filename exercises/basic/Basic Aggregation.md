# Exercise 1: Basic Aggregation

Let’s create a basic aggregation query in AWS Athena using a sample table. The query will calculate the total sales per product category by summing up the quantity_sold and multiplying it by the price.

## Step 1: Create an S3 Bucket and Upload a CSV File

First, upload a CSV file with the following sales data into S3 bucket:

```
product_id,product_name,category,quantity_sold,price
1,Smartphone,Electronics,50,700
2,Headphones,Electronics,100,100
3,T-shirt,Clothing,200,20
4,Jeans,Clothing,150,50
5,Microwave,Home Appliances,30,150
6,Blender,Home Appliances,80,80
```

## Step 2: Create an Athena Table

Provide the `CREATE TABLE` query for `sales_data`

```
```

## Step 3: Aggregation Query

Create a basic aggregation query to calculate the total sales per category.

```
```
