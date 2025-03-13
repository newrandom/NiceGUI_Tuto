from nicegui import ui

# https://quasar.dev/vue-components/button
def btnClicked():
    ui.notify('Button Clicked!')

ui.button(text="This is Q-Button", color="None", icon="thumb_up").on_click(btnClicked)

for i in range(0,3):
    ui.space()      # 공란 (<br>)

# 버튼 클릭 알림 기능 (ui.notify)
# https://quasar.dev/quasar-plugins/notify#notify-api
with ui.row():
    ui.button('non_multiLine', on_click=lambda:ui.notify(message="multiLine 미적용", position='top', close_button=True, type='positive', color='None', multi_line=False))
    ui.button('multiLine', on_click=lambda:ui.notify(message="multiLine 적용", position='top', close_button='닫기', type='positive', color='None', multi_line=True))

''' Async Button 작업

# async clicked() 함수를 사용하여 버튼 클릭을 기다림
async def button_handler():
    button = ui.button("Async Button")
    await button.clicked()
    ui.label('Button was clicked')

def start_async_task():
    ui.timer(0.1, lambda:button_handler(), once=True)       # 0.1초 뒤에 실행

start_async_task()      # 비동기 작업 등록
'''

if __name__ in ('__main__', '__mp_main__'):
    ui.run()