import sqlite3

con = sqlite3.connect('applied.db')
curs = con.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS Applied_Jobs (jobs INTEGER)')

curs.execute("SELECT jobs FROM Applied_Jobs")
row = curs.fetchone()

if row is None:
    curs.execute("INSERT INTO Applied_Jobs (jobs) VALUES (0)")
    con.commit()
    print("Starting Value Set!")
else:
    print("No need to set starting!")
con.commit()

