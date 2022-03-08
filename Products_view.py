import sqlite3

conn = sqlite3.connect("Products.db")

cursor = conn.execute("SELECT * FROM PRODUCT_DATA")

for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Price-", i[2])
    print("Distributor Name-", i[3])
    print("Manufacture Name-", i[4])
    print("------------------------------------------------------")
