import flet as ft
from login import login_page
from todotentativa2 import todo_list_page

def main(page):
    def router(route):
        if route == "/":
            page.go("/login")
        elif route == "/login":
            login_page(page)
        elif route == "/todo-list":
            todo_list_page(page)

    page.on_route_change = router
    page.go("/")

ft.app(target=main)
