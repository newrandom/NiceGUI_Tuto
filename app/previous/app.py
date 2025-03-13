from nicegui import app, ui, native

app.native.window_args['resizable'] = False
# app.native.start_args['debug'] = True
app.native.settings['ALLOW_DOWNLOADS'] = True

ui.label('app running in native mode')

chat_box = ui.column()
input_field = ui.input(placeholder='메시지를 입력하세요...')

def send_message():
    message = input_field.value.strip()
    if message:
        # chat_box.add_slot()
        # chat_box.add(ui.label(f"사용자 : {message}"))
        # chat_box.append('test')
        with chat_box:
            ui.label(f"사용자 : {message}")
        input_field.value = ""

input_field.on("keydown.enter", lambda: send_message())        

ui.button('전송', on_click=send_message)


ui.button('enlarge', on_click=lambda: app.native.main_window.resize(1000, 700))
ui.button('reload', on_click=lambda: app.native.main_window.resize(400, 300))

# ui.run(native=True, window_size=(400, 300), fullscreen=False, language='ko-KR', reload=False,port=native.find_open_port())        # app version
ui.run(native=False, window_size=(400, 300), fullscreen=False, language='ko-KR', reload=False,port=native.find_open_port())     # web version