from flet import *
import flet as ft
import flet_material as fm
import mysql.connector

PRIMARY = "white"
fm.Theme.set_theme(theme=PRIMARY)

#conexão banco de dados
conexao = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '',
database = 'mommy.to_do_list'
)

# cursor = conexao.cursor()

def Task(page: Page):
    page.title = "   MOMMY'S CONTROL   "
    page.scroll= "auto"
    page.padding = 15
    page.spacing = 0
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.bgcolor = fm.Theme.primary_theme
    
    
    def cpf(e):
        cursor = conexao.cursor()
        cursor.execute("SELECT cpf_dependente FROM mommy.cadastro_dependente WHERE 34142232878 in (responsavel1, responsavel2)")
        conexao.commit()
        print("Dependente localizado")
        page.update()
        
    # # vinculando cpf do responsável que irá acrescentar as tarefas em questão
    # responsible_user = ElevatedButton((responsavel))
    
    # vinculando cpf do dependente que receberá as tarefas em questão
    dependent_user = CircleAvatar(foreground_image_src=((cpf)), radius=70)
    
    #criando espaço aonde irão ser descritas as tarefas
    new_task = TextField(hint_text="Que tarefa deseja acrescentar?", expand=True)

    # def responsavel(e):
    #     try:
    #         cursor = conexao.cursor()
    #         cursor.execute("FROM mommy.cadastro_depente WHERE responsavel1 SELECT responsavel FROM mommy.to_do_list")
    #         conexao.commit()
    #         print("Responsável 1 localizado")
    #         page.update()
            
    #     except:
    #         cursor = conexao.cursor()
    #         cursor.execute("FROM mommy.cadastro_depente WHERE responsavel2 SELECT responsavel FROM mommy.to_do_list")
    #         conexao.commit()
    #         print("Responsável 2 localizado")
    #         page.update()       


    def mostrar_tarefa(e):
        input.offset = transform.Offset(0,0)
        page.update()
        
    def salvar(e):
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO mommy.to_do_list (task_named) VALUES (?)", (new_task))
            conexao.commit()
            print("Tarefa adicionada")
        
            input.offset = transform.Offset(2,0)
            
            page.snack_bar = SnackBar(
                Text("Adicionado"),
                bgcolor="green"
            )
            
            page.snack_bar.open= True
            
        except Exception as e:
            print(e)

    def deletar(e):
        try:
            myid = int(e.control.data)
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM mommy.to_do_list WHERE (task_named) VALUES (?)", (new_task))
            conexao.commit()
            print("Tarefa apagada")
            page.update()
            
        except Exception as e:
            print(e)
            
    def alterar_e_salvar(e):       
            myid = new_task.value     
            cursor = conexao.cursor()
            cursor.execute("UPDATE mommy.to_do_list SET (task_named) VALUES (?)", (new_task))
            conexao.commit()
            print("Tarefa editada")
            page.update()

    page.add(
        Container(
            width=550, height=450,
            bgcolor=colors.with_opacity(0.01, "white"),
            border_radius=10,
            padding=0,
            content= Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    Divider(height=5, color='transparent'),
                    dependent_user,
                    Divider(height=15, color='transparent'),
                    Row(
                        controls=[
                            new_task,
                            FloatingActionButton(icon=icons.ADD, on_click=salvar)])
                    ])
        )
    )

    # page.add(
    #     Column(
    #         controls=[
    #             Row(
    #                 controls=[
    #                     dependent_user,
    #                     Divider(height=5, color='transparent'),
    #                     new_task,
    #                     FloatingActionButton(icon=icons.ADD, on_click=salvar)]
    #             )
    #         ]
    #     )
    # )

# class Task(ft.Row):
#     def __init__(self, task_name, task_status_change, task_delete):
#         super().__init__()
#         self.completed = False
#         self.task_name = task_name
#         self.task_status_change = task_status_change
#         self.task_delete = task_delete
        
#     def build(self):
#         self.display_task = Checkbox(
#             value=False,
#             label=self.task_name,
#             on_change=self.task_status_change
#         )
#         self.edit_name = TextField(expand=1)
        
#         self.display_view = Row(
#             alignment=MainAxisAlignment.SPACE_BETWEEN,
#             vertical_alignment=CrossAxisAlignment.CENTER,
#             controls=[
#                 self.display_task,
#                 Row(
#                     spacing=0,
#                     controls=[
#                         IconButton(
#                             icon=icons.CREATE_OUTLINED,
#                             tooltip="Editar",
#                             on_click=self.edit_clicked
#                         ),
#                         IconButton(
#                             icons.DELETE_OUTLINE,
#                             tooltip="Apagar",
#                             on_click=self.delete_clicked,
#                             icon_color=colors.RED
#                         )
#                     ]
#                 )
#             ]
#         )
        
