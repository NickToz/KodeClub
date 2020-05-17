import sqlite3
conn = sqlite3.connect('Feeling App\\feeling.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE feeling
             (date TEXT, feeling_1 INTEGER, feeling_2 INTEGER, q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER)''')

c.close()