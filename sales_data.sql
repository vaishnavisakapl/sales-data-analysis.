
-- Create sales table
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
);

-- Insert sample data
INSERT INTO sales (product, quantity, price) VALUES ('Apples', 10, 5.0);
INSERT INTO sales (product, quantity, price) VALUES ('Apples', 15, 5.0);
INSERT INTO sales (product, quantity, price) VALUES ('Bananas', 20, 2.5);
INSERT INTO sales (product, quantity, price) VALUES ('Oranges', 8, 4.0);
INSERT INTO sales (product, quantity, price) VALUES ('Bananas', 12, 2.5);
INSERT INTO sales (product, quantity, price) VALUES ('Oranges', 10, 4.0);
