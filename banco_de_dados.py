import pyodbc
import pandas as pd

# Driver é SQL Server o servidor é o nome que aparece na tela de login do sql server, o database é o nome da tabela que foi criada
conexao = ('Driver={SQL Server};'
           'Server=SAO3D002880;'
           'Database=PythonSQL;'
           'Trusted_Connection=yes;')

conectar = pyodbc.connect(conexao)
print('Conexão efetuada com sucesso')

cursor = conectar.cursor()

cursor.execute("DELETE FROM Vendas WHERE produto = 'avião'")


conectar.commit()


df = pd.read_sql_query('SELECT * FROM Vendas', conectar)

print(df)
