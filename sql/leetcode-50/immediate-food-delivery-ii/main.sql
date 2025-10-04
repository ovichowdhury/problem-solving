-- https://leetcode.com/problems/immediate-food-delivery-ii/?envType=study-plan-v2&envId=top-sql-50

-- Calculate the percentage of immediate orders
SELECT 
    ROUND(
        (
            COUNT(1) FILTER (WHERE order_date = customer_pref_delivery_date)::NUMERIC 
            / COUNT(1)
        ) * 100,
        2
    ) AS immediate_percentage
FROM (
    SELECT DISTINCT ON (customer_id) *
    FROM delivery
    ORDER BY customer_id, order_date
) AS first_orders;
