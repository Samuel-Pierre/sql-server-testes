import string
import pyodbc
import pandas as pd


def inserir():
    print("Digite o Email que voce gostaria de inserir no banco de dados")
    novo_email = input("Email: ")
    cursor.execute(f"INSERT INTO teste(id_teste)VALUES('{novo_email}')")
    cursor.commit()
    print('Cadastro efetuado com sucesso')
    df = pd.read_sql_query('SELECT * FROM teste', conectar)
    print(df)


def deletar():
    df = pd.read_sql_query('SELECT * FROM teste', conectar)
    print(df)
    print("Qual email voce gostaria de deletar?")
    eliminar_email = input("Email: ")
    cursor = conectar.cursor()
    cursor.execute(f"DELETE FROM teste WHERE id_teste = ('{eliminar_email}')")
    cursor.commit()
    print('Item deletado com sucesso')
    df = pd.read_sql_query('SELECT * FROM teste', conectar)
    print(df)


conexao = ('Driver={SQL Server};'
           'Server=SAO3D002880;'
           'Database=teste;'
           'Trusted_Connection=yes;')

conectar = pyodbc.connect(conexao)

cursor = conectar.cursor()

print("1 - Adicionar  2 - Eliminar")

escolha = int(input("O que voce gostaria de fazer?: "))

if(escolha == 1):
    inserir()
elif(escolha == 2):
    deletar()

# email = input("Digite seu email aqui: ")

# cursor.execute(f"INSERT INTO teste(id_teste)VALUES('{email}')")

# # cursor.execute("DELETE FROM teste WHERE id_teste = 'frufrufru'")

# cursor.commit()

# df = pd.read_sql_query('SELECT * FROM teste', conectar)

# print(df)
