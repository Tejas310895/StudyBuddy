import flet as ft

from flet.buttons import RoundedRectangleBorder


def main(page: ft.Page):
    page.title = "Routes Example"
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
        explore_container = ft.Container(
            ft.ListTile(
                leading=ft.Image(
                    src="images/bio_infor.png", border_radius=50),
                title=ft.Text("Bioinformatics"),
                subtitle=ft.Text(
                    "Sylabus wise study ahead...."
                ),
            ),
            bgcolor=ft.colors.WHITE,
            on_click=lambda _: page.go("/info_block")
        )

        lv = ft.ListView(expand=True, spacing=0,
                         padding=ft.padding.all(2))

        for i in range(1, 20):
            lv.controls.append(explore_container)

        return lv

    def study_container():
        study_container = ft.Column([
            ft.Container(
                ft.TextButton(content=ft.Row([ft.Image(src='/images/avtar1.png', width=20, height=20), ft.Text("What is Python ?",
                              font_family='JosefinSans Regular', size=15)]),
                              style=ft.ButtonStyle(
                                  shape=RoundedRectangleBorder(
                                      radius=ft.border_radius.BorderRadius(
                                          topLeft=15,
                                          topRight=15,
                                          bottomLeft=0,
                                          bottomRight=0)
                                  ), elevation=0,
                                  bgcolor=ft.colors.PURPLE_50)), padding=ft.padding.only(bottom=0)
            ),
            ft.Container(
                ft.ListTile(
                    leading=ft.Image(
                        src="images/avtar1.png", border_radius=50, width=35, height=35),
                    title=ft.Text("Tejas Shirsat",
                                  font_family='JosefinSans Regular'),
                    subtitle=ft.Column([
                        ft.Container(
                            ft.Text(
                                "Python is high level language it is easy to debug and the code interpret by single line so that debuging becomes faster",
                                font_family='JosefinSans Regular'
                            ), bgcolor=ft.colors.ORANGE_50, padding=ft.padding.all(10), border_radius=ft.border_radius.BorderRadius(topLeft=0, topRight=15, bottomLeft=15, bottomRight=15)
                        ),
                    ]),
                ), bgcolor=ft.colors.WHITE, padding=ft.padding.only(top=0)
            )
        ], spacing=0)

        lv = ft.ListView(expand=True, spacing=10,
                         padding=ft.padding.all(2))

        for i in range(1, 20):
            lv.controls.append(study_container)

        return lv

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        leading=ft.Container(ft.Image(src="/images/logo.png"),
                                             padding=ft.padding.only(left=10)),
                        leading_width=40,
                        title=ft.Text("Study-Buddy", font_family="Frozito",
                                      size=20, color=ft.colors.ORANGE_ACCENT_200),
                        center_title=True,
                        bgcolor=ft.colors.WHITE,
                        actions=[
                            ft.IconButton(icon=ft.icons.SEARCH,
                                          icon_color=ft.colors.ORANGE_400, icon_size=25),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(content=ft.Text(
                                        "Profile", font_family='JosefinSans Regular', size=15)),
                                    ft.PopupMenuItem(content=ft.Text(
                                        "Logout", font_family='JosefinSans Regular', size=15)),
                                ]
                            )
                        ],
                    ),
                    explore_container(),
                    ft.NavigationBar(
                        bgcolor=ft.colors.ORANGE_ACCENT_100,
                        elevation=0,
                        height=60,
                        opacity=50,
                        destinations=[
                            ft.NavigationDestination(
                                icon=ft.icons.EXPLORE_OUTLINED,
                                selected_icon=ft.icons.EXPLORE,
                                label="Explore",
                            ),
                            ft.NavigationDestination(
                                icon=ft.icons.BOOKMARK_ADD_OUTLINED,
                                selected_icon=ft.icons.BOOKMARK_ADD,
                                label="New Topic",
                            ),
                            ft.NavigationDestination(
                                icon=ft.icons.BOOK_OUTLINED,
                                selected_icon=ft.icons.BOOK,
                                label="New Book",
                            ),
                        ]
                    )
                ],
            )
        )
        if page.route == "/info_block":
            page.views.append(
                ft.View(
                    "/info_block",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(
                                icon=ft.icons.ARROW_BACK, icon_size=25, on_click=lambda _: page.go("/")),
                            leading_width=30,
                            title=ft.ListTile(
                                leading=ft.Container(
                                    ft.Image(src="/images/bio_infor.png"), padding=ft.padding.only(left=0)),
                                title=ft.Text("Bioinformatics", font_family="JosefinSans Regular",
                                              size=20, color=ft.colors.BLACK54),
                                subtitle=ft.Text("Go for the sylabus ahead...", font_family="JosefinSans Regular",
                                                 size=10, color=ft.colors.BLACK54),
                                content_padding=ft.padding.only(left=0),
                                expand=True
                            ),
                            center_title=False,
                            bgcolor=ft.colors.WHITE,
                        ),
                        study_container(),
                        ft.Row([
                            ft.TextField(
                                hint_text="Enter the answer", expand=True, height=40, content_padding=ft.padding.only(top=5, bottom=5, left=10), text_style=ft.TextStyle(font_family='JosefinSans Regular')),
                            ft.IconButton(icon=ft.icons.SEND_SHARP,
                                          icon_color=ft.colors.ORANGE_ACCENT_400)
                        ])
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
