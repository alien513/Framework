import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            r"/mnt/d/learn/Framework" + r"/become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
        return True

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # ----------------- Individual Part ---------------------
    def insert_user(self, id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
                VALUES ({id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_user_name_by_id(self, user_id):
        query = f"SELECT name FROM customers WHERE id = {user_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_user_name_by_id(self, id, name):
        query = f"UPDATE customers SET name = '{name}' WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_user_by_id(self, id):
        query = f"DELETE FROM customers WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_order(self, id, customer_id, product_id):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
                VALUES ({id}, {customer_id}, {product_id}, datetime())"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_order_by_id(self, id):
        query = f"DELETE FROM orders WHERE id = {id}"
        self.cursor.execute(query)
        self.connection.commit()