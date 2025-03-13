from nicegui import ui, Client, app
from nicegui.page import page
from fastapi import Request

"""
    html 오류 코드 발생 시 처리
    - 기본적으로 404 오류 발생 시에는 nicegui의 404 페이지가 나타난다.
"""

@ui.page('/')
def main():
    ui.label('This is Home Page')

    with ui.row():
        ui.button('Existing Address', on_click=lambda:ui.navigate.to('/existing'))
        ui.button('Wrong Address', on_click=lambda:ui.navigate.to('/wrong'))

@ui.page('/existing')
def existing():
    ui.label('This is Existing Page')
    ui.button('Go Back', on_click=lambda:ui.navigate.back())

""" 404 오류 발생시 처리 """
@app.exception_handler(404)
async def custom_404_handler(request:Request, exception:Exception):
    with Client(page=page(''), request=request) as client:
        with ui.card(align_items='center').classes('w-full'):
            ui.label(f'{request.url.path} does not exist')
            ui.button('Go back to Home' , on_click=lambda:ui.navigate.to('/'), icon='home')
    return client.build_response(request, 404)

# @app.exception_handler(500)
# async def exception_handler_500(request: Request, exception: Exception) -> Response:
#     stack_trace = traceback.format_exc()
#     msg_to_user = f"**{exception}**\n\nStack trace: \n<pre>{stack_trace}"

#     if OTAP == 'P':   # production -> send trace by mail & nice soothing message
#         mailres = send_mail_somehow(from, to, etc, etc, msg_to_user)
#         msg_to_user = _("Incident has been reported, repair is underway.")

#     with Client(page(''), request=request) as client:
#         with theme.frame("error"):
#             with ui.card().classes("error-card"):
#                 ui.label(_("500 Application Error")).classes("heading")
#                 ui.markdown(msg_to_user).classes("message")
#     return client.build_response(request, 500)

ui.run()