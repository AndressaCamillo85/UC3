import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'compravenda'
)
cursor = connection.cursor()
sql = "UPDATE produto SET nomeproduto = %s, qtd = %s, valor = %s WHERE codproduto = %s"
data = (
	'Monitor',
	20,
	35000,
	4)
cursor.execute(sql, data)
connection.commit()
recordsaffected = cursor.rowcount
cursor.close()
connection.close()
print(recordsaffected, "registros alteradds")