import flet as ft

def main(page: ft.Page):
    page.title = "Простое чат-приложение"
    page.vertical_alignment = ft.MainAxisAlignment.START

    chat_box = ft.ListView(expand=True)
    input_field = ft.TextField(hint_text="Введите сообщение...", expand=True)
    send_button = ft.ElevatedButton("Отправить", on_click=lambda e: send_message())

    def send_message():
        message = input_field.value.strip()
        if message:
            chat_box.controls.append(ft.Text(f"You: {message}", size=16))
            input_field.value = ""
            page.update()

    page.add(chat_box, ft.Row([input_field, send_button]))

ft.app(target=main)