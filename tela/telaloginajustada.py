import flet as ft
import flet_material as fm
import asyncio
from auth import register_user, login_user
import tela_inicial_responsavel
import tela_inicial_dependente

# Definindo a cor padrão de plano de fundo do aplicativo
PRIMARY = "white"
fm.Theme.set_theme(theme=PRIMARY)

# classe personalizada para o campo de entrada
class CustomInputField(ft.UserControl):
    def __init__(self, password: bool, title: str):
        super().__init__()
        self.input = ft.TextField(
            height=45,
            border_color="#bbbbbb",
            border_width=0.6,
            cursor_height=14,
            cursor_width=1,
            cursor_color="white",
            text_size=13,
            bgcolor=fm.Theme.primary_theme,
            password=password,
            on_focus=self.focus_shadow,
            on_blur=self.blur_shadow,
            on_change=self.set_loader_animation
        )
        
        self.input_box = ft.Container(
            expand=True,
            content=self.input,
            animate=ft.Animation(300, "ease"),
            shadow=None
        )
        
        self.loader = ft.ProgressBar(
            value=0,
            bar_height=1.25,
            color='black',
            bgcolor='transparent'
        )
        
        self.status = fm.CheckBox(
            shape="circle",
            value=False,
            disabled=True,
            offset=ft.Offset(1, 0),
            bottom=0,
            right=1,
            top=1,
            animate_opacity=ft.Animation(200, "linear"),
            animate_offset=ft.Animation(350, "ease"),
            opacity=0
        )
        
        self.object = self.create_input(title)
    
    def set_ok(self):
        # define o status como ok e atualiza os componentes
        self.loader.value = 0
        self.loader.update()
        self.status.offset = ft.Offset(-0.5, 0)
        self.status.opacity = 1
        self.update()
        
        asyncio.sleep(1)
        
        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()
    
    def set_loader_animation(self, e):
        # define a animação do carregador com base no valor do campo de entrada
        if len(self.input.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0
        self.loader.update()
     
    def blur_shadow(self, e):
        # remove a sombra do campo de entrada ao perder o foco
        self.input_box.shadow = None
        self.input.border_color = "#bbbbbb"
        self.update()
        
    def focus_shadow(self, e):
        # adiciona uma sombra ao campo de entrada ao ganhar foco
        self.input.border_color = PRIMARY
        self.input_box.shadow = ft.BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(4, 4)
        )
        self.update()
        self.set_loader_animation(None)
        
    def create_input(self, title):
        # cria o componente de entrada completo com título, campo de entrada e loader
        return ft.Column(
            spacing=5,
            controls=[
                ft.Text(
                    title,
                    size=11,
                    weight='bold',
                    color='#bbbbbb'
                ),
                ft.Stack(
                    controls=[
                        self.input_box,
                        self.status
                    ]
                ),
                self.loader,
            ]
        )
        
    def build(self):
        return self.object

# classe para o formulário de login principal
class MainFormUI(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.email = ft.TextField(label="Email")
        self.password = ft.TextField(label="Senha", password=True, can_reveal_password=True)
        self.ImagemLogin = ft.Image(
            src="tela/9480567.jpg",
            width=180,
            height=180,
            fit=ft.ImageFit.FILL,
            border_radius=10,
            color_blend_mode="white"
        )
        
    def build(self):
        return ft.Container(
            width=450, height=550,
            bgcolor=ft.colors.with_opacity(0.01, "white"),
            border_radius=10,
            padding=0,
            content=ft.Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    ft.Divider(height=5, color='transparent'),
                    self.ImagemLogin,
                    ft.Text(
                        "MOMMY's CONTROL", 
                        size=21,
                        weight="w800",
                        color=ft.colors.with_opacity(0.85, "black")
                    ),
                    ft.Divider(height=25, color='transparent'),
                    self.email,
                    ft.Divider(height=5, color='transparent'),
                    self.password,
                    ft.Row(
                        width=320,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[ft.TextButton("Esqueceu a senha?")]
                    ),
                    ft.Divider(height=25, color='transparent'),
                ]
            )
        )

# classe para entrada 
class SignInButton(ft.UserControl):
    def __init__(self, btn_name):
        super().__init__()
        self.password = CustomInputField(True, "Senha")
        self.email = CustomInputField(False, "Email")
        self.btn_name = btn_name
       
    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(
                    self.btn_name,
                    size=13,
                    weight='bold'
                ),
                style=ft.ButtonStyle(
                    shape={"": ft.RoundedRectangleBorder(radius=8)},
                    color={"": "black"},
                    bgcolor={"": "#7df6dd"}
                ),
                height=42,
                width=320,
                on_click=lambda e: asyncio.run(self.validate_entries(e))
            )
        )
        
    async def validate_entries(self, e):
        password_value = self.password.input.value
        email_value = self.email.input.value
        
        user_type = login_user(email_value, password_value)
        if user_type == "responsavel":
            await asyncio.sleep(0.5)
            await self.email.set_ok()
            await asyncio.sleep(1)
            await self.password.set_ok()
            self.page.go("/tela_inicial_responsavel")
            self.update()
        elif user_type == "dependente":
            await asyncio.sleep(0.5)
            await self.email.set_ok()
            await asyncio.sleep(1)
            await self.password.set_ok()
            self.page.go("/tela_inicial_dependente")
            self.update()
        else:
            self.email.input.value = ""
            self.password.input.value = ""
            self.email.update()
            self.password.update()

class RegisterInButton(ft.UserControl):
    def __init__(self, btn_register):
        super().__init__()
        self.btn_register = btn_register
        
    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(
                    self.btn_register,
                    size=13,
                    weight='bold'
                ),
                style=ft.ButtonStyle(
                    shape={"": ft.RoundedRectangleBorder(radius=8)},
                    color={"": "black"},
                    bgcolor={"": "#7df6dd"}
                ),
                height=42,
                width=320,
            )
        )

# tela de login do aplicativo
def tela_login(page: ft.Page):
    page.title = "MOMMY'S CONTROL"
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = fm.Theme.primary_theme

# criação do formulario de login
    form = MainFormUI()
    
    page.add(
        form,
        ft.Divider(height=5, color='transparent'),
        SignInButton("Entrar"),
        ft.Divider(height=10, color='transparent'),
    )
    page.update()

if __name__ == '__main__':
    ft.app(
        target=tela_login,
#       routes={
#           "/tela_inicial_responsavel": tela_inicial_responsavel.main,
            # "/tela_inicial_dependente": tela_inicial_dependente.main
        # }
    )
