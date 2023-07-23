DELIMITER //

CREATE TRIGGER ProductSellPriceUpdateCheck 
    AFTER UPDATE  
    ON Products FOR EACH ROW  
	BEGIN
	IF NEW.SellPrice <= NEW.BuyPrice THEN
		INSERT INTO Notifications(Notification,DateTime) 
		VALUES(CONCAT(NEW.ProductID,' was updated with a SellPrice of ', NEW.SellPrice,' which is the same or less than the BuyPrice'), NOW()); 
    END IF;
	END;

DELIMITER;
