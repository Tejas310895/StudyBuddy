import flet as ft
from flet.buttons import RoundedRectangleBorder
from time import sleep
import modules.build as format


def main(page: ft.Page):
    page.splash = ft.Container(ft.Image(
        src="/images/splash_loader.gif", width=200), bgcolor=ft.colors.WHITE, expand=True, alignment=ft.alignment.center)
    page.update()
    sleep(5)
    page.splash = None
    page.update()
    page.title = "Study Buddy"
    page.vertical_alignment = "center"  # page alignment
    page.horizontal_alignment = "center"  # page alignment

    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "/fonts/OpenSans-Regular.ttf",
        "Permanent Marker": "/fonts/PermanentMarker-Regular.ttf",
        "JosefinSans Regular": "/fonts/JosefinSans-Regular.ttf",
        "JosefinSans Medium": "/fonts/JosefinSans-Medium.ttf",
        "Modak Regular": "/fonts/Modak-Regular.ttf",
        "EricaOne Regular": "/fonts/EricaOne-Regular.ttf",
        "Unbounded VariableFont": "/fonts/Unbounded-VariableFont_wght.ttf",
        "Frozito": "/fonts/Frozito.ttf",
        "FredokaOne Regular": "/fonts/FredokaOne-Regular.ttf",
        "Kalam Bold": "/fonts/Kalam-Bold.ttf",
        "Kalam Light": "/fonts/Kalam-Light.ttf",
        "Kalam Regular": "/fonts/Kalam-Regular.ttf"

    }

    def explore_container():
        fornt_topic_object = format.TopicListObject()

        lv = ft.ListView(expand=True, spacing=0,
                         padding=ft.padding.all(2))

        for i in range(1, 20):
            lv.controls.append(fornt_topic_object.topic_object(
                "images/bio_infor.png", "Bioinformatics", "Sylabus wise study ahead....", page))

        return lv

    def study_container():
        study_container = format.TopicListObject()

        lv = ft.ListView(expand=True, spacing=10,
                         padding=ft.padding.all(2))

        for i in range(1, 20):
            lv.controls.append(study_container.chat_object('/images/avtar1.png', "What is Python ?", "images/avtar1.png", "Tejas Shirsat",
                               "Python is high level language it is easy to debug and the code interpret by single line so that debuging becomes faster"))

        return lv

    def nav_routes(e):
        if e.control.selected_index == 0:
            page.go("/")
        elif e.control.selected_index == 1:
            page.go("/add_topic")

    def route_change(route):
        page.views.clear()
        main_app_bar = format.TopicListObject()
        custom_app_bar = format.TopicListObject()
        bottom_bar = format.TopicListObject()
        page.views.append(
            ft.View(
                "/",
                [
                    main_app_bar.main_appbar(page),
                    explore_container(),
                    bottom_bar.bottom_nav(page)
                ],
            )
        )
        if page.route == "/info_block":
            chat_input = format.TopicListObject()
            page.views.append(
                ft.View(
                    "/info_block",
                    [
                        custom_app_bar.custom_appbar(page, 'chat_head'),
                        study_container(),
                        chat_input.chat_input_object("Enter the answer")
                    ],
                )
            )
        elif page.route == "/add_topic":
            page.views.append(
                ft.View(
                    "/add_topic",
                    [
                        custom_app_bar.custom_appbar(page),
                        ft.Column([
                            ft.TextField(label="Topic Name", hint_text="Enter unique topic name", text_style=ft.TextStyle(
                                font_family='JosefinSans Regular', size=18), content_padding=ft.padding.only(top=5, bottom=5, left=10)),
                            ft.TextField(label="Topic Description", hint_text="Enter topic Description", text_style=ft.TextStyle(
                                font_family='JosefinSans Regular', size=18), content_padding=ft.padding.only(top=5, bottom=5, left=10)),
                            ft.TextField(label="Topic Tags", hint_text="#biology,#maths,#python", text_style=ft.TextStyle(
                                font_family='JosefinSans Regular', size=18), content_padding=ft.padding.only(top=5, bottom=5, left=10)),
                            ft.ElevatedButton(
                                "Submit", color=ft.colors.WHITE, elevation=0, width=300, bgcolor=ft.colors.GREEN_ACCENT_200)
                        ]),
                        bottom_bar.bottom_nav(page)

                    ],
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view="flet_app", assets_dir="assets")
