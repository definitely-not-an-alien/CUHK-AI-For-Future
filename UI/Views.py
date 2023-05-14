import flet as ft
import openai
openai.api_key = "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"
messages = [{"role": "system", "content": "你是一個大型語言模型，具有寫很好的粵劇劇本歌詞的能力，可以寫很好的粵劇歌詞，以歌詞為對白，請使用繁體字以及文言文，亦必須要有對仗、音韻之美。"}]
mb_def_style = ft.ButtonStyle(
    color={
        ft.MaterialState.HOVERED: ft.colors.WHITE,
        ft.MaterialState.FOCUSED: ft.colors.BLUE,
        ft.MaterialState.DEFAULT: ft.colors.BLACK,
    },
    bgcolor={
        ft.MaterialState.HOVERED: "#807095",
        ft.MaterialState.FOCUSED: "#807095",
        ft.MaterialState.DEFAULT: "#F9F9F8",
    },
    shape=ft.buttons.RoundedRectangleBorder(radius=0),
    elevation=1
)
mb_mod_style = ft.ButtonStyle(
    color={
        ft.MaterialState.HOVERED: ft.colors.WHITE,
        ft.MaterialState.FOCUSED: ft.colors.BLUE,
        ft.MaterialState.DEFAULT: ft.colors.WHITE,
    },
    bgcolor={
        ft.MaterialState.HOVERED: "#807095",
        ft.MaterialState.FOCUSED: "#807095",
        ft.MaterialState.DEFAULT: "#504278",
    },
    shape=ft.buttons.RoundedRectangleBorder(radius=0),
    elevation=0
)
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
msg_p = ""
def views_handler(page):
    def sub_prompt(e):
        global msg_p
        e.text="Loading... (This may take a while)"
        e.style=ft.ButtonStyle(
            color={
                ft.MaterialState.HOVERED: ft.colors.WHITE,
                ft.MaterialState.FOCUSED: ft.colors.WHITE,
                ft.MaterialState.DEFAULT: ft.colors.WHITE,
            },
            bgcolor={
                ft.MaterialState.HOVERED: "green",
                ft.MaterialState.FOCUSED: "green",
                ft.MaterialState.DEFAULT: "green",
            },
            shape=ft.buttons.RoundedRectangleBorder(radius=0),
            elevation=0
        )
        user_prompt = "請按以下文字寫一個粵劇劇本歌詞： {}。".format(msg_p)
        messages.append({"role": "user", "content": user_prompt})
        apireturn  = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print(apireturn['choices'][0]['message']['content'])
        oa_rt.value = apireturn['choices'][0]['message']['content']
        page.update()
        e.style=sub_but_style
        page.update()
        pass
    def on_change(e):
        global msg_p
        msg_p = e.control.value
    def oe_search(e):

        oe_otitle.value=opera_database[oe_tb.value]['title']
        print(opera_database[oe_tb.value])
        oe_o_e_title.value=opera_database[oe_tb.value]['e_title']
        oe_o_content.value=opera_database[oe_tb.value]['Synopsis']
        page.update()
        pass
    def page_ho(e):
        # global curr_page, top_buttons
        # top_buttons = men_but_temp
        page.go('/')
        # top_buttons.update()
        # page.update()
        pass
    def page_oe(e):
        page.go('/oe')
        # top_buttons.update()
        # print(curr_page)
        # page.update()
        pass
    def page_oa(e):
        page.go('/oa')
        # top_buttons = men_but_temp
        # # top_buttons.update()
        # page.update()
        pass
    def page_au(e):
        page.go('/au')
        # top_buttons.update()
        # page.update()
        pass
    top_buttons = ft.Row(
        height=20,
        width=page.width,
        controls=[
            ft.ElevatedButton(text="Home", 
            style=mb_def_style, 
            ),
            ft.ElevatedButton(text="Opera Explorer", 
            style=mb_def_style,
            ),
            ft.ElevatedButton(text="Opera AI", 
            style=mb_def_style
            ),
            ft.ElevatedButton(text="About Us", 
            style=mb_def_style
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )
    home_top = ft.Text(
        "Welcome to", 
        # bgcolor="#44444400",
        size=50,
        color="#F5F5F5",
    )
    home_bot = ft.Text(
        "Opera Explorer", 
        # bgcolor="#44444400",
        size=70,
        color="#F5F5F5",
    )
    get_start = ft.TextButton(
        text="Get started",
        style=ft.ButtonStyle(color="#F8F8F8"),
        width=200,
        on_click=page_oa
    )
    title_col = ft.Column(
        width=page.width,
        height=page.height-20,
        controls=[home_top, home_bot, get_start],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )
    oa_title = ft.Text(
        "Opera AI\nScript Writing Assistant",
        size=50,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER
    )
    oa_sub = ft.Text(
        "Enter an unfinished script or a brief prompt for a Chinese Opera script and watch the magic happen",
        size=15,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER
    )
    oa_tb = ft.TextField(
        width=page.width-100,
        label="Prompt",
        hint_text="Enter your prompt here",
        multiline=True,
        on_change=on_change
    )

    oa_sb = ft.ElevatedButton(
        text="Submit",
        style=sub_but_style,
        on_click=sub_prompt
    )
    oa_rt = ft.TextField(
        width=page.width-100,
        label="Generated Script",
        multiline=True,
        read_only=True
    )
    oa_col = ft.Column(
        width=page.width,
        controls=[
            oa_title, oa_sub
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )
    oa_sp = ft.Text("", size=30)
    oa_col2 = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        width=page.width-100,
        controls=[
            oa_tb, oa_sb, oa_rt
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        alignment=ft.MainAxisAlignment.CENTER
    )
    oa_col3 = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        width=page.width,
        controls=[oa_col, oa_sp, oa_col2],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )
    gp=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        rotation=-45,
        colors=[ft.colors.PURPLE, ft.colors.LIGHT_BLUE_700],
    )
    oa_page_cont=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            spacing=20,
            controls=[
                ft.Row(
                    height=20,
                    width=page.width,
                    scroll=ft.ScrollMode.ALWAYS,
                    controls=[
                        ft.ElevatedButton(text="Home", 
                        width=page.width/4,
                        style=mb_def_style, 
                        on_click=page_ho
                        ),
                        ft.ElevatedButton(text="Opera Explorer", 
                        width=page.width/4,
                        style=mb_def_style,
                        on_click=page_oe
                        ),
                        ft.ElevatedButton(text="Opera AI", 
                        width=page.width/4,
                        style=mb_mod_style,
                        on_click=page_oa
                        ),
                        ft.ElevatedButton(text="About Us", 
                        width=page.width/4,
                        style=mb_def_style,
                        on_click=page_au
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                oa_sp,
                oa_col3
            ]
        )
    oa_page = ft.Container(
        width=page.width,
        height=page.height,
        gradient=gp,
        content = oa_page_cont
        
    )
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
        on_change=on_change
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
        ]
    )
    return {
        '/': ft.View(
            route='/',
            bgcolor=ft.colors.PURPLE,
            vertical_alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.MainAxisAlignment.CENTER,
            scroll = ft.ScrollMode.ALWAYS,
            padding = 0,
            controls=[
                ft.Container(
                    gradient=gp,
                    # image_src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Vancouver_Cantonese_Opera_Extravaganza_22May2005_-_11_crop.jpeg",
                    width=page.width,
                    height=page.height,
                    content=
                        ft.Container(
                            bgcolor="#44444470",
                            width=page.width,
                            height=page.height,
                            blur=3,
                            content=
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            height=20,
                                            width=page.width,
                                            controls=[
                                                ft.ElevatedButton(text="Home", 
                                                width=page.width/4,
                                                style=mb_mod_style, 
                                                on_click=page_ho
                                                ),
                                                ft.ElevatedButton(text="Opera Explorer", 
                                                width=page.width/4,
                                                style=mb_def_style,
                                                on_click=page_oe
                                                ),
                                                ft.ElevatedButton(text="Opera AI", 
                                                width=page.width/4,
                                                style=mb_def_style,
                                                on_click=page_oa
                                                ),
                                                ft.ElevatedButton(text="About Us", 
                                                width=page.width/4,
                                                style=mb_def_style,
                                                on_click=page_au
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        ),
                                        title_col
                                    ]
                                )
                        )
                )
            ]
        ),
        '/oa': ft.View(
            route='/oa',
            # gradient=gp,
            bgcolor="#504278",
            vertical_alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.MainAxisAlignment.CENTER,
            scroll = ft.ScrollMode.ALWAYS,
            padding = 0,
            controls=[
                oa_page
            ]
        ),
        '/oe': ft.View(
            route='/oe',
            vertical_alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.MainAxisAlignment.CENTER,
            scroll = ft.ScrollMode.ALWAYS,
            padding = 0,
            controls=[
                ft.Container(
                    gradient=gp,
                    width=page.width,
                    # height=page.height,
                    # scroll = ft.ScrollMode.ALWAYS,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                height=20,
                                width=page.width,
                                controls=[
                                    ft.ElevatedButton(text="Home", 
                                    width=page.width/4,
                                    style=mb_def_style, 
                                    on_click=page_ho
                                    ),
                                    ft.ElevatedButton(text="Opera Explorer", 
                                    width=page.width/4,
                                    style=mb_mod_style,
                                    on_click=page_oe
                                    ),
                                    ft.ElevatedButton(text="Opera AI", 
                                    width=page.width/4,
                                    style=mb_def_style,
                                    on_click=page_oa
                                    ),
                                    ft.ElevatedButton(text="About Us", 
                                    width=page.width/4,
                                    style=mb_def_style,
                                    on_click=page_au
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            ),
                            oe_page
                        ]
                    )
                )
            ]
        ),
        '/au': ft.View(
            route='/au',
            vertical_alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.MainAxisAlignment.CENTER,
            scroll = ft.ScrollMode.ALWAYS,
            padding = 0,
            controls=[
                ft.Container(
                    gradient=gp,
                    width=page.width,
                    height=page.height,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                height=20,
                                width=page.width,
                                controls=[
                                    ft.ElevatedButton(text="Home", 
                                    width=page.width/4,
                                    style=mb_def_style, 
                                    on_click=page_ho
                                    ),
                                    ft.ElevatedButton(text="Opera Explorer", 
                                    width=page.width/4,
                                    style=mb_def_style,
                                    on_click=page_oe
                                    ),
                                    ft.ElevatedButton(text="Opera AI", 
                                    width=page.width/4,
                                    style=mb_def_style,
                                    on_click=page_oa
                                    ),
                                    ft.ElevatedButton(text="About Us", 
                                    width=page.width/4,
                                    style=mb_mod_style,
                                    on_click=page_au
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,

                            ),
                            
                        ]
                    )
                )
            ]
        )
    }
