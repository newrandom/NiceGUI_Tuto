from nicegui import app, ui

@ui.page('/')
def index():
    ui.textarea('This note is kept between visits').classes('w-full').bind_value(app.storage.user, 'note')

# print(app.storage.user.items()    )

ui.run(storage_secret="my_secret_key")