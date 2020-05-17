
import sqlite3
import time
import datetime

def main():
    create_table()
    insert_feeling_1()
  
conn = sqlite3.connect('feeling.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS feeling
             (date TEXT, feeling_1 INTEGER, feeling_2 INTEGER, q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER)''')

def insert_feeling_1():
    feeling_1 = int(input("On a scale of 1 to 10, 1 being the worst, 10 being the best, how are you feeling today? "))
    while feeling_1 < 1 or feeling_1 > 10:
      int(input('not valid. Please enter a number between 1 and 10:'))
    c.execute("INSERT INTO feeling (feeling_1) VALUES (?)",
    (feeling_1))
    conn.commit()





if __name__=='__main__':
    main()
