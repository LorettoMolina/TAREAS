import flet as ft
from src.controllers.UserController import AuthController
from src.controllers.TareaController import TareaController
from src.views.LoginView import LoginView
from src.views.Dashboard import DashboardView

def main(page: ft.Page):
    # Instanciamos los controladores una sola vez
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
       
       # Caso de seguridad: si algo falla, mostrar texto de error
        if not page.views:
           page.views.append(
               ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacía")])
           )

        page.update()

    page.on_route_change = route_change
    # Forzamos la navegación inicial
    page.go("/")


def main():
    # Ejecución de la app
    ft.app(target=start)


if __name__ == "__main__":
    main()