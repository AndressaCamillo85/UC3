import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'compravenda')
cursor = connection.cursor()
sql = "DELETE FROM funcionario WHERE codfuncionario = %s"
data = (4,)
cursor.execute(sql, data)
connection.commit()
recordsaffected = cursor.rowcount
cursor.close()
connection.close()
print(recordsaffected, "registros excluídos")