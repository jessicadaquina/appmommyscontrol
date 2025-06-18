from flet import *
import flet as ft
import mysql.connector

#conexão banco de dados
conexao = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '',
database = 'mommy'
)

cursor = conexao.cursor()
   
class Task(UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
        
    def build(self):
        self.display_task = Checkbox(
            value=False,
            label=self.task_name,
            on_change=self.task_status_change
        )
        self.edit_name = TextField(expand=1)
        
        self.display_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Editar",
                            on_click=self.edit_clicked
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Apagar",
                            on_click=self.delete_clicked,
                            icon_color=colors.RED
                        )
                    ]
                )
            ]
        )
        
        self.edit_view = Row(
            visible=False,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Atualizar",
                    on_click=self.save_clicked
                )
            ]
        )
        
        return Column(controls=[self.display_view, self.edit_view])
        
    async def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        await self.update_async()
        
    async def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        await self.update_async()
        
    async def status_change(self, e):
        self.completed = self.display_task.value
        await self.task_status_change(self)
        
    async def delete_clicked (self, e):
        await self.task_delete(self)

class ToDoList(UserControl):    
    def build(self):
        self.new_task = TextField(hint_text="Que tarefa deseja acrescentar?", expand=True)

        self.tasks = Column()
        
        self.filter = Tabs(
            scrollable=False,
            selected_index=0,
            on_change= self.tabs_changed,
            tabs=[Tab(text="Tudo"),
                  Tab(text="Falta concluir"),
                  Tab(text="Concluído")]
        )
        
        self.items_left = ft.Text("0 itens já concluídos")
    
        return Column(
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD,
                        on_click=self.add_clicked)
                    ]
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Limpar itens concluídos",
                                    on_click=self.clear_clicked
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        
    async def add_clicked(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            await self.new_task.focus_async()
            await self.update_async()
        
    async def task_status_change(self, task):
        await self.update_async()
        
    async def task_delete(self, task):
        self.tasks.controls.remove(task)
        await self.update_async()
        
    async def tabs_changed(self, e):
        await self.update_async()
        
    async def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                await self.task_delete(task)
                
    async def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "Tudo"
                or (status == "Falta concluir" and not task.completed)
                or (status == "Concluído" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} itens já concluídos"
        await super().update_async()
            
async def ToDoListManager (page: Page):
    page.title = "MOMMY's CONTROL"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = ScrollMode.ADAPTIVE
    
    await page.add_async(ToDoList())
    
    # ToDoListManager = ToDoList()
    # page.add(ToDoListManager)
    
        
app(target=ToDoListManager)
        