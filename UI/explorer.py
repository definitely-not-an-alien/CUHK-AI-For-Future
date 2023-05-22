import flet as ft
sub_but_style = ft.ButtonStyle(
    color={
        ft.MaterialState.HOVERED: ft.colors.WHITE,
        ft.MaterialState.FOCUSED: ft.colors.BLUE,
        ft.MaterialState.DEFAULT: ft.colors.WHITE,
    },
    bgcolor={
        ft.MaterialState.HOVERED: "green",
        ft.MaterialState.FOCUSED: "green",
        ft.MaterialState.DEFAULT: "#30337530",
    },
    shape=ft.buttons.RoundedRectangleBorder(radius=4),
    elevation=1
)
def ret(page):
    def oe_search(e):
        oe_otitle.value=opera_database[oe_tb.value]['title']
        print(opera_database[oe_tb.value])
        oe_o_e_title.value=opera_database[oe_tb.value]['e_title']
        oe_o_content.value=opera_database[oe_tb.value]['Synopsis']
        page.update()
        pass
    opera_database={
        '帝女花':{'title': '帝女花', 'e_title': 'The Flower Princess', 'Synopsis': "The story unfolds as Princess Changping and Zhou Shixian are introduced to each other, participating in an arranged marriage.\nThey meet and get engaged with the blessing of their parents. Her father, the emperor, is overthrown by Li Zicheng. To save herself, the Princess hides as a nun in a monastery, but she happens to meet Zhou again. After being found by the new regime (the Qing dynasty), she follows Zhou's plan to eventually commit suicide. Zhou formulates a plan to make sure that her father is properly buried (without asking for a proper burial ceremony) while her little brother is released to safety. Zhou returns alone to negotiate with the new regime using the bargaining power vested in him by a written request from her. Once the new regime makes good on these promises, the couple return to her former home for a wedding ceremony. They take poison on their wedding night in the palace garden where they first meet."}, 
    }
    oe_title=ft.Text(
        "Opera Explorer\nExplore opera pieces",
        size=50,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER
    )
    oe_sub=ft.Text(
        "Search for an opera piece",
        size=15,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER
    )
    oe_tb=ft.TextField(
        width=page.width-100,
        label="Query",
        hint_text="Enter your search query here",
        multiline=True,
        icon=ft.icons.SEARCH,
        # on_change=on_change
    )
    oe_sb=ft.ElevatedButton(
        text="Search",
        style=sub_but_style,
        icon=ft.icons.SEARCH,
        on_click=oe_search
    )
    oe_otitle=ft.Text(
        "",
        size=30,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        selectable=True
    )
    oe_o_e_title=ft.Text(
        "",
        size=30,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        selectable=True
    )
    oe_o_content=ft.Text(
        "",
        size=15,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER,
        selectable=True,
        # scroll=ft.ScrollMode.ALWAYS
    )
    oe_page=ft.Column(
        width=page.width,
        height=page.height,
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ALWAYS,
        spacing=20,
        controls=[
            ft.Column(
                alignment = ft.MainAxisAlignment.START,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
                spacing=10,
                controls=[
                    oe_title,
                    oe_sub
                ]
            ),
            ft.Column(
                width=page.width-50,
                alignment = ft.MainAxisAlignment.START,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                spacing=10,
                scroll=ft.ScrollMode.ALWAYS,
                controls=[
                    oe_tb,
                    oe_sb
                ]
            ),
            ft.Column(
                width=page.width-100,
                alignment = ft.MainAxisAlignment.START,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
                spacing=15,
                controls=[
                    oe_otitle,
                    oe_o_e_title,
                    oe_o_content
                ]
            )
        ],
        visible=False
    )
    return oe_page
