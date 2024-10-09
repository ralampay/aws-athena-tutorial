# Example 1: Basic Aggregation Query

## `employee_salaries.csv`

```csv
employee_id,employee_name,department,salary
101,John Doe,Sales,60000
102,Jane Smith,HR,75000
103,Sam Wilson,Engineering,90000
104,Alice Johnson,Engineering,85000
105,Bob Brown,Sales,70000
```

## Create Table Query

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS employee_salaries (
    employee_id INT,
    employee_name STRING,
    department STRING,
    salary INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    'separatorChar' = ',',
    'quoteChar' = '"'
)
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/employee_salaries/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

## Query

```
SELECT department, AVG(salary) AS avg_salary
FROM employee_salaries
GROUP BY department;
```
