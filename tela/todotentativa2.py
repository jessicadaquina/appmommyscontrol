from flet import Page, Text, TextField, ElevatedButton, Column, Row
import flet as ft
from auth import get_user_id
from databasetentativa2 import get_connection

def todo_list_page(page: Page):
    user_email = page.session.get("user_email")
    user_id = get_user_id(user_email)

    def add_task(e):
        task = task_field.value
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO to_do_list (user_id, task) VALUES (%s, %s)", (user_id, task))
        connection.commit()
        cursor.close()
        connection.close()
        load_tasks()
        task_field.value = ""
        page.update()

    def load_tasks():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT task FROM to_do_list WHERE user_id = %s", (user_id,))
        tasks = cursor.fetchall()
        cursor.close()
        connection.close()
        tasks_column.controls.clear()
        for task in tasks:
            tasks_column.controls.append(Text(task[0]))

    task_field = TextField()
    add_button = ElevatedButton(text="Add Task", on_click=add_task)
    tasks_column = Column()

    load_tasks()

    page.add(Row([task_field, add_button]), tasks_column)

ft.app(target=todo_list_page)
