# Advanced Example 6: Correlated Subquery

**Explanation:**

* This query selects products that have sold more than the average quantity of products in their respective category.
* The subquery computes the average quantity sold for each category, and the outer query filters products that exceed this average.

## `product_sales.csv`

```
product_id,product_name,category,quantity_sold,price
1,Laptop,Electronics,100,1000
2,Headphones,Electronics,200,150
3,Desk Chair,Furniture,50,250
4,Coffee Table,Furniture,40,300
5,Smartphone,Electronics,150,800
6,Tablet,Electronics,120,500
7,Sofa,Furniture,30,1200
8,Monitor,Electronics,80,300
9,Bookshelf,Furniture,20,200
10,TV,Electronics,90,900
11,Bed,Furniture,10,1500
12,Washing Machine,Appliances,25,800
13,Refrigerator,Appliances,15,1200
14,Microwave,Appliances,35,400
15,Oven,Appliances,20,1000
16,Fan,Appliances,100,100
17,Smartwatch,Electronics,250,200
18,Camera,Electronics,70,600
19,Soundbar,Electronics,60,300
20,Dishwasher,Appliances,15,700
```

## Query: Category with the Maximum Total Revenue (Subquery in SELECT)

```
SELECT category, SUM(quantity_sold * price) AS total_revenue
FROM product_sales
GROUP BY category
HAVING SUM(quantity_sold * price) = (
    SELECT MAX(total_revenue) 
    FROM (
        SELECT SUM(quantity_sold * price) AS total_revenue
        FROM product_sales
        GROUP BY category
    ) category_revenues
);
```
