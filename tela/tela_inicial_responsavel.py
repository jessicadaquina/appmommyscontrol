from flet import *
import flet as ft
import flet_material as fm
import time


def main(page: ft.Page):
    page.title = "Home - Responsável"
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = fm.Theme.primary_theme

    page.add(
        ft.Text("Bem-vindo à Tela Inicial do Responsável!", size=30, weight="bold", color="black")
    )
    page.update()

                
    # # configurando a barra superior da tela inicial do responsável
    # def header_page(page):
    #     #definindo tema padrão do app
    #     # page.theme_mode="light"
        
    #     # centralizando conteúdo do corpo da tela no centro
    #     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
    #     # colocando condição para alteração de tema escuro e claro
    #     def change_theme(e):
    #         page.theme_mode="light" if page.theme_mode == "dark" else "dark"
    #         page.update()
    #         time.sleep(0.5)
                
    #     # configurando as informações da barra superior
    #     page.appbar = ft.AppBar(       
    #         # definindo botões que aparecerão ao lado esquerdo da parte superior
    #         leading= ft.PopupMenuButton(
    #             icon=ft.icons.FAMILY_RESTROOM,
    #             tooltip=("Mostrar Família"),
    #             items=[
    #                 ft.PopupMenuItem(text="Adicionar dependente"),
    #                 ft.PopupMenuItem(text="Adicionar responsável")]),
            
    #         center_title=False,
    #         leading_width=70,
    #         bgcolor=ft.colors.WHITE,
            
    #         # definindo botões que aparecerão ao lado direito da parte superior
    #         actions=[
    #             # desenvolvendo funções para alterar tema de fundo do aplicativo de claro para escuro. Configuração inicial definida como claro
    #             ft.IconButton(
    #                 icon=icons.SUNNY,
    #                 selected_icon=icons.DARK_MODE,
    #                 style=ButtonStyle(
    #                     color={"": colors.BLACK, "selected": colors.WHITE}
    #                 ),
    #                 on_click = change_theme
    #             ),
    #             ft.PopupMenuButton(
    #                 icon=ft.icons.ADD_CIRCLE,
    #                 tooltip="Adicionar integrante",
    #                 items=[
    #                     ft.PopupMenuItem(text="Adicionar dependente"),
    #                     ft.PopupMenuItem(text="Adicionar responsável")
    #                 ]
    #             )
    #         ]
    #     )
    #     page.update()

    # # configurando função para trocar de light theme para dark theme
            

        

    # # configurando corpo da tela inicial

    # # configurando a barra inferior da tela inicial do responsável
    # def footer_page(page):
    #     page.title = "MOMMY'S CONTROL"
    #     page.navigation_bar = ft.CupertinoNavigationBar(
    #         bgcolor=ft.colors.WHITE,
    #         inactive_color=ft.colors.GREY,
    #         active_color=ft.colors.RED,
    #         on_change=lambda e: print("Selecione uma opção: ", e.control.selected_index),
    #         destinations=[
    #             ft.NavigationDestination(icon=ft.icons.LOCATION_ON, label="Localização"),
    #             ft.NavigationDestination(icon=ft.icons.VIEW_LIST, label="Dia a Dia"),
    #             ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Configuração")
    #         ]
    #     )
        
    #     page.update()

    # # função de cronometro para acrescimento de tempo definindo em horas e minutos
    # def timer_picker(page):
    #     value_limited_time_ref = ft.Ref[ft.Text]()
        
    #     # realizando o alinhamento do cronômetro horizontalmente no centro e verticalmente na parte inferior da tela
    #     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #     page.vertical_alignmente = ft.MainAxisAlignment.END
        
    #     # configurando o formato de hora a ser apresentado no contador
    #     def seletec_timer_change(e):
    #         val = int(e.data)
    #         value_limited_time_ref.current.value = time.strftime("%H:%M:%S", time.gmtime(val))
    #         page.update()
        
    #     # utilizando o modelo Cupertino para Ios/Android para apresentação do relógio esteticamente
    #     selected_timer = ft.CupertinoTimerPicker(
    #         value=3600,
    #         minute_interval=5,
    #         mode=ft.CupertinoTimerPickerMode.HOUR_MINUTE,
    #         on_change=seletec_timer_change,
    #     )
        
    #     page.add(
    #         ft.Row(
    #             tight=True,
    #             controls=[
    #                 # definindo tempo de acréscimo de uso do aparelho dependente
    #                 ft.Text("Tempo a ser definido: ", size=20),
    #                 ft.TextButton(
    #                     content=ft.Text("00:05", size=20, ref=value_limited_time_ref),
    #                     style=ft.ButtonStyle(color=ft.colors.BLUE),
    #                     on_click=lambda _: page.show_bottom_sheet(
    #                         ft.CupertinoBottomSheet(
    #                             selected_timer,
    #                             height=200,
    #                             padding=ft.padding.only(top=6)
    #                         )
    #                     )
    #                 )
    #             ]
    #         )
    #     )


    # def tela(page: ft.Page):
    #     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #     page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #     page.bgcolor = fm.Theme.primary_theme
        
    #     page.add(
    #         AppBar(
    #             actions=[
    #                 Divider(height=5, color='transparent'),
    #                 header_page,
    #                 Divider(height=5, color='transparent'),
    #                 footer_page
    #             ]
    #         )
    #     )
        
    #     page.update()
        
if __name__ == '__main__':
    ft.app(target=main)