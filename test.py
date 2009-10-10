# written by Simon Norber 2009 feel free to use it for any purpose
#you need to install MySQLdb first eg. sudo apt-get install python-mysql in
#debian and probobly debian derivates like ubuntu too.
import MySQLdb

conn = MySQLdb.connect(host = "sheeva.bsnet.se",
	       	       user = "bank",
		       passwd = "some_pass",
		       db = "bank")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS test")
# the use of """ alow for multiline text
cursor.execute("""CREATE TABLE test(
		id int PRIMARY KEY auto_increment,
		firstName varchar(20),
		sureName varchar(30)
	        )""")
names = (("Erik", "Ponti"), ("Peter", "Andersson"), ("Nisse", "Hult"))
for name in names:
	cursor.execute("INSERT INTO test VALUES(null, %s, %s)",
			[name[0],name[1]])
cursor.execute("SELECT * from test")
result = cursor.fetchall()
for row in result:
	print row[0], row[1], row[2]

cursor.close()	
conn.commit()
conn.close()



