from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, lit
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.appName("ImputeMissingValues").getOrCreate()

# Sample data
data = [
    (1, 1001, "Home", 1200.50, "2024-01-01"),
    (2, 1002, "Auto", None, "2024-01-02"),
    (3, None, "Auto", 750.00, "2024-01-03"),
    (4, 1004, "Life", 400.00, None),
    (5, 1005, None, 900.00, "2024-01-05")
]

# Define schema
columns = ["transaction_id", "customer_id", "policy_type", "transaction_amount", "transaction_date"]

# Create DataFrame
df = spark.createDataFrame(data, schema=columns)

# Impute 'customer_id' with mean value
mean_customer_id = df.select(mean(col("customer_id"))).collect()[0][0]
df = df.na.fill({"customer_id": mean_customer_id})

# Impute 'policy_type' with most frequent value (mode)
most_frequent_policy_type = df.groupBy("policy_type").count().orderBy("count", ascending=False).first()[0]
df = df.na.fill({"policy_type": most_frequent_policy_type})

# Impute 'transaction_amount' with mean value
mean_transaction_amount = df.select(mean(col("transaction_amount"))).collect()[0][0]
df = df.na.fill({"transaction_amount": mean_transaction_amount})

# Impute 'transaction_date' with a default date
df = df.na.fill({"transaction_date": "2024-01-01"})

# Show result
df.show()

