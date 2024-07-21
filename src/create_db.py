from sqlite3 import connect

def create_database():
    """Script to create the database and tables"""
    with connect("database.db") as conn:
        cursor = conn.cursor()

        # Create Users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id TEXT PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT UNIQUE,
                            password TEXT,
                            date_of_birth TEXT
                          )''')

        # Create Products table
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            product_id TEXT PRIMARY KEY,
                            name TEXT,
                            category TEXT,
                            price REAL,
                            stock INTEGER
                          )''')

        # Create Orders table
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                            order_id TEXT PRIMARY KEY,
                            user_id TEXT,
                            product_id TEXT,
                            quantity INTEGER,
                            total_price REAL,
                            order_date TEXT,
                            shipping_address TEXT,
                            payment_method TEXT,
                            payment_status TEXT,
                            FOREIGN KEY (user_id) REFERENCES users (user_id),
                            FOREIGN KEY (product_id) REFERENCES products (product_id)
                          )''')
        conn.commit()

def clear_db():
    """Clear all data from the database"""
    with connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users")
        cursor.execute("DELETE FROM products")
        cursor.execute("DELETE FROM orders")
        conn.commit()

if __name__ == "__main__":
    # create_database()
    clear_db()
