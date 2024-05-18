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

    query="SELECT * FROM customers"

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