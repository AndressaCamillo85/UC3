import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password= '',
    database= 'compravenda')
cursor = connection.cursor()
sql= "INSERT INTO funcionario (nome, cpf, endereco, datanascimento) VALUES (%s, %s, %s, %s)"
data= (
    'Andressa Camillo',
    '105.645.957-30',
    'Estrada dos Palmares, 4085',
    '1985-08-08')
cursor.execute(sql, data)
connection.commit ()
codcliente = cursor.lastrowid
cursor.close ()
connection.close ()
print ("Funcionário cadastrado com sucesso, seu código é: ", codfuncionario)