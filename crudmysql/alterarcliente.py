import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'compravenda'
)
cursor = connection.cursor()
sql = "UPDATE cliente SET nome = %s, endereco = %s, cpf = %s WHERE codcliente = %s"
data = (
	'Maria da Silva',
	'Rua CER, 56',
	'034.899.455-09',
	6)
cursor.execute(sql, data)
connection.commit()
recordsaffected = cursor.rowcount
cursor.close()
connection.close()
print(recordsaffected, "registros alteradds")