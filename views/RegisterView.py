import flet as ft

def RegisterView(page, auth_controller):

    nombre_input = ft.TextField(label="Nombre", width=350)
    email_input = ft.TextField(label="Correo electrónico", width=350)
    pass_input = ft.TextField(label="Contraseña", password=True, width=350)

    def registrar_click(e):
        ok, msg = auth_controller.registrar_usuario(
            nombre_input.value,
            email_input.value,
            pass_input.value
        )

        if ok:
            page.snack_bar = ft.SnackBar(ft.Text(msg), bgcolor="green")
            page.go("/")  # vuelve al login
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg), bgcolor="red")

        page.snack_bar.open = True
        page.update()

    return ft.View(
        route="/registro",
        appbar=ft.AppBar(title=ft.Text("Registro de Usuario")),
        controls=[
            ft.Column(
                [
                    ft.Text("Crear Cuenta", size=24, weight="bold"),
                    nombre_input,
                    email_input,
                    pass_input,
                    ft.ElevatedButton("Registrarse", on_click=registrar_click, width=350),
                    ft.TextButton("Ya tengo cuenta", on_click=lambda _: page.go("/"))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ]
    )