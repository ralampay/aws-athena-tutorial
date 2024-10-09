# Example 5: Querying JSON Data

## `customer_data.json`

```
{"customer_id": 1, "name": "John Doe", "address": {"city": "New York", "zip": "10001"}, "age": 30}
{"customer_id": 2, "name": "Jane Smith", "address": {"city": "Los Angeles", "zip": "90001"}, "age": 25}
{"customer_id": 3, "name": "Sam Johnson", "address": {"city": "Chicago", "zip": "60601"}, "age": 35}
```

## Create Table Query

```
CREATE EXTERNAL TABLE IF NOT EXISTS customer_data (
    customer_id INT,
    name STRING,
    address STRUCT<city:STRING, zip:STRING>,
    age INT
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/customer_data/';
```

## Query: Retrieve customer names and their cities.

```
SELECT name, address.city
FROM customer_data;
```
