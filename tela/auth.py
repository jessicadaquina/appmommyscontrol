import os
from flet import *
import mysql.connector
# from tela_login import tela_login

#conexão banco de dados
conexao = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '',
database = 'mommy'
)

cursor = conexao.cursor()

# # Verificando as credenciais do usuário
# def credenciais(tela_login):
#     tela_login
    
#     try:
#         consulta = "SELECT * FROM user WHERE self.email = %s AND self.password = %s"
#         cursor.execute(consulta, (self.email, self.password))
#         result = cursor.fetchone

#         if result:
#             print("Usuário autenticado com sucesso!")
#         else:
#             print("Credenciais inválidas. Tente novamente!")
            
#         cursor.close()

#     except mysql.connector.Error as err:
#         print(f"Erro: {err}")

# Inicie o aplicativo Flet
# app(target=login)


# tentativa 2
import bcrypt
from databasetentativa2 import get_connection

# registrando cadastro do responsável
def register_user(email, password, full_name, birthday, cellphone):
    connection = get_connection()
    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO cadastro_responsavel (user_email, password, full_name, birthday, cellphone) VALUES (%s, %s, %s, %s, %s)", (email, hashed_password, full_name, birthday, cellphone))
    connection.commit()
    cursor.close()
    connection.close()

def login_user(email, password):
    connection = get_connection()
    cursor = connection.cursor()

    # Verificar na tabela cadastro_responsavel
    cursor.execute("SELECT password FROM cadastro_responsavel WHERE user_email = %s", (email,))
    result = cursor.fetchone()
    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        cursor.close()
        connection.close()
        return "responsavel"

    # Verificar na tabela cadastro_dependente
    cursor.execute("SELECT password FROM cadastro_dependente WHERE user_email = %s", (email,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        return "dependente"

    return None

def get_user_id(email):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT cpf_responsavel FROM cadastro_responsavel WHERE user_email = %s", (email,))
    user_id = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return user_id

def add_to_do(cpf_dependente, task_name, task_completed):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO to_do_list (cpf_dependente, task_name, task_completed) VALUES (%s, %s, %s)", (cpf_dependente, task_name, task_completed))
    connection.commit()
    cursor.close()
    connection.close()

def list_to_do(cpf_dependente):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT task_name, task_completed FROM to_do_list WHERE cpf_dependente = %s", (cpf_dependente,))
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    return tasks

def register_dependente(cpf_dependente, full_name, user_email, birthday, cellphone, password, responsavel1, responsavel2):
    connection = get_connection()
    cursor = connection.cursor()
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO cadastro_dependente (cpf_dependente, full_name, user_email, birthday, cellphone, password, responsavel1, responsavel2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (cpf_dependente, full_name, user_email, birthday, cellphone, hashed_password, responsavel1, responsavel2))
    connection.commit()
    cursor.close()
    connection.close()

def list_dependentes(cpf_responsavel):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT full_name, user_email, birthday, cellphone FROM cadastro_dependente WHERE responsavel1 = %s OR responsavel2 = %s", (cpf_responsavel, cpf_responsavel))
    dependentes = cursor.fetchall()
    cursor.close()
    connection.close()
    return dependentes
