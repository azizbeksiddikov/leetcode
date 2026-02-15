# Link: https://leetcode.com/problems/product-sales-analysis-i/description/

# SQL Query:
"""
SELECT p.product_name, s.year, s.price
FROM Product p
JOIN Sales s ON s.product_id = p.product_id
"""
