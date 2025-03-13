from nicegui import ui

# https://quasar.dev/options/quasar-icon-sets : Quasar icon sets

@ui.page('/')
def index():
    ui.label('Hello, world')
    ui.button('link to /test', on_click=lambda:ui.navigate.to('/test'))

@ui.page('/test')
def test():
    ui.label('This page is Test Page')
    ui.button('link to MainPage', on_click=lambda:ui.navigate.to('/'), icon='home')
    ui.button('link to previous page', on_click=lambda:ui.navigate.back(),icon="arrow_back")

if __name__ in ("__main__","__mp_main__"):
    ui.run()