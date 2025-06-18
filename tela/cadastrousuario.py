from flet import *
import flet as ft
import mysql.connector
    
# def deletar_cadastro(cpf):
#     comando = "DELETE FROM usuario WHERE cpf = %s"
#     val = (cpf)
#     cursor.execute(comando, val)
#     conexao.commit()
        
def TelaCadastro (page: Page):
#conexão banco de dados
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'cadastro_usuario'
    )
    
    cursor = conexao.cursor()
    
    cpf = TextField(
        label="CPF",
        max_length="11",
        input_filter=NumbersOnlyInputFilter())
    nome = TextField(label="Nome e Sobrenome", autofocus=True)
    email = TextField(label="Email")
    data_nascimento = TextField(label="Data de nascimento")
    celular = TextField(
        label="Número Celular",
        max_length="11",
        input_filter=NumbersOnlyInputFilter())
    tipo_registro = Dropdown(
        label="Defina a conta",
        options=[
            dropdown.Option("Responsável"),
            dropdown.Option("Dependente")
        ],
        autofocus=True,
    )
    
    def cadastrar_click(event):
        try:
            cadastrar_usuario(
            cursor, cpf.value, nome.value, email.value, data_nascimento.value, celular.value, tipo_registro.value)
        finally:
            cursor.close()
            conexao.close()
    
    page.add(
        cpf,
        nome,
        email,
        data_nascimento,
        celular,
        tipo_registro,
        ElevatedButton("Cadastrar", on_click= cadastrar_click)
    )
    
    # conexao.close()   
    
def cadastrar_usuario(cursor, conexao, cpf, nome, email, data_nascimento, celular, tipo_registro):
    # comando = 'INSERT INTO usuario (CPF, NomeUsuario, EmailUsuario, DataNascimento, Telefone, Registro) VALUES ("{cpf}", "{nome}", "{email}", "{data_nascimento}", "{celular}", "{tipo_registro}")'
    comando = 'INSERT INTO usuario (CPF, NomeUsuario, EmailUsuario, DataNascimento, Telefone, Registro) VALUES (%s, %s, %s, %s, %s, %s)'
    valores = (cpf, nome, email, data_nascimento, celular, tipo_registro)
    cursor.execute(comando, valores)
    conexao.commit()
    # conexao.commit() #edita banco de dados
    # resultado = cursor.fetchall() #ler banco de dados
    print("Usuário cadastrado com sucesso!")
    # cursor.close()
    
app(target=TelaCadastro)