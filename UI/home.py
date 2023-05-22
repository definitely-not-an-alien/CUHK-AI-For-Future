import flet as ft
import time
import nav_bar
def ret(page):
    title = "JyutOp"
    subtitle = "Your guide to Cantonese Opera"
    home_page = ft.Column(
                    width=page.width,
                    height=page.height,
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value=title,
                            size=60
                        ),
                        ft.Text(
                            value=subtitle,
                            size=30
                        )
                    ],
                    visible=True
                )
                # nav_bar.ret(page)
    
    return home_page
