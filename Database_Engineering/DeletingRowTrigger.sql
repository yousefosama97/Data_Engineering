DELIMITER //

CREATE TRIGGER NotifyProductDelete 
    AFTER DELETE   
    ON Products FOR EACH ROW   
	INSERT INTO Notifications(Notification, DateTime) 
    VALUES(CONCAT('The product with a ProductID ', OLD.ProductID,' was deleted'), NOW()); 

DELIMITER ;
