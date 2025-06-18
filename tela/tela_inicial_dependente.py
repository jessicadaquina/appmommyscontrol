import flet as ft
import flet_material as fm

def main(page: ft.Page):
    page.title = "Home - Dependente"
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = fm.Theme.primary_theme

    page.add(
        ft.Text("Bem-vindo à Tela Inicial do Dependente!", size=30, weight="bold", color="black") )
    
    page.update()
    
if __name__ == '__main__':
    ft.app(target=main)