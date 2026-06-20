import sqlite3

con = sqlite3.connect('applied.db')
curs = con.cursor()
curs.execute('CREATE TABLE Applied_Jobs (jobs)')
