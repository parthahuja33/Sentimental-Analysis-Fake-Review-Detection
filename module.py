import sqlite3
import pandas as pd


class credentials:
    def __init__(self):
        conn = sqlite3.connect("sqlLite.db")
        c = conn.cursor()
        c.execute("""create table if not exists customers(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username varchar(20),
                    password varchar(20),
                    email varchar(40)
                    )
                """)
        self.conn, self.c = conn, c

    def login(self, username, password):
        conn, c = self.conn, self.c
        c.execute('SELECT * FROM customers')
        data = pd.DataFrame(c.fetchall(), columns=['id', 'username', 'password', 'email'])
        print(data)
        if username in list(data['username']) and password in list(data['password']):
            return True
        conn.commit()
        return False

    def signup(self, username, password, email):
        conn, c = self.conn, self.c
        c.execute('SELECT * FROM customers')
        data = pd.DataFrame(c.fetchall(), columns=['username', 'password', 'email'])
        print(data)
        if username in list(data['username']):
            return False
        conn.commit()

        query = """INSERT INTO customers
                                      (username, password, email) 
                                      VALUES (?, ?, ?);"""

        data_tuple = (username, password, email)
        c.execute(query, data_tuple)
        conn.commit()
        return True


class products:
    def __init__(self):
        conn = sqlite3.connect("sqlLite.db")
        c = conn.cursor()
        c.execute("""create table if not exists products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name varchar(20),
                    price varchar(20),
                    description varchar(200)
                    )
                """)
        self.conn, self.c = conn, c

    def add_product(self, name, price, description):
        conn, c = self.conn, self.c
        c.execute('SELECT * FROM products')
        data = pd.DataFrame(c.fetchall(), columns=['id', 'username', 'password', 'email'])
        print(data)
        if name in list(data['username']):
            return False
        conn.commit()
        print(description)
        print('\n\n\n')
        query = """INSERT INTO products
                                      (name, price, description) 
                                      VALUES (?, ?, ?);"""

        data_tuple = (name, price, description)
        c.execute(query, data_tuple)
        conn.commit()
        return True

    def get_products(self):
        conn, c = self.conn, self.c
        c.execute('SELECT * FROM products')
        data = pd.DataFrame(c.fetchall(), columns=['id', 'name', 'price', 'description'])
        return data

    def delete_item(self, id):
        conn, c = self.conn, self.c
        c.execute("DELETE FROM products WHERE id=" + str(id))
        conn.commit()


class reviews:
    def __init__(self):
        conn = sqlite3.connect("sqlLite.db")
        c = conn.cursor()
        c.execute("""create table if not exists reviews(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer varchar(20),
                    name varchar(20),
                    type varchar(20),
                    rating varchar(2),
                    review varchar(200)
                    )
                """)
        self.conn, self.c = conn, c

    def save_review(self, customer, name, type, rating, review):
        conn, c = self.conn, self.c
        query = """INSERT INTO reviews
                                              (customer, name, type, rating, review) 
                                              VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (str(customer), str(name), str(type), str(rating), str(review))
        c.execute(query, data_tuple)
        conn.commit()

    def get_review(self):
        conn, c = self.conn, self.c
        c.execute('SELECT * FROM reviews')
        data = pd.DataFrame(c.fetchall(), columns=['id', 'customer', 'name', 'type', 'rating', 'review'])
        return data

    def delete_fake(self):
        conn, c = self.conn, self.c
        c.execute("DELETE FROM reviews WHERE type='Fake'")
        conn.commit()

    def get_review_name(self, cust):
        conn, c = self.conn, self.c
        c.execute('SELECT * FROM reviews')
        data = pd.DataFrame(c.fetchall(), columns=['id', 'customer', 'name', 'type', 'rating', 'review'])
        data = data[data['customer'] == cust]
        return data

    def delete_review(self, id):
        conn, c = self.conn, self.c
        query = "DELETE FROM reviews WHERE id="+str(id)
        c.execute(query)
        conn.commit()


class data:
    def __init__(self):
        self.arrD = None
        self.id = None
        self.customer = None

    def set_customer(self, customer):
        self.customer = customer

    def set_id(self, id):
        self.id = id

    def set_dict(self, arrD):
        self.arrD = arrD
