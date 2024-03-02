import flet as ft

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("JSK"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        
    )
    page.add(ft.Text("This is the body of the example"))

ft.app(target=main)
