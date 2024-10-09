# Exercise 1: Subqueries

You’ll work with two tables:

1. Insurance Transactions: Contains details about insurance claims and payments.
2. Policy Holders: Contains details about insurance policy holders.

## Step 1: Setup the Data

### `insurance_transactions.csv`

```
transaction_id,policy_id,transaction_type,transaction_amount,transaction_date
1,101,Claim,5000,2023-01-15
2,102,Claim,12000,2023-02-10
3,103,Premium,1500,2023-03-05
4,101,Premium,2000,2023-04-01
5,104,Claim,7000,2023-05-21
6,105,Premium,1800,2023-06-11
7,103,Claim,3000,2023-07-19
8,102,Premium,2200,2023-08-30
9,106,Claim,9000,2023-09-15
10,104,Premium,2500,2023-10-05
```

### `policy_holders.csv`

```
policy_id,holder_name,holder_age,policy_type,policy_start_date
101,John Doe,45,Home,2020-05-01
102,Jane Smith,34,Auto,2019-06-15
103,Robert Brown,50,Health,2021-07-23
104,Emily Davis,29,Life,2022-08-30
105,Michael Clark,37,Auto,2020-09-12
106,Sarah Johnson,42,Health,2019-12-05
```

## Step 2: Create the Table

After uploading the data to S3, create the following external tables in Athena.

### `insurance_transactions`

```
```

### `policy_holders`

```
```

## Step 3: Subquery Exercises

1. Write a query to find all policy holders who have made a claim in 2023, along with their claim amounts. Use a subquery to retrieve the policy IDs with claims in 2023.

```
```

2. Find all policy holders who have paid a total premium greater than $4000 across all transactions. Use a subquery to sum up the premiums for each policy holder.

```
```

3. Find policy holders who started their policy after 2021, and show their most recent claim amount using a subquery.

```
```

4. Write a query to find all policy holders who have both paid a premium and made a claim in 2023. Use subqueries to check for the presence of both transactions.

```
```

5. Find the average claim amount for each policy type. Use a subquery to aggregate the claims by policy type.

```
```
