import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password= '',
    database= 'compravenda')
cursor = connection.cursor()
sql= "INSERT INTO pedido (qtd, total, formaspagamento, codcliente, codproduto, codfuncionario) VALUES (%s, %s, %s, %s, %s, %s)"
data= (
    10,
    1200,
    'crédito',
    1,
    2,
    3)
cursor.execute(sql, data)
connection.commit ()
codpedido = cursor.lastrowid
cursor.close ()
connection.close ()
print ("Pedido cadastrado com sucesso, seu código é: ", codpedido)