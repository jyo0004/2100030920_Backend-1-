import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='exam_repository'
)

try:
    cusor=conn.cursor()

    query="""SELECT p.productname,sum(oi.quantity) as total
            from orderitems oi
            join products p on oi.productid=p.productid
            group by p.productname order by total desc limit 1"""

    cusor.execute(query)

    result=cusor.fetchall()

    for row in result:
        print(row)
        
except Exception as e:
    print(e)