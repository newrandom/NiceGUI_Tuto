from nicegui import ui


@ui.page('/dev')
def devPage():
    ui.label('개발 페이지')

    draggableBtn =  ui.button('드래그 테스트',)


    pass