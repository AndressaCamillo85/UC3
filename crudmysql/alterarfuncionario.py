import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'compravenda'
)
cursor = connection.cursor()
sql = "UPDATE funcionario SET nome = %s, cpf = %s, endereco = %s, datanascimento = %s WHERE codfuncionario = %s"
data = (
	'Maria',
	'060.060.060-06',
	'Rua Estrela do Sul, 54',
	'2002-10-02',
    '2')
cursor.execute(sql, data)
connection.commit()
recordsaffected = cursor.rowcount
cursor.close()
connection.close()
print(recordsaffected, "registros alteradds")