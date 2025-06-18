import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def login(page: ft.Page) -> None:
    page.title = 'Entrar'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    
    #Campo de configuração
    text_username: TextField = TextField(label='Usuário', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Senha', text_align=ft.TextAlign.LEFT, width=200, password=True)
    button_submit: ElevatedButton = ElevatedButton(text='Entrar', width=200)
    page.add(ft.ElevatedButton(text='Cadastrar'))
    
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
            
        page.update()
        
    def submit(e: ControlEvent) -> None:
        print('Usuário: ', text_username.value)
        print('Senha: ', text_password.value)
        
        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Seja Bem Vindo {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
    
        page.clean()
        
        
    #Vinculando a função a interface do usuário    
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit
    button_submit1 = page.add(Row(
            controls=[
                Column([text_username, text_password,button_submit])
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ))
    
    #Pagina cadastro
    # page.add(
    #     Row(
    #         controls=[
    #             Column([text_username, text_password,button_submit])
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER
    #     )
    # )
    
    