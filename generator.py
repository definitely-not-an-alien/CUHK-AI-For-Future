import flet as ft
import random
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
    def on_change_1(e):
        cond_num.value = "Cond Scale: " + str(cond_scale.value)
        inf_num.value = "Inf Scale: " + str(inf_scale.value)
        mask_num.value = "Mask Rate: " + str(round(mask_rate.value, 2))
        cond_num.update()
        inf_num.update()
        mask_num.update()
        gpe.update()
        page.update()
        pass
    def sub_prompt(e):
        __src = "1/" + str(random.randint(1, 4)) + "/" + str(random.randint(1, 5)) + ".png"
        print(__src)
        image_out=ft.Image(
            src=__src
        )
        # image_out.image_src=f"/1/1/1.png"
        image_out.update()
        right_col.update()
        gr.update()
        gr2.update()
        gpe.update()
        page.update()
        pass
    cond_scale = ft.Slider(min=0, max=10, divisions=10, on_change=on_change_1)
    inf_scale = ft.Slider(value=18, min=0, max=24, divisions=24, on_change=on_change_1)
    mask_rate = ft.Slider(value=0.32, min=0.10, max=0.70, divisions=30, on_change=on_change_1)
    g_tb = ft.TextField(
        # width=page.width-100,
        # label="User Prompt",
        multiline=True,
        # read_only=True
    )
    cond_num = ft.Text("Cond Scale: 0.0")
    inf_num = ft.Text("Inf Scale: 18.0")
    mask_num = ft.Text("Mask Rate: 0.32")
    left_col = ft.Column(
        spacing=10,
        controls=[
            ft.Text("Prompt: "),
            g_tb,
            cond_num,
            cond_scale,
            inf_num,
            inf_scale,
            mask_num,
            mask_rate
        ]
    )
    image_out = ft.Image(
        height=256,
        width=256,
        # border=ft.border.all(1, ft.colors.BLACK),
        src=f"1/1/1.png"
    )
    g_b = ft.ElevatedButton(
        text="Submit",
        style=sub_but_style,
        on_click=sub_prompt
    )
    right_col = ft.Column(
        controls=[
            ft.Text("Output: "),
            image_out,
            g_b
        ]
    )
    g_title=ft.Text(
        "Costume Designer",
        size=50,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER
    )
    g_sub=ft.Text(
        "Get a mask / make-up design tailored to your prompt",
        size=15,
        color=ft.colors.WHITE,
        text_align=ft.TextAlign.CENTER
    )
    g_sp = ft.Text("", size=30)
    gr = ft.Row(
        width=page.width,
        height=page.height-50,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
        controls=[left_col, right_col]
    )
    gr2 = ft.Column(
        width=page.width,
        height=page.height-50,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ALWAYS,
        spacing=20,
        controls=[
            g_sp,
            g_title,
            g_sub,
            gr,
            g_sp,
        ]
    )
    gp=ft.LinearGradient(
        begin=ft.alignment.top_center,
        end=ft.alignment.bottom_center,
        rotation=-45,
        colors=[ft.colors.PURPLE, ft.colors.LIGHT_BLUE_700],
    )
    gpe = ft.Container(
        width=page.width,
        height=page.height-50,
        gradient=gp,
        content=gr2,
        # animate=ft.animation.Animation(1000, "fadeOut"),
        animate_opacity=300,
    )
    return gpe
# 1/4/5.png