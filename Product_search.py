import sqlite3

conn = sqlite3.connect("Products.db")
getProduct = input("Enter the Product code- ")
cursor = conn.execute("SELECT * FROM PRODUCT_DATA WHERE PRODUCT_CODE="+getProduct)

for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Price-", i[2])
    print("Distributor Name-", i[3])
    print("Manufacture Name-", i[4])
    print("------------------------------------------------------")
