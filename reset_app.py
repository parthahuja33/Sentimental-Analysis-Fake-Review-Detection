import sqlite3

conn = sqlite3.connect("sqlLite.db")

c = conn.cursor()
query = '''drop table customers'''
c.execute(query)

conn.commit()

c = conn.cursor()
query = '''drop table reviews'''
c.execute(query)

conn.commit()

c = conn.cursor()
query = '''drop table products'''
c.execute(query)

conn.commit()

conn.close()