#         self.edit_view = Row(
#             visible=False,
#             alignment=MainAxisAlignment.SPACE_BETWEEN,
#             vertical_alignment=CrossAxisAlignment.CENTER,
#             controls=[
#                 self.edit_name,
#                 IconButton(
#                     icon=icons.DONE_OUTLINE_OUTLINED,
#                     icon_color=colors.GREEN,
#                     tooltip="Atualizar",
#                     on_click=self.save_clicked
#                 )
#             ]
#         )
        
#         return Column(controls=[self.display_view, self.edit_view])
        
#     async def edit_clicked(self, e):
#         self.edit_name.value = self.display_task.label
#         self.display_view.visible = False
#         self.edit_view.visible = True
#         await self.update_async()
        
#     async def save_clicked(self, e):
#         self.display_task.label = self.edit_name.value
#         self.display_view.visible = True
#         self.edit_view.visible = False
#         await self.update_async()
        
#     async def status_change(self, e):
#         self.completed = self.display_task.value
#         await self.task_status_change(self)
        
#     async def delete_clicked (self, e):
#         await self.task_delete(self)

# class ToDoList(UserControl):    
#     #conexão banco de dados
#     conexao = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'mommy'
#     )

#     cursor = conexao.cursor()
    
#     def build(self):
#         self.new_task = TextField(hint_text="Que tarefa deseja acrescentar?", expand=True)

#         self.tasks = Column()
        
#         self.filter = Tabs(
#             scrollable=False,
#             selected_index=0,
#             on_change= self.tabs_changed,
#             tabs=[Tab(text="Tudo"),
#                   Tab(text="Falta concluir"),
#                   Tab(text="Concluído")]
#         )
        
#         self.items_left = ft.Text("0 itens já concluídos")
    
#         return Column(
#             controls=[
#                 Row(
#                     controls=[
#                         self.new_task,
#                         FloatingActionButton(icon=icons.ADD,
#                         on_click=self.add_clicked)
#                     ]
#                 ),
#                 Column(
#                     spacing=25,
#                     controls=[
#                         self.filter,
#                         self.tasks,
#                         Row(
#                             alignment=MainAxisAlignment.SPACE_BETWEEN,
#                             vertical_alignment=CrossAxisAlignment.CENTER,
#                             controls=[
#                                 self.items_left,
#                                 OutlinedButton(
#                                     text="Limpar itens concluídos",
#                                     on_click=self.clear_clicked
#                                 )
#                             ]
#                         )
#                     ]
#                 )
#             ]
#         )
        
#     async def add_clicked(self, e, cursor, conexao):
#         comando = "INSERT INTO mommy.to_do_list (task_named) VALUE (%s)"
#         valor = (self.new_task)
#         cursor.execute(comando, valor)
#         conexao.commit()
        
#         if self.new_task.value:
#             task = Task(self.new_task.value, self.task_status_change, self.task_delete)
#             self.tasks.controls.append(task)
#             self.new_task.value = ""
#             await self.new_task.focus_async()
#             await self.update_async()
        
#     async def task_status_change(self, cursor, conexao):
#         comando = "UPDATE mommy.to_do_list SET task_named = $s"
#         val = (self.new_task)
#         cursor.execute(comando, val)
#         conexao.commit()
#         await self.update_async()
        
#     async def task_delete(self, task, cursor, conexao):
#         self.tasks.controls.remove(task)
#         comando = "DELETE FROM mommy.to_do_list WHERE task_named = %s"
#         val = (task)
#         cursor.execute(comando, val)
#         conexao.commit()
#         await self.update_async()
        
#     async def tabs_changed(self, e):
#         await self.update_async()
        
#     async def clear_clicked(self, e):
#         for task in self.tasks.controls[:]:
#             if task.completed:
#                 await self.task_delete(task)
                
#     async def update(self):
#         status = self.filter.tabs[self.filter.selected_index].text
#         count = 0
#         for task in self.tasks.controls:
#             task.visible = (
#                 status == "Tudo"
#                 or (status == "Falta concluir" and not task.completed)
#                 or (status == "Concluído" and task.completed)
#             )
#             if not task.completed:
#                 count += 1
#         self.items_left.value = f"{count} itens já concluídos"
#         await super().update_async()
            
# async def ToDoListManager (page: Page):
#     page.title = "MOMMY's CONTROL"
#     page.horizontal_alignment = CrossAxisAlignment.CENTER
#     page.scroll = ScrollMode.ADAPTIVE
    
#     page.add(ToDoList())
    
        
app(target=Task)
        