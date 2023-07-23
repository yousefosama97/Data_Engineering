CREATE PROCEDURE GetDiscount(IN Ordernum INT)
BEGIN
    SELECT 
        CASE 
            WHEN Quantity >= 20 THEN Cost * (1 - 0.2) 
            WHEN Quantity < 20 AND Quantity >= 10 THEN Cost * (1 - 0.1)
            ELSE Cost
        END AS cost_after_discount
    FROM 
        (SELECT Quantity, Cost FROM Orders WHERE OrderID = Ordernum) AS x;
END//

