# main page > button > sql 에서 data 가져오기 > table 로 나타내기
from FunctionCollection import *
from fastapi import Request
from starlette.responses import HTMLResponse
from nicegui.page import page
from nicegui import Client

fc = FunctionClass()

@ui.page('/')
def mainPage():
    # MainPage 생성
    ui.label("Hello World")

    # button 생성
    with ui.row():
        btnConTest = ui.button("DB접속 테스트", on_click=fc.dbConResult)
        btnGetData = ui.button("DB데이터 가져오기")
        btnResetData = ui.button("테이블 초기화")
    
    ui.separator()

    # table 생성
    dataTable = ui.table(columns=[], rows=[], pagination=10).classes('w-full')

    ## 버튼 생성 > 테이블생성 > 버튼에서 클릭 이벤트 발생 시 테이블에 데이터 생성하기
    def getDataEvent() -> None:
        select_query = "select actor_id , first_name, last_name, to_char(last_update,'yyyy-mm-dd hh24:mi:ss') last_update from actor"
        df = fc.loadData(select_query)
        try:
            fc.setTable(dataTable,df)
            dataTable.row_key = 'actor_id'
            # dataTable.add_slot(f'body-cell-{dataTable.row_key}', """
            #     <q-td :props="props">
            #         <a :href="'detail/'+props.value">{{ props.value }}</a>
            #     </q-td>
            # """)
            dataTable.add_slot('body-cell', """
                <q-td :props="props">
                    <a :href="'detail/'+props.row.actor_id">{{ props.value }}</a>
                </q-td>
            """)
            transList = ['배우ID', '이름','성','최근수정일']
            fc.queryColumnLabel(dataTable, transList )
        except (Exception) as e:
            print(e)

    btnGetData.on_click(getDataEvent)

    # 초기화버튼 이벤트 연결
    btnResetData.on_click(lambda:fc.resetTable(dataTable))

@ui.page('/detail/{actor_id}')
def detailPage(actor_id:int):
    ui.label(f"Detail Page {actor_id}")
    ui.button('이전페이지로', on_click=lambda:ui.navigate.back())

# https://github.com/zauberzeug/nicegui/discussions/883
@app.exception_handler(404)
async def custom_404_handler(request: Request, exception:Exception):
    # return HTMLResponse(
    #     content="""<html><head><title>Page Not Found</title></head><body style="text-align:center; font-family:sans-serif;"><h1>404 - Page Not Found</h1><p>The page you are looking for does not exist.</p><a href='/'>Go Back to Home</a></body></html>""",
    #     status_code=404
    # )
    with Client(page=page(''), request=request) as client:
        with ui.card(align_items='center').classes('w-full'):
            ui.label('Sorry, this page does not exist')
            ui.button('Go back to Home', on_click=lambda:ui.navigate.to('/'), icon='home')
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

# 프로그램 실행
app.native.window_args['resizable'] = False
app.native.settings['ALLOW_DOWNLOADS'] = False
ui.run(native=True, window_size=(1000,800), language='ko-KR', title='DB 연동 테스트' )