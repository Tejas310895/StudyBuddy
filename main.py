import flet as ft
from flet.buttons import RoundedRectangleBorder
from time import sleep
import modules.build as format
import modules.db as db
from datetime import datetime
import os


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
    page.theme = ft.Theme(color_scheme_seed="dark_theme",
                          visual_density=ft.ThemeVisualDensity.COMFORTABLE)

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
        "Kalam Regular": "/fonts/Kalam-Regular.ttf",
        "The Antique": "/fonts/TheAntique.ttf"
    }

    today = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

    def close_banner(e):
        page.banner.open = False
        page.update()

    def question_input_check(e):
        q_check_object = format.TopicListObject(page)
        if q_check_object.censor_check(e.control.value) == 'bad':
            chat_input.border_color = "#FF0000"
            page.banner = ft.Banner(
                bgcolor=ft.colors.AMBER_100,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED,
                                color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "Use proper english and non offensive words"
                ),
                actions=[
                    ft.TextButton("Ok", on_click=close_banner),
                ],
            )
            page.banner.open = True
            page.update()
        else:
            chat_input.border_color = "#33FF00"
            page.update()

    def explore_container():
        fornt_topic_object = format.TopicListObject(page)

        lv = ft.ListView(expand=True, spacing=0,
                         padding=ft.padding.all(2))

        try:
            db.cursor.execute(
                f"SELECT t.topic_title,u.user_name,t.icon_hex_code,t.topic_id FROM topic_details as t INNER JOIN users as u where t.user_id = u.user_id")
            topic_detais_fetch = db.cursor.fetchall()
            db.connection.commit()
        except db.Error as E:
            print(E)

        for i in topic_detais_fetch:
            lv.controls.append(fornt_topic_object.topic_object(
                i[0], i[1], i[2], i[3], page))

        return lv

    def submit_question(e):
        # try:
        #     db.cursor.execute(
        #         f"SELECT count(*) as q_dubi from topic_questions WHERE question='{chat_input.value}'")
        #     check_dubli_question = [j for i in db.cursor.fetchall() for j in i]
        #     db.connection.commit()
        # except db.Error as E:
        #     print(E)
        q_submit_check = format.TopicListObject(page)
        if chat_input.value == "":
            chat_input.hint_text = "Need to enter the question"
            page.update()
        elif q_submit_check.censor_check(chat_input.value) == 'bad':
            chat_input.hint_text = "Use proper questioning format"
            page.update()
        # elif check_dubli_question[0] > 0:
        #     chat_input.value = ""
        #     chat_input.hint_text = "This question is already asked check the history"
        #     page.update()
        else:
            try:
                chat_q_token_object = format.TopicListObject(page)
                chat_q_token = chat_q_token_object.get_random_token(10)
                db.cursor.execute("INSERT INTO topic_questions values (%s,%s,%s,%s,%s,%s,%s)", ('default', page.client_storage.get(
                    "user_id"), page.client_storage.get("top_id"), chat_input.value, chat_q_token, today, today))
                db.connection.commit()
                send_click(chat_q_token)
            except db.Error as E:
                print(E)

    def submit_answer(e):
        a_submit_check = format.TopicListObject(page)
        if chat_input.value == "":
            chat_input.hint_text = "Need to enter the answer"
            page.update()
        elif a_submit_check.censor_check(chat_input.value) == 'bad':
            chat_input.hint_text = "Use proper questioning format"
            page.update()
        else:
            try:
                chat_q_token_object = format.TopicListObject(page)
                chat_a_token = chat_q_token_object.get_random_token(10)
                db.cursor.execute("INSERT INTO topic_answers values (%s,%s,%s,%s,%s,%s,%s,%s)", ('default', page.client_storage.get(
                    "user_id"), page.client_storage.get("top_id"), resquested_question_button.data, chat_input.value, chat_a_token, today, today))
                db.connection.commit()
                chat_input.hint_text = "Enter your question"
                chat_button.on_click = submit_question
                page.client_storage.remove("chat_type")
                c_input_object.controls = [
                    ft.Row([
                        chat_input,
                        chat_button
                    ])]
                page.update()
                try:
                    db.cursor.execute(
                        f"SELECT question_token FROM topic_questions WHERE topic_question_id={resquested_question_button.data}")
                    chat_topic_q_token = [
                        j for i in db.cursor.fetchall() for j in i]
                    db.connection.commit()
                except db.Error as E:
                    print(E)
                send_click(chat_topic_q_token[0])
            except db.Error as E:
                print(E)
    chat_input = ft.TextField(
        hint_text="Enter your question",
        expand=True,
        height=40,
        multiline=True,
        content_padding=ft.padding.only(top=5, bottom=5, left=10),
        text_style=ft.TextStyle(font_family='JosefinSans Regular'),
        on_blur=question_input_check,
        on_focus=question_input_check)
    chat_button = ft.IconButton(icon=ft.icons.SEND_SHARP,
                                icon_color=ft.colors.ORANGE_ACCENT_400)
    resquested_question_icon = ft.Text(size=7, font_family='JosefinSans Regular',
                                       weight=ft.FontWeight.BOLD, tooltip=page.client_storage.get("chat_type"))
    resquested_question_text = ft.Text(
        font_family='JosefinSans Regular',
        size=12)
    resquested_question_button = ft.IconButton(icon=ft.icons.CANCEL_ROUNDED,
                                               icon_size=20,
                                               icon_color=ft.colors.WHITE,
                                               bgcolor=ft.colors.RED_ACCENT_200,
                                               width=20,
                                               height=20,
                                               style=ft.ButtonStyle(
                                                   padding=ft.padding.all(0)))
    resquested_question = ft.Row([ft.Container(resquested_question_icon,
                                               bgcolor=ft.colors.PURPLE_ACCENT_400,
                                               border_radius=50,
                                               width=15,
                                               height=15,
                                               alignment=ft.alignment.center,
                                               padding=ft.padding.only(
                                                   top=2),
                                               tooltip="Pankaj"),
                                  resquested_question_text,
                                  resquested_question_button
                                  ])

    def on_message(msg):
        try:
            db.cursor.execute(
                f"SELECT q.question,u.user_icon_hex,u.user_name,q.topic_question_id FROM topic_questions AS q INNER JOIN users AS u ON q.user_id = u.user_id WHERE q.question_token ='{msg}'")
            questions_for_topic_msg = [
                j for i in db.cursor.fetchall() for j in i]
            db.connection.commit()
        except db.Error as E:
            print(E)
        answer_against_question_msg = []
        try:
            db.cursor.execute(
                f"SELECT topic_answer,user_icon_hex,user_name FROM topic_answers AS a INNER JOIN users as u ON a.user_id = u.user_id where topic_question_id={questions_for_topic_msg[3]}")
            answer_against_question_msg = db.cursor.fetchall()
            db.connection.commit()
        except db.Error as E:
            print(E)
        try:
            get_similar_query = format.TopicListObject(page)
            db.cursor.execute(
                f"SELECT topic_answer,user_icon_hex,user_name FROM topic_answers AS a INNER JOIN users as u ON a.user_id = u.user_id INNER JOIN topic_questions as q ON a.topic_question_id = q.topic_question_id WHERE {get_similar_query.get_like_query(questions_for_topic_msg[0],'q.question')} and q.topic_question_id!={questions_for_topic_msg[3]}")
            similar_answer_msg = db.cursor.fetchall()
            db.connection.commit()
            answer_against_question_msg = answer_against_question_msg+similar_answer_msg
        except db.Error as E:
            print(E)
        answer_container_msg = []
        for i in answer_against_question_msg:
            if i == None:
                answer_container_msg = []
            else:
                answer_container_msg.append(
                    ft.ListTile(
                        leading=ft.Container(ft.Text(i[2][0], size=15, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                             bgcolor=f"{i[1]}",
                                             border_radius=50,
                                             width=30,
                                             height=30,
                                             alignment=ft.alignment.center,
                                             padding=ft.padding.only(
                                                 top=4),
                                             tooltip=i[2]
                                             ),
                        title=ft.Text(i[2],
                                      font_family='JosefinSans Regular'),
                        subtitle=ft.Column([
                            ft.Container(
                                ft.Text(
                                    i[0],
                                    font_family='JosefinSans Regular'
                                ), bgcolor=ft.colors.ORANGE_50, padding=ft.padding.all(10), border_radius=ft.border_radius.BorderRadius(topLeft=0, topRight=15, bottomLeft=15, bottomRight=15)
                            ),
                        ]),
                    )
                )
        messages.controls.append(
            ft.Column([
                ft.Container(
                    ft.TextButton(content=ft.Row([ft.Container(ft.Text(questions_for_topic_msg[2][0], size=10, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                                               bgcolor=f"{questions_for_topic_msg[1]}",
                                                               border_radius=50,
                                                               width=20,
                                                               height=20,
                                                               alignment=ft.alignment.center,
                                                               padding=ft.padding.only(
                        top=2),
                        tooltip="Pankaj"),
                        ft.Text(questions_for_topic_msg[0],
                                font_family='JosefinSans Regular',
                                size=15)]),
                        style=ft.ButtonStyle(
                        shape=RoundedRectangleBorder(
                            radius=ft.border_radius.BorderRadius(
                                topLeft=15,
                                topRight=15,
                                bottomLeft=0,
                                bottomRight=0)
                        ),
                        elevation=0,
                        bgcolor=ft.colors.PURPLE_50)),
                    padding=ft.padding.only(bottom=0),
                    data=questions_for_topic_msg[3],
                    on_click=change_chat_type
                ),
                ft.Container(
                    ft.Column(answer_container_msg), bgcolor=ft.colors.WHITE, padding=ft.padding.only(top=0)
                ),
            ], spacing=0)
        )
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(mmg):
        page.pubsub.send_all(mmg)
        # clean up the form
        chat_input.value = ""
        page.update()

    def change_chat_type(e):
        try:
            db.cursor.execute(
                f"SELECT q.question,u.user_icon_hex FROM topic_questions as q INNER JOIN users as u WHERE topic_question_id={e.control.data}")
            input_question_id = [j for i in db.cursor.fetchall() for j in i]
            db.connection.commit()
        except db.Error as E:
            print(E)
        page.client_storage.set("chat_type", e.control.data)
        chat_input.hint_text = "Enter your Answer"
        chat_button.on_click = submit_answer
        resquested_question_icon.value = input_question_id[0][1]
        resquested_question_icon.color = input_question_id[1]
        resquested_question_text.value = input_question_id[0]
        resquested_question_button.on_click = remove_pinned_question
        resquested_question_button.data = e.control.data
        c_input_object.controls = [
            resquested_question,
            ft.Row([
                chat_input,
                chat_button
            ])]
        page.update()

    def remove_pinned_question(e):
        chat_input.hint_text = "Enter your question"
        chat_button.on_click = submit_question
        page.client_storage.remove("chat_type")
        c_input_object.controls = [
            ft.Row([
                chat_input,
                chat_button
            ])]
        page.update()

    messages = ft.ListView(expand=True, spacing=10,
                           padding=ft.padding.all(2), auto_scroll=True)

    def study_container():
        messages.controls.clear()

        def chat_object(q_image, question, chat_user_name, question_id):
            answer_against_question = []
            try:
                db.cursor.execute(
                    f"SELECT topic_answer,user_icon_hex,user_name FROM topic_answers AS a INNER JOIN users as u ON a.user_id = u.user_id where topic_question_id={question_id}")
                answer_against_question = db.cursor.fetchall()
                db.connection.commit()
            except db.Error as E:
                print(E)
            try:
                get_similar_query = format.TopicListObject(page)
                db.cursor.execute(
                    f"SELECT topic_answer,user_icon_hex,user_name FROM topic_answers AS a INNER JOIN users as u ON a.user_id = u.user_id INNER JOIN topic_questions as q ON a.topic_question_id = q.topic_question_id WHERE {get_similar_query.get_like_query(question,'q.question')} and q.topic_question_id!={question_id}")
                similar_answer = db.cursor.fetchall()
                db.connection.commit()
                answer_against_question = answer_against_question+similar_answer
            except db.Error as E:
                print(E)
            answer_container = []
            for i in answer_against_question:
                if i == None:
                    answer_container = []
                else:
                    answer_container.append(
                        ft.ListTile(
                            leading=ft.Container(ft.Text(i[2][0], size=15, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                                 bgcolor=f"{i[1]}",
                                                 border_radius=50,
                                                 width=30,
                                                 height=30,
                                                 alignment=ft.alignment.center,
                                                 padding=ft.padding.only(
                                                     top=4),
                                                 tooltip=i[2]
                                                 ),
                            title=ft.Text(i[2],
                                          font_family='JosefinSans Regular'),
                            subtitle=ft.Column([
                                ft.Container(
                                    ft.Text(
                                        i[0],
                                        font_family='JosefinSans Regular'
                                    ), bgcolor=ft.colors.ORANGE_50, padding=ft.padding.all(10), border_radius=ft.border_radius.BorderRadius(topLeft=0, topRight=15, bottomLeft=15, bottomRight=15)
                                ),
                            ]),
                        )
                    )
            study_container = ft.Column([
                ft.Container(
                    ft.TextButton(content=ft.Row([ft.Container(ft.Text(chat_user_name[0], size=10, font_family='JosefinSans Regular', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                                               bgcolor=f"{q_image}",
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
                                  ),
                                  elevation=0,
                                  bgcolor=ft.colors.PURPLE_50)),
                    padding=ft.padding.only(bottom=0),
                    data=question_id,
                    on_click=change_chat_type
                ),
                ft.Container(
                    ft.Column(answer_container), bgcolor=ft.colors.WHITE, padding=ft.padding.only(top=0)
                ),
            ], spacing=0)

            return study_container
        try:
            db.cursor.execute(
                f"SELECT q.question,u.user_icon_hex,u.user_name,q.topic_question_id FROM topic_questions AS q INNER JOIN users AS u ON q.user_id = u.user_id WHERE q.topic_id = {page.client_storage.get('top_id')}")
            questions_for_topic = db.cursor.fetchall()
            db.connection.commit()
        except db.Error as E:
            print(E)

        for i in questions_for_topic:
            messages.controls.append(chat_object(i[1], i[0], i[2], i[3]))
        page.update()

    def user_auth(e):
        if login_user_email.value == "":
            login_user_email.helper_text = "This field cannot be empty"
            page.update()
        else:
            login_user_email.helper_text = ""
            page.update()
        if login_user_password.value == "":
            login_user_password.helper_text = "This filed cannot be empty"
            page.update()
        else:
            login_user_password.helper_text = ""
            page.update()

        if login_user_email.value != "" and login_user_email.value != "":
            db.cursor.execute(
                f"SELECT user_email,user_password FROM users WHERE user_email='{login_user_email.value}'",)
            auth_verify = db.cursor.fetchall()
            db.connection.commit()
            if ([(login_user_email.value, login_user_password.value)]) == auth_verify:
                try:
                    db.cursor.execute(
                        f"SELECT user_id FROM users WHERE user_email='{login_user_email.value}'",)
                    user_id_list = [j for i in db.cursor.fetchall() for j in i]
                    db.connection.commit()
                    page.client_storage.set("user_id", user_id_list[0])
                    page.go("/")
                except db.Error as E:
                    print(E)

    def add_new_topic(e):
        if new_topic_name.value == "":
            new_topic_name.helper_text = "This field cannot be empty"
            page.update()
        else:
            new_topic_name.helper_text = ""
            page.update()
        if new_topic_desc.value == "":
            new_topic_desc.helper_text = "This field cannot be empty"
            page.update()
        else:
            new_topic_desc.helper_text = ""
            page.update()
        if new_topic_tags.value == "":
            new_topic_tags.helper_text = "This field cannot be empty"
            page.update()
        else:
            new_topic_tags.helper_text = ""
            page.update()
        if new_topic_name.value != "" and new_topic_desc.value != "" and new_topic_tags.value != "":
            topic_hex_code = format.TopicListObject(page)
            try:
                db.cursor.execute(
                    "INSERT INTO topic_details values (%s,%s,%s,%s,%s,%s,%s,%s)", ('default', page.client_storage.get('user_id'), topic_hex_code.get_hex_colors(), new_topic_name.value, new_topic_desc.value, new_topic_tags.value, today, today))
                db.connection.commit()

                page.banner = ft.Banner(
                    bgcolor=ft.colors.GREEN_ACCENT_100,
                    leading=ft.Icon(ft.icons.DONE,
                                    color=ft.colors.GREEN_600, size=40),
                    content=ft.Text(
                        "New topic is successfully added"
                    ),
                    actions=[
                        ft.TextButton("Ok", on_click=close_banner),
                    ],
                )
                page.banner.open = True
                page.update()
                page.go("/")
            except db.Error as E:
                print(E)
                page.banner = ft.Banner(
                    bgcolor=ft.colors.AMBER,
                    leading=ft.Icon(ft.icons.WARNING_AMBER,
                                    color=ft.colors.AMBER, size=40),
                    content=ft.Text(
                        "Failed to add the new topic, Try again"
                    ),
                    actions=[
                        ft.TextButton("Ok", on_click=close_banner),
                    ],
                )
                page.banner.open = True
                page.update()

    login_user_email = ft.TextField(
        label="Email Id",
        hint_text="Enter your registered Email id",
        label_style=ft.TextStyle(
            font_family='JosefinSans Regular', size=15),
        hint_style=ft.TextStyle(
            font_family='JosefinSans Regular', size=15)
    )
    login_user_password = ft.TextField(
        label="Password",
        hint_text="Enter your Password",
        can_reveal_password=True,
        password=True,
        label_style=ft.TextStyle(
            font_family='JosefinSans Regular', size=15),
        hint_style=ft.TextStyle(
            font_family='JosefinSans Regular', size=15)
    )

    new_topic_name = ft.TextField(label="Topic Name", hint_text="Enter unique topic name", text_style=ft.TextStyle(
        font_family='JosefinSans Regular', size=18), content_padding=ft.padding.only(top=5, bottom=5, left=10))
    new_topic_desc = ft.TextField(label="Topic Description", hint_text="Enter topic Description", text_style=ft.TextStyle(
        font_family='JosefinSans Regular', size=18), content_padding=ft.padding.only(top=5, bottom=5, left=10))
    new_topic_tags = ft.TextField(label="Topic Tags", hint_text="#biology,#maths,#python", text_style=ft.TextStyle(
        font_family='JosefinSans Regular', size=18), content_padding=ft.padding.only(top=5, bottom=5, left=10))

    def insert_c_input_object():
        if page.client_storage.get("chat_type") == None:
            chat_input.hint_text = "Enter your question"
            chat_button.on_click = submit_question
            chat_body = [ft.Row([
                chat_input,
                chat_button
            ])]
        else:
            chat_input.hint_text = "Enter your Answer"
            chat_button.on_click = submit_answer
            chat_body = [resquested_question, ft.Row([
                chat_input,
                chat_button
            ])]
        c_input_object.controls = chat_body
        page.update()
    c_input_object = ft.Column()

    def open_book(e):
        base = r"assets\books"
        file_name = f"\{e.control.data}"
        path = base+file_name+".pdf"
        os.system(path)

    def library_container():
        try:
            db.cursor.execute(f"Select book_title from library")
            books_dump = db.cursor.fetchall()
        except db.Error as E:
            print(E)
        library_lv = ft.ListView(expand=1, spacing=10,
                                 padding=20, auto_scroll=True)
        for i in books_dump:
            library_lv.controls.append(
                ft.Container(
                    ft.ListTile(
                        leading=ft.Icon(
                            ft.icons.MENU_BOOK, color="#FBFF00"),
                        title=ft.Text(
                            i[0], color="#FBFF00", font_family="The Antique", size=25),
                        trailing=ft.IconButton(
                            icon=ft.icons.OPEN_IN_BROWSER_ROUNDED, icon_color="#00E1FF", on_click=open_book, data=i[0]),
                    ), bgcolor="#141215",
                    border_radius=ft.border_radius.all(15)
                )
            )
        return library_lv

    def route_change(route):
        page.views.clear()
        main_app_bar = format.TopicListObject(page)
        custom_app_bar = format.TopicListObject(page)
        bottom_bar = format.TopicListObject(page)
        if page.client_storage.get("user_id") == None:
            page.views.append(
                ft.View(
                    "/user_login",
                    [
                        ft.Container(
                            ft.Column([
                                ft.Container(
                                    ft.Image(
                                        src=f"/images/logo.png", width=100),
                                    alignment=ft.alignment.center),
                                ft.Container(
                                    ft.Text("Study-Buddy", font_family="Frozito",
                                            size=20, color=ft.colors.ORANGE_ACCENT_200),
                                    alignment=ft.alignment.center),
                                login_user_email,
                                login_user_password,
                                ft.ElevatedButton(
                                    "Login",
                                    elevation=0,
                                    bgcolor=ft.colors.GREEN_ACCENT_400,
                                    color=ft.colors.WHITE,
                                    width=500,
                                    on_click=user_auth)
                            ], alignment=ft.MainAxisAlignment.CENTER), expand=True,
                            alignment=ft.alignment.center
                        )

                    ],
                )
            )
        else:
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
            study_container()
            insert_c_input_object()
            db.cursor.execute(
                f"SELECT icon_hex_code,topic_title,topic_desc FROM topic_details WHERE topic_id={page.client_storage.get('top_id')}")
            topic_list = db.cursor.fetchall()
            db.connection.commit()
            page.views.append(
                ft.View(
                    "/info_block",
                    [
                        custom_app_bar.custom_appbar(
                            page, 'chat_head', topic_list[0][0], topic_list[0][1], topic_list[0][2]),
                        messages,
                        c_input_object
                    ],
                )
            )
        elif page.route == "/add_topic":
            page.views.append(
                ft.View(
                    "/add_topic",
                    [
                        custom_app_bar.custom_appbar(
                            page, topic_title="Add Topic"),
                        ft.Column([
                            new_topic_name,
                            new_topic_desc,
                            new_topic_tags,
                            ft.ElevatedButton(
                                "Submit", color=ft.colors.WHITE,
                                elevation=0,
                                width=300,
                                bgcolor=ft.colors.GREEN_ACCENT_200,
                                on_click=add_new_topic)
                        ]),
                        bottom_bar.bottom_nav(page)

                    ],
                )
            )
        elif page.route == "/library":
            page.views.append(
                ft.View(
                    "/library",
                    [
                        custom_app_bar.custom_appbar(
                            page, topic_title="Library"),
                        library_container(),
                        bottom_bar.bottom_nav(page),
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


ft.app(target=main, view=ft.FLET_APP, assets_dir="assets")
