import sqlite3

conn=sqlite3.connect('testing.db')
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE example (language VARCHAR, level TEXT, Version REAL)")

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 'Beginner', 2.7)")
    c.execute("INSERT INTO example VALUES('Python', 'Intermediate', 3.4)")
    c.execute("INSERT INTO example VALUES('Python', 'Expert', 2.6)")

enter_data()

conn.close()
