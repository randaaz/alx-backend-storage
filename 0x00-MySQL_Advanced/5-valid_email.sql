-- Create a trigger to invalidate a user's email address when it is updated.
-- when the email changed.
DELIMITER $$ 
CREATE TRIGGER email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email
THEN
    SET NEW.valid_email = 0;
END IF;
END
$$
DELIMITER ;
