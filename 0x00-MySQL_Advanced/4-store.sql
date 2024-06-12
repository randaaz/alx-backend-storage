-- Create a trigger to update the quantity of items after an order is inserted.
CREATE TRIGGER buy_trigger
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
