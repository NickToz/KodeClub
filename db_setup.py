import sqlite3
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE weather
             (date text, postcode text, description text, temperature real)''')

c.close()