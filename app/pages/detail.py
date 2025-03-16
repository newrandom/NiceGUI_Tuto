from nicegui import ui
from FunctionCollection import FunctionClass
from pages.actors_film import *
import requests, time

fc = FunctionClass()

@ui.page('/detail/{actor_id}')
def detailActor(actor_id:int):
    # print(request)
    ui.label(f'Actor ID : {actor_id}')

    data = fc.loadData(f"select * from actor where actor_id = '{actor_id}' ")

    ui.separator()
    columnDef = [
        {'headerName' : 'actor_id', 'field' : 'actor_id', 'hide' : True},
        {'headerName' : '성', 'field' : 'last_name', 'editable':True},
        {'headerName' : '이름', 'field' : 'first_name', 'editable':True},
        {'headerName' : 'last_update', 'field' : 'last_update', 'hide' : True}
    ]

    rowData = [
        {k : data[k].values[0] for k in data.columns}
    ]

    # # dialog 생성
    # with ui.dialog() as dialog, ui.card():
    #     ui.label('저장하시겠습니까?')
    #     with ui.row():
    #         btnOk = ui.button('저장하기')
    #         btnCancel = ui.button('취소하기')

    # Dialog 버튼 이벤트
    def dialogOk(dialog: ui.dialog, grid: ui.aggrid, kvPair: dict):
        try:
            a = grid.props['options']['rowData']
            for i in range(len(a)):
                setQuery = []
                # for key in a[i]:
                for key in kvPair.keys():
                    if key == 'last_update':
                        setQuery.append(f"{key} = now()")
                    else:
                        setQuery.append(f"{key} = '{kvPair[key]}'")
                updateQuery = "update actor set " + ", ".join(setQuery) + f" where actor_id = '{actor_id}' "
                print(updateQuery)
                fc.queryExecute(updateQuery)
            dialog.close()
            ui.notify('저장되었습니다.', actions=[{'icon': 'check', 'label': '확인', 'onclick': 'location.reload(true)'}])
        except Exception as e:
            print(f"Error updating data: {e}")
            ui.notify(f"Error: {e}")

    def dialogCancel(dialog:ui.dialog):
        dialog.close()
        # ui.notify('취소되었습니다.', type='positive', close_button='확인')
        ui.navigate.reload()

    # cellChange 이벤트 발생 시 데이터 업데이트
    def update_data_from_table_change(e):
        row = grid.props['options']['rowData'][e.args['rowIndex']]

        # 데이터 확인
        colId = e.args['colId']
        orgData = e.args['oldValue']
        cngData = e.args['value']

        kvPair = {colId : cngData, 'last_update' : 'now()'}

        with ui.dialog() as dig, ui.card(align_items='center'):
            ui.label(f"{e.args['colId']}의 {orgData}를 {cngData}로 변경하시겠습니까?")
            with ui.row(align_items='center'):
                btnOk = ui.button('예',on_click=lambda:dialogOk(dig, grid,kvPair))
                btnCancel = ui.button('아니오', on_click=lambda:dialogCancel(dig))

        dig.open()

    grid = ui.aggrid({
        'columnDefs' : columnDef,
        'rowData' : rowData,
    }).on("cellValueChanged", update_data_from_table_change)

    with ui.row():
        # ui.button('저장하기',on_click=dialog.open)
        ui.button('새로고침',on_click=ui.navigate.reload)
        ui.button('이전페이지로', on_click=lambda:ui.navigate.to('/'))
        ui.button('출연작 보러가기', on_click=lambda:ui.navigate.to(f'/actors_film/{actor_id}'))

if __name__ in  ('__main__', '__mp_main__'):
    ui.run()