import sqlite3

conn = sqlite3.connect("Products.db")
getProduct = input("Enter the Product code- ")

getName = input("Enter the Name-")
getPrice = input("Enter the Price-")
getDis = input("Enter the Distributor Name-")
getMan = input("Enter the Manufacture Name-")
cursor = conn.execute("UPDATE PRODUCT_DATA SET NAME= '"+getName+"',PRICE= "+getPrice+",DISTRIBUTOR_NAME='"+getDis+"',MANUFACTURE_NAME='"+getMan+"' WHERE PRODUCT_CODE="+getProduct)
conn.commit()
print("Record Updated successfully")
cursor = conn.execute("SELECT * FROM PRODUCT_DATA WHERE PRODUCT_CODE="+getProduct)

for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Price-", i[2])
    print("Distributor Name-", i[3])
    print("Manufacture Name-", i[4])
    print("------------------------------------------------------")