import flet as ft
from auth import register_user, login_user

def main(page):
    email_field = ft.TextField()
    password_field = ft.TextField(password=True)
    error_label = ft.Text("")

    def register(e):
        email = email_field.value
        password = password_field.value
        register_user(email, password)
        page.go("/login")

    def login(e):
        email = email_field.value
        password = password_field.value
        if login_user(email, password):
            page.session.set("user_email", email)
            page.go("/todo-list")
        else:
            error_label.value = "Login failed, please try again."
            page.update()

    page.add(ft.Text("Register"))
    page.add(email_field)
    page.add(password_field)
    page.add(ft.ElevatedButton("Register", on_click=register))
    page.add(ft.Text("Login"))
    page.add(email_field)
    page.add(password_field)
    page.add(ft.ElevatedButton("Login", on_click=login))
    page.add(error_label)

ft.app(target=main)
