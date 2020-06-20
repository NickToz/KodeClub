
import sqlite3
import time
import datetime
import psycopg2 as p

# homwork look for psycopg2 - do what it in quey editor but from python



def main():
    #connect()
    #create_table()
    ask_questions()
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

def feeling_input():
    f = int(input("On a scale of 1 to 10, 1 being the worst, 10 being the best, how are you feeling today? "))
    while f < 1 or f > 10:
        f = int(input('not valid. Please enter a number between 1 and 10:'))
    return f


def ask_questions():
    f0 = feeling_input()
    f1 = feeling_input()
    q1 = q_input("Have you exercised?")
    q2 = q_input("Have you cooked a healthy meal?")
    q3 = q_input("Have you had a meaningful conversation?")
    q4 = q_input("Have you smoked?")
    q5 = q_input("Have you drank alcohol?")
    commit_to_db(datetime.datetime.utcnow(), f0, f1, q1, q2, q3, q4, q5)

def q_input(what_to_ask):
    q = input(what_to_ask)
    # while q not in ("y", "n"):
    #    q = input("please enter y or n")
    if q == "y":
        return True
    else:
        return False


def commit_to_db(timedate,f0,f1,q1,q2,q3,q4,q5):
    c.execute("INSERT INTO feeling (datetime, feeling_0, feeling_1, q1, q2, q3, q4, q5) values ('{}',{},{},{},{},{},{},{})".format(timedate,f0,f1,q1,q2,q3,q4,q5))
    conn.commit()

# one function for feeling scales, one for booleans, one for inserting into database.
# different prompts for feeling inputs
# unique identifier
# tell user whether it's a yes or no question - find smart way - string concatonation.


if __name__=='__main__':
    main()
