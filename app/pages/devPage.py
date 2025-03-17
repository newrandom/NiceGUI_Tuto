from nicegui import ui


@ui.page('/dev')
def devPage():
    ui.page_title('개발 페이지')
    ui.label('개발 페이지')

    fab = ui.element('q-fab').props('icon=home color=green')

    # draggable 속성을 true로 설정
    input_element = ui.input().props('draggable').classes('w-full').props('id=input_element')
    button_element = ui.button('Click me').props('draggable').classes('w-full').props('id=button_element')
    label_element = ui.label('Drag me').props('draggable').classes('w-full').props('id=label_element')

    # draggable 속성을 false로 설정
    non_draggable_input = ui.input().props('draggable="false"').classes('w-full')
    non_draggable_button = ui.button('Click me').props('draggable="false"').classes('w-full')
    non_draggable_label = ui.label('Cannot drag me').props('draggable="false"').classes('w-full')

    ui.separator()

    # 드래그 시작 이벤트 핸들러 추가
    def handle_dragstart(event):
        event.args['data'] = event.sender.props['id']

    # 드래그 가능한 요소에 이벤트 핸들러 추가
    input_element.on('dragstart', handle_dragstart)
    button_element.on('dragstart', handle_dragstart)
    label_element.on('dragstart', handle_dragstart)

    # 드롭 이벤트 핸들러 추가
    def handle_drop(event):
        event.preventDefault()
        data = event.args['data']
        ui.notify(f'{data} dropped!')

    # 드롭 가능한 영역에 이벤트 핸들러 추가
    with ui.card().on('drop', handle_drop).on('dragover.prevent'):
        ui.label('여기에 드랍해봐')

    ui.separator()
    ui.button('돌아가기', on_click=lambda: ui.navigate.to('/'))

    pass