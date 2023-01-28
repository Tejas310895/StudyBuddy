import flet as ft
import random
import string
import operator
from functools import reduce
from better_profanity import profanity
import enchant
import re
from PyPDF2 import PdfReader
import re
import os
import nltk
from nltk.corpus import stopwords
from assets.lists import phrases


class TopicListObject():
    def __init__(self, route):
        self.route = route

    def main_appbar(self, route):

        def user_logout(e):
            route.client_storage.clear()
            route.go("/user_login")

        main_app_bar = ft.AppBar(
            leading=ft.Container(ft.Image(src="/images/logo.png"),
                                 padding=ft.padding.only(left=10)),
            leading_width=40,
            title=ft.Text(f"Study-Buddy", font_family="Frozito",
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
                            "Logout", font_family='JosefinSans Regular', size=15), on_click=user_logout),
                    ]
                )
            ],
        )
        return main_app_bar

    def top_back(self, e):
        self.route.client_storage.remove("top_id")
        self.route.client_storage.remove("chat_type")
        self.route.go("/")

    def custom_appbar(self, route, type=None, topic_hex=None, topic_title=None, topic_subtitle=None):
        if type == 'chat_head':
            clickables = [
                ft.IconButton(icon=ft.icons.SEARCH,
                              icon_color=ft.colors.BLACK45, icon_size=25),
            ]
            leading_icon = ft.Container(ft.Text(topic_title[0], size=25, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                        bgcolor=f"{topic_hex}",
                                        border_radius=50,
                                        width=50,
                                        height=50,
                                        alignment=ft.alignment.center,
                                        padding=ft.padding.only(top=8)
                                        )
            title_text = ft.Text(topic_title, font_family="JosefinSans Regular",
                                 size=20, color=ft.colors.BLACK54)
            subtitle_text = ft.Text(topic_subtitle, font_family="JosefinSans Regular",
                                    size=15, color=ft.colors.BLACK54, max_lines=1)

        else:
            clickables = None
            leading_icon = None
            title_text = ft.Text(topic_title, font_family="JosefinSans Regular",
                                 size=20, color=ft.colors.BLACK54)
            subtitle_text = None

        chat_app_bar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK, icon_size=25, on_click=self.top_back),
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

    def open_topic(self, e):
        self.route.client_storage.set("top_id", e.control.data)
        self.route.go("/info_block")
        self.route.update()

    def topic_object(self, title, sub_title, icon_hex, topic_id, route):
        topic_list_bp = ft.Container(
            ft.ListTile(
                leading=ft.Container(ft.Text(sub_title[0], size=25, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                     bgcolor=f"{icon_hex}",
                                     border_radius=50,
                                     width=50,
                                     height=50,
                                     alignment=ft.alignment.center,
                                     padding=ft.padding.only(top=8)
                                     ),
                title=ft.Text(title),
                subtitle=ft.Text(f"Author of topic : {sub_title}"),
                on_click=self.open_topic,
                data=topic_id
            ),
            bgcolor=ft.colors.WHITE,
        )
        return topic_list_bp

    def bottom_nav(self, route):

        def nav_routes(e):
            if e.control.selected_index == 0:
                route.go("/")
            elif e.control.selected_index == 1:
                route.go("/add_topic")
            elif e.control.selected_index == 2:
                route.go("/library")

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
                ft.NavigationDestination(
                    icon=ft.icons.LIBRARY_BOOKS_OUTLINED,
                    selected_icon=ft.icons.LIBRARY_BOOKS,
                    label="Library",
                )
            ]
        )

        return b_navigation

    def get_hex_colors(self):
        random_number = random.randint(0, 16777215)
        hex_number = str(hex(random_number))
        hex_number = '#' + hex_number[2:]
        return hex_number

    def get_random_token(self, N):
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=N))
        return str(res)

    def censor_check(self, text):
        per_text = text
        d = enchant.Dict("en_US")

        def check(word):
            eng = ''
            try:
                eng = d.check(word)
            except Exception:
                pass
            except:
                pass
            # if word.isalnum() == True:
            #     eng = True
            if profanity.contains_profanity(word) == False:
                cenc = True
            else:
                cenc = False
            return [eng, cenc]
        text = text.split()
        text = [re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in text]
        text = list(map(check, text))
        if len(text) > 0:
            text = reduce(operator.concat, text)
        if per_text.capitalize() in phrases.Prases:
            text.append(False)
        if False in text:
            return 'bad'
        else:
            return 'good'

    def search_book(self, question):
        def check_noun(text):
            ans = nltk.pos_tag([text])
            # ans returns a list of tuple
            val = ans[0][1]
            # checking if it is a noun or not
            if (val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
                return True
            else:
                return False

        q_list = question.split()
        actual_list = list(filter(check_noun, q_list))

        path = "C:/Users/admin/OneDrive/Desktop/edu_buddy/assets/books"
        dir_list = os.listdir(path)
        topic_pages = []
        for file in dir_list:
            # Enter code here
            String = actual_list
            file_name = f"/{file}"
            reader = PdfReader(
                r"C:\Users\admin\OneDrive\Desktop\edu_buddy\assets\books"+file_name)
            number_of_pages = len(reader.pages)
            page_count = 0
            for i in String:
                for j in range(0, number_of_pages):
                    page = reader.pages[j]
                    page_text = page.extract_text()
                    ResSearch = re.search(i, page_text)
                    if ResSearch != None:
                        topic_pages.append(file)
                        page_count += 1
                    if page_count == 1:
                        break

        return topic_pages

    def get_like_query(self, text, checking_colum):
        def check_noun_query(text):
            ans = nltk.pos_tag([text])
            # ans returns a list of tuple
            val = ans[0][1]
            # checking if it is a noun or not
            if (val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP'):
                return True
            else:
                return False

        t = text.split()

        box = list(filter(check_noun_query, t))
        query = []
        for i in box:
            if i == box[len(box)-1]:
                query.append(checking_colum+" LIKE '%"+i+"%'")
            else:
                query.append(checking_colum+" LIKE '%"+i+"%' AND ")
        Like_query = ''.join(str(e) for e in query)
        return Like_query
