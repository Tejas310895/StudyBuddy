import flet as ft

from flet.buttons import RoundedRectangleBorder


class TopicListObject:

    def main_appbar(self, route):
        main_app_bar = ft.AppBar(
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
        )
        return main_app_bar

    def custom_appbar(self, route, type=None):
        if type == 'chat_head':
            clickables = [
                ft.IconButton(icon=ft.icons.SEARCH,
                              icon_color=ft.colors.BLACK45, icon_size=25),
            ]
            leading_icon = ft.Container(
                ft.Image(src="/images/bio_infor.png"), padding=ft.padding.only(left=0))
            title_text = ft.Text("Bioinformatics", font_family="JosefinSans Regular",
                                 size=20, color=ft.colors.BLACK54)
            subtitle_text = ft.Text("Go for the sylabus ahead...", font_family="JosefinSans Regular",
                                    size=10, color=ft.colors.BLACK54)
        else:
            clickables = None
            leading_icon = None
            title_text = ft.Text("Add Topic", font_family="JosefinSans Regular",
                                 size=20, color=ft.colors.BLACK54)
            subtitle_text = None

        chat_app_bar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK, icon_size=25, on_click=lambda _: route.go("/")),
            leading_width=30,
            title=ft.ListTile(
                leading=leading_icon,
                title=title_text,
                subtitle=subtitle_text,
                content_padding=ft.padding.only(left=0),
                expand=True
            ), actions=clickables,
            center_title=False,
            bgcolor=ft.colors.WHITE,
        )
        return chat_app_bar

    def topic_object(self, image, title, sub_title, route):
        topic_list_bp = ft.Container(
            ft.ListTile(
                leading=ft.Container(ft.Text("B", size=25, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                     bgcolor=ft.colors.PURPLE_ACCENT_400,
                                     border_radius=50,
                                     width=50,
                                     height=50,
                                     alignment=ft.alignment.center,
                                     padding=ft.padding.only(top=8)
                                     ),
                title=ft.Text(title),
                subtitle=ft.Text(sub_title),
                on_click=lambda _: route.go("/info_block")
            ),
            bgcolor=ft.colors.WHITE,
        )
        return topic_list_bp

    def chat_object(self, q_image, question, a_image, a_name, answer):
        study_container = ft.Column([
            ft.Container(
                ft.TextButton(content=ft.Row([ft.Container(ft.Text("P", size=10, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                                           bgcolor=ft.colors.PURPLE_ACCENT_400,
                                                           border_radius=50,
                                                           width=20,
                                                           height=20,
                                                           alignment=ft.alignment.center,
                                                           padding=ft.padding.only(
                                                               top=2),
                                                           tooltip="Pankaj"),
                                              ft.Text(question,
                              font_family='JosefinSans Regular',
                              size=15)]),
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
                    leading=ft.Container(ft.Text("T", size=15, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                         bgcolor=ft.colors.PURPLE_ACCENT_400,
                                         border_radius=50,
                                         width=30,
                                         height=30,
                                         alignment=ft.alignment.center,
                                         padding=ft.padding.only(top=4),
                                         tooltip="Tejas Shirsat"
                                         ),
                    title=ft.Text(a_name,
                                  font_family='JosefinSans Regular'),
                    subtitle=ft.Column([
                        ft.Container(
                            ft.Text(
                                answer,
                                font_family='JosefinSans Regular'
                            ), bgcolor=ft.colors.ORANGE_50, padding=ft.padding.all(10), border_radius=ft.border_radius.BorderRadius(topLeft=0, topRight=15, bottomLeft=15, bottomRight=15)
                        ),
                    ]),
                ), bgcolor=ft.colors.WHITE, padding=ft.padding.only(top=0)
            )
        ], spacing=0)

        return study_container

    def chat_input_object(self, input_type):
        c_input_object = ft.Row([
            ft.TextField(
                                hint_text=input_type, expand=True, height=40, content_padding=ft.padding.only(top=5, bottom=5, left=10), text_style=ft.TextStyle(font_family='JosefinSans Regular')),
            ft.IconButton(icon=ft.icons.SEND_SHARP,
                          icon_color=ft.colors.ORANGE_ACCENT_400)
        ])
        return c_input_object

    def bottom_nav(self, route):

        def nav_routes(e):
            if e.control.selected_index == 0:
                route.go("/")
            elif e.control.selected_index == 1:
                route.go("/add_topic")

        b_navigation = ft.NavigationBar(
            bgcolor=ft.colors.ORANGE_ACCENT_100,
            selected_index=1,
            elevation=0,
            height=60,
            opacity=50,
            on_change=nav_routes,
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
            ]
        )

        return b_navigation
