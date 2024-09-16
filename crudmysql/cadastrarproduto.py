import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password= '',
    database= 'compravenda')
cursor = connection.cursor()
sql= "INSERT INTO produto (nomeproduto, qtd, valor) VALUES (%s, %s, %s)"
data= (
    'Pen Drive',
    '20',
    '400')
cursor.execute(sql, data)
connection.commit ()
codcliente = cursor.lastrowid
cursor.close ()
connection.close ()
print ("Produto cadastrado com sucesso, seu código é: ", codproduto)