DELIMITER //

CREATE TRIGGER ProductSellPriceInsertCheck 
    AFTER INSERT  
    ON Products FOR EACH ROW  
	BEGIN
	IF NEW.SellPrice <= NEW.BuyPrice THEN
		INSERT INTO Notifications(Notification,DateTime) 
		VALUES(CONCAT('A SellPrice same or less than the BuyPrice was inserted for ProductID ', NEW.ProductID), NOW()); 
    END IF;
	END;//

DELIMITER;
