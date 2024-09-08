import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='valeria',
        password='')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'email varchar (150) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO books (email, name)'
            'VALUES (%s, %s)',
            ('mark@gmail.com',
             'Evil Incarnate')
            )

conn.commit()

cur.close()
conn.close()