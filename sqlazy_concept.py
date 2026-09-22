import sqlite3

# This is a simplified demonstration of the core concept behind SQLazy:
# making database interaction more intuitive and less reliant on raw SQL.
# In a real-world SQLazy, this would involve a GUI or a more abstract API.

def create_and_populate_database(db_name='mydatabase.db'):
    """Creates an SQLite database and populates it with sample data."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create a table for 'products'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    # Insert some sample products
    products_data = [
        ('Laptop', 1200.50, 50),
        ('Keyboard', 75.00, 150),
        ('Mouse', 25.99, 200),
        ('Monitor', 300.75, 75)
    ]
    cursor.executemany('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', products_data)

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created and populated.")

def get_products_above_price(price_threshold, db_name='mydatabase.db'):
    """Retrieves products with a price above a given threshold using a simplified approach."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Instead of writing complex SQL, imagine a more abstract query builder or filter.
    # Here, we're still using SQL for demonstration, but the idea is to abstract this.
    query = "SELECT name, price FROM products WHERE price > ?"
    cursor.execute(query, (price_threshold,))

    results = cursor.fetchall()
    conn.close()
    return results

def get_low_stock_products(stock_threshold, db_name='mydatabase.db'):
    """Retrieves products with stock below a given threshold."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Another example of an intuitive query concept.
    query = "SELECT name, stock FROM products WHERE stock < ?"
    cursor.execute(query, (stock_threshold,))

    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    db_file = 'sqlazy_demo.db'
    create_and_populate_database(db_file)

    print("\n--- Products with price > $100 ---")
    expensive_products = get_products_above_price(100, db_file)
    for product in expensive_products:
        print(f"- {product[0]} (${product[1]:.2f})")

    print("\n--- Products with stock < 100 ---")
    low_stock = get_low_stock_products(100, db_file)
    for product in low_stock:
        print(f"- {product[0]} (Stock: {product[1]})")
