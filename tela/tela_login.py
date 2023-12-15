from flet import *
import flet as ft
import flet_material as fm
import asyncio

PRIMARY = "white"

fm.Theme.set_theme(theme=PRIMARY)

dummy_user_list: list = [["jessica.tomino@gmail.com", 123456]]

class CustomInputfiel(UserControl):
    def __init__(self, password: bool, title: str):
        self.input: Control = TextField(
            height=45,
            border_color= "#bbbbbb",
            border_width=0.6,
            cursor_height=14,
            cursor_width=1,
            cursor_color="white",
            text_size=13,
            bgcolor= fm.Theme.primary_theme,
            password=password,
            on_focus= lambda e: self.focus_shadow(e),
            on_blur= lambda e: self.blur_shadow(e),
            on_change= lambda e: self.set_loader_animation(e)
        )
        
        self.input_box: Container = Container(
            expand=True,
            content=self.input,
            animate=Animation(300, "ease"),
            shadow=None
        )
        
        self.loader: Control = ProgressBar(
            value=0,
            bar_height=1.25,
            color='black',
            bgcolor='transparent'
        )
        
        self.status: Control = fm.CheckBox(
            shape="circle",
            value=False,
            disabled=True,
            offset= Offset(1,0),
            bottom=0,
            right=1,
            top=1,
            animate_opacity= Animation(200, "linear"),
            animate_offset= Animation(350, "ease"),
            opacity=0
        )
        
        self.object = self.create_input(title)
        
        super().__init__()
    
    def set_ok(self):
        self.loader.value = 0
        self.loader.update()
        self.status.offset = Offset(-0.5, 0)
        self.status.opacity = 1
        self.update()
        
        asyncio.sleep(1)
        
        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()
    
    def set_loader_animation(self, e):
        if len(self.input.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0
            
        self.loader.update()
     
    def blur_shadow(self, e):
        self.input_box.shadow = None
        self.input.border_color = "#bbbbbb"
        self.update()
        
    def focus_shadow(self, e):
        self.input.border_color=PRIMARY
        self.input_box.shadow = BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color= colors.with_opacity(0.25, "black"),
            offset= Offset(4,4)
        )
        self.update()
        self.set_loader_animation(e=None)        

    def create_input(self, title):
        return Column(
            spacing=5,
            controls=[
                Text(
                    title,
                    size=11,
                    weight='bold',
                    color='#bbbbbb'
                ),
                Stack(
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

class MainFormUI(UserControl):
    def __init__ (self):
        self.email = CustomInputfiel(False, "Email")
        self.password = CustomInputfiel(True, "Senha")
        self.ImagemLogin: Control = Image(
            src="tela/9480567.jpg",
            width=180,
            height=180,
            fit=ImageFit.FILL,
            border_radius=10,
            color_blend_mode="white")
        super().__init__()
        
    
        
    def build(self):
        return Container(
            width=450, height=550,
            bgcolor=colors.with_opacity(0.01, "white"),
            border_radius=10,
            padding=40,
            content= Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    Divider(height=5, color='transparent'),
                    self.ImagemLogin,
                    Text(
                        "MOMMY's CONTROL", 
                        size=21,
                        weight="w800",
                        color= colors.with_opacity(0.85, "black")),
                    Divider(height=25, color='transparent'),
                    self.email,
                    Divider(height=5, color='transparent'),
                    self.password,
                    Row(
                        width=320,
                        alignment=MainAxisAlignment.END,
                        controls=[TextButton("Esqueceu a senha?")]
                    ),
                    Divider(height=25, color='transparent'),
                    # self.submit,
                ]
            )
        )
        
class SignInButton(UserControl):
   def __init__(self, btn_name):
       self.btn_name = btn_name
       super().__init__()
       
   def build(self):
        return Container(
            content=ElevatedButton(
                content=Text(
                    self.btn_name,
                    size=13,
                    weight='bold'
                ),
                style=ButtonStyle(
                    shape={ 
                           "": RoundedRectangleBorder(radius=8)},
                    color={"": "black"},
                    bgcolor={"": "#7df6dd"}
                ),
                height=42,
                width=320,
            ),
       on_click= lambda e: asyncio.run(self.validade_entries(e))
        )
        
   async def validade_entries(self, e):
        password_value = self.password.inout.value()
        email_value = self.email.input.value
        
        for user, password in dummy_user_list:
            if email_value == user and password_value == str(password):
                await asyncio.sleep(0.5)
                await self.email.set_ok()
                await asyncio.sleep(1)
                await self.password.set_ok()
                self.update()

class RegisterInButton(UserControl):
    def __init__(self, btn_register):
        self.btn_register = btn_register
        super().__init__()
        
    def build(self):
       return Container(
           content=ElevatedButton(
               content=Text(
                   self.btn_register,
                   size=13,
                   weight='bold'
               ),
                style=ButtonStyle(
                    shape={ 
                           "": RoundedRectangleBorder(radius=8)},
                    color={"": "black"},
                    bgcolor={"": "#7df6dd"}
                ),
                height=42,
                width=320,
           )
       )
   
    
        
def main(page: Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.bgcolor = fm.Theme.primary_theme

    form = MainFormUI()
    
    page.add(
        form,
        Divider(height=5, color='transparent'),
        SignInButton("Entrar"),
        Divider(height=2, color='transparent'),
        RegisterInButton("Cadastrar")
    )
    page.update()
    
if __name__ == '__main__':
    ft.app(target=main)