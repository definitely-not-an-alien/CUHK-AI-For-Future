import flet as ft
import explorer
import writer
import generator
import home
import time
pg_list=["/home","/ex","/wr","/ge"]
def main(page: ft.Page):
    page.title = "JyutOp"
    page.route = "/home"
    h_page = home.ret(page)
    e_page = explorer.ret(page)
    w_page = writer.ret(page)
    g_page = generator.ret(page)
    screen = ft.Column(
        width=page.width,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.START,
        controls=[
            h_page,
            e_page,
            w_page,
            g_page
        ]
    )
    def resize(e):
        screen.width = page.width
        screen.height = page.height-50
        screen.update()
        h_page.height = page.height-50
        h_page.width = page.width
        h_page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        h_page.update()
        e_page.height = page.height-50
        e_page.width = page.width
        e_page.update()
        w_page.height = page.height-50
        w_page.width = page.width
        w_page.update()
        # print(h_page.width)
        g_page.height = page.height-50
        g_page.width = page.width
        g_page.update()
        screen.update()
        page.update()
    def pg_change(e):
        # print(e.control.selected_index)
        print(e_page.visible)
        h_page.opacity = 0
        g_page.opacity = 0
        w_page.opacity = 0
        e_page.opacity = 0
        screen.update()
        page.update()
        time.sleep(0.4)
        h_page.visible = True if e.control.selected_index == 0 else False
        g_page.visible = True if e.control.selected_index == 3 else False
        w_page.visible = True if e.control.selected_index == 2 else False
        e_page.visible = True if e.control.selected_index == 1 else False
        h_page.opacity = 1 if e.control.selected_index == 0 else 0
        g_page.opacity = 1 if e.control.selected_index == 3 else 0
        w_page.opacity = 1 if e.control.selected_index == 2 else 0
        e_page.opacity = 1 if e.control.selected_index == 1 else 0

        screen.update()
        # h_page.opacity = 1 if e.control.selected_index == 0 else 0
        # e_page.opacity = 1 if e.control.selected_index == 1 else 0
        # w_page.opacity = 1 if e.control.selected_index == 2 else 0
        # g_page.opacity = 1 if e.control.selected_index == 3 else 0
        time.sleep(0.3)
        page.update()
        time.sleep(0.3)
        # page.go(pg_list[e.control.selected_index])
    def route_change(route):
        if(page.route=="/home"):
            page.views.append(home.ret(page))
        pass
    page.navigation_bar = ft.NavigationBar(

        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
                label="Home",
            ),
            ft.NavigationDestination(
                icon=ft.icons.EXPLORE_OUTLINED,
                selected_icon=ft.icons.EXPLORE,
                label="Explore",
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
        elevation=10,
        label_behavior="ONLY_SHOW_SELECTED",
        bgcolor="#705080",
        on_change=pg_change
    )
    # nav_bar.ret(page)
    # page.on_route_change = route_change
    # page.add(ft.Text("Body!"))
    page.on_resize = resize
    page.add(screen)
    page.go("/home")


ft.app(target=main)