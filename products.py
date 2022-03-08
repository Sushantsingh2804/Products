import sqlite3

conn = sqlite3.connect("Products.db")

conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCT_DATA(
                PRODUCT_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT,
                PRICE INTEGER, 
                DISTRIBUTOR_NAME TEXT,
                MANUFACTURE_NAME TEXT
                );
''')
print(" Table Creation Successful ")

getName = input("Enter the Name-")
getPrice = input("Enter the Price-")
getDis = input("Enter the Distributor Name-")
getMan = input("Enter the Manufacture Name-")

conn.execute("INSERT INTO PRODUCT_DATA (NAME,PRICE,DISTRIBUTOR_NAME,MANUFACTURE_NAME) VALUES('"+getName+"',"+getPrice+",'"+getDis+"','"+getMan+"')")
conn.commit()
conn.close()
print("Entry successful")