import flet as ft


class Message():
    def __init__(self, user: str, text: str, message_type: str):
        self.user = user
        self.text = text
        self.message_type = message_type


def main(page: ft.Page):

    chat = ft.Column()
    new_message = ft.TextField()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            chat.controls.append(ft.Text(f"{message.user}: {message.text}"))
        elif message.message_type == "login_message":
            chat.controls.append(
            ft.Text(message.text, italic=True, color=ft.colors.BLACK45, size=12)
            )
    page.update()

    page.pubsub.subscribe(on_message)
    def join_click(e):
        if not user_name.value:
            user_name.error_text = "Name cannot be blank!"
            user_name.update()
        else:
             page.session.set("user_name", user_name.value)
             page.dialog.open = False
             page.pubsub.send_all(Message(user=user_name.value, text=f"{user_name.value} has joined the chat.", message_type="login_message"))
             page.update()

    user_name = ft.TextField(label="Enter your name")

    page.dialog = ft.AlertDialog(

        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([user_name], tight=True, alignment=ft.MainAxisAlignment.CENTER),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end"
    )

    def send_click(e):
     page.pubsub.send_all(Message(user=page.session.get('user_name'), text=new_message.value, message_type="chat_message"))
     new_message.value = ""
     page.update()

    page.add(chat, ft.Row([new_message, ft.ElevatedButton("Send", on_click=send_click)], alignment=ft.MainAxisAlignment.CENTER))
    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


ft.app(target=main)
