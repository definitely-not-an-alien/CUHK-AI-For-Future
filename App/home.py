import flet as ft
import time
gp=ft.LinearGradient(
    begin=ft.alignment.top_center,
    end=ft.alignment.bottom_center,
    rotation=-45,
    colors=[ft.colors.LIGHT_BLUE_700, ft.colors.BLUE_900],
)
def ret(page):
    title = "JyutOp"
    subtitle = "Your guide to Cantonese Opera"
    hp = ft.Column(
                    width=page.width,
                    height=page.height,
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value=title,
                            size=80
                        ),
                        ft.Text(
                            value=subtitle,
                            size=30
                        )
                    ],
                    visible=True
                )
                # nav_bar.ret(page)
    hs = ft.Stack(
        
        controls=[
            ft.Container(
                # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.alignment.center,
                content=ft.Text(value="粵 樂",
                    size=300,opacity=0.2),
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=hp
            )
        ]
    )
    home_page = ft.Container(
        width=page.width,
        height=page.height-50,
        gradient=gp,
        content = hs,
        padding=0,
        margin=0,
        # animate=ft.animation.Animation(1000, "fadeOut"),
        animate_opacity=300,
        alignment=ft.alignment.center,
    )
    return home_page
