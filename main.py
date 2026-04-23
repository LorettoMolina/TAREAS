import flet as ft
from src.controllers.UserController import AuthController
from src.controllers.TareasController import TareaController
from views.LoginView import LoginView
from views.dashbooard import DashboardView

def start(page: ft.Page):

    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.controls.clear()

        if page.route == "/":
            page.controls.append(LoginView(page, auth_ctrl))

        elif page.route == "/dashboard":
            page.controls.append(DashboardView(page, task_ctrl))

        else:
            page.controls.append(ft.Text("Ruta no encontrada"))

        page.update()

    page.on_route_change = route_change

    page.go("/")
    
def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()