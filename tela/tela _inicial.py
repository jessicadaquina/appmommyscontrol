import flet as ft

def tela_inicial(page: ft.Page):
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        
        # extended=True,
        
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Responsáveis"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Dependentes"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Código Acesso Familiar",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Configuração"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
        
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SUPERVISED_USER_CIRCLE),
        leading_width=40,
        title=ft.Text("CONTROLE PARENTAL"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Adicionar criança"),
                    ft.PopupMenuItem(text="Adicionar Responsável"),
                    ft.PopupMenuItem(text="Acesso do familiar responsável"),
                    ft.PopupMenuItem(text="Gerenciar família"),
                ],
            ),

            ft.IconButton(ft.icons.ADD_HOME_WORK),
            ft.IconButton(ft.icons.SETTINGS_APPLICATIONS_OUTLINED),

        ],
    )
    page.add(ft.Text("Body!"))

# ft.app(target=tela_inicial)