import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'compravenda')
cursor = connection.cursor()
sql = "DELETE FROM cliente WHERE codcliente = %s"
data = (6,)
cursor.execute(sql, data)
connection.commit()
recordsaffected = cursor.rowcount
cursor.close()
connection.close()
print(recordsaffected, "registros excluídos")