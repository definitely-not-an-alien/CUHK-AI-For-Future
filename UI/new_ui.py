import flet as ft
import explorer
import writer
import generator



def main(page: ft.Page):

    page.title = "Opera Explorer"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.EXPLORE_OUTLINED,
                selected_icon=ft.icons.EXPLORE,
                label="Explore"
            ),
            ft.NavigationDestination(
                icon=ft.icons.KEYBOARD_OUTLINED,
                selected_icon=ft.icons.KEYBOARD,
                label="Write",
            ),
            ft.NavigationDestination(
                icon=ft.icons.DRAW_OUTLINED,
                selected_icon=ft.icons.DRAW,
                label="Generate",
            ),
        ],
        #elevation=10,
        #label_behavior="ONLY_SHOW_SELECTED",
        #bgcolor="#807090",
    )
    page.add(ft.Text("Body!"))

ft.app(target=main)