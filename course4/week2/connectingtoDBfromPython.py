import sqlite3

#------connecting to the db-------#
con=sqlite3.connect(r"C:\Users\saran\Desktop\python_michighan\course4\week2\databases\sample.db")
cur=con.cursor()
#--running query using execute-------#
#-----printing data within table-----#
#-------con.execute("SELECT * FROM users") executes select query----#

for row in con.execute("SELECT * FROM Ages"):
	print(row)

print("---------using fetch one--------")
fi=cur.execute("SELECT * FROM Ages")
name=cur.fetchone()
print(name)
print(type(name))

