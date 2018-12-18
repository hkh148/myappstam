import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="203761333",
    database="projectdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM AnchorTable WHERE Title = 'רבי עקיבא'")
entries = mycursor.fetchall()

for entry in entries:
	print(entry[0])
