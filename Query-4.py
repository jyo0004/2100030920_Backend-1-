import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='exam_repository'
)

try:
    cusor=conn.cursor()

    query="SELECT p.ProductName,p.Price,o.OrderId from products p left join orderitems o on p.ProductID=o.ProductID order by o.OrderId"

    cusor.execute(query)

    result=cusor.fetchall()

    for row in result:
        print(row)
        
except Exception as e:
    print(e)