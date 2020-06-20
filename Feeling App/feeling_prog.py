
import sqlite3
import time
import datetime
import psycopg2 as p

# homwork look for psycopg2 - do what it in quey editor but from python



def main():
    #connect()
    #create_table()
    insert_feeling_1()
    show_rows()
    
  
"""USE THIS IF USING SQLite3

conn = sqlite3.connect('feeling.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS feeling
             (date TEXT, feeling_0 INTEGER, feeling_1 INTEGER, q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER)''')

"""

# FOR CONNECTING WITH POSTGRES DB

# postgres host  ec2-54-75-246-118.eu-west-1.compute.amazonaws.com

#def connect():
conn = p.connect("dbname=d45ir25h8c6ka user=jkqlddsqykkyqw host=ec2-54-75-246-118.eu-west-1.compute.amazonaws.com password=7c7329ca43ab68a68f288e770789e4ce0ac4a35b1442367c05ade823f087b5a0")
c = conn.cursor()

def show_rows():
    c.execute("select * from feeling")
    rows = c.fetchall()
    for r in rows:
        print(r)


def insert_feeling_1():
    f1 = int(input("On a scale of 1 to 10, 1 being the worst, 10 being the best, how are you feeling today? "))
    while f1 < 1 or f1 > 10:
      int(input('not valid. Please enter a number between 1 and 10:'))
    c.execute("INSERT INTO feeling (feeling_1) values ({})".format(f1))
    conn.commit()




if __name__=='__main__':
    main()
