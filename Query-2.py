import mysql.connector
import datetime

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='exam_repository'
)

try:
    cusor=conn.cursor()


    query="""SELECT p.ProductName as orders,o.orderdate,monthname(o.orderdate) as monthname 
            FROM orders o 
            join orderitems oi on oi.orderid=o.orderid 
            join products p on p.productid=oi.productid
            where YEAR(OrderDate)=2023 and MONTHNAME(OrderDate)="January" """

    cusor.execute(query)

    result=cusor.fetchall()

    for row in result:
        formatted_row = tuple(
            col.strftime('%Y-%m-%d') if isinstance(col, datetime.date) else col
            for col in row
        )
        print(formatted_row)
        
except Exception as e:
    print(e)