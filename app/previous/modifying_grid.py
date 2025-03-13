from nicegui import ui
import asyncio

# 공유할 데이터 (모든 클라이언트가 이 데이터를 공유)
data = [
    {"이름": "홍길동", "나이": 30},
    {"이름": "김철수", "나이": 25},
]

# 테이블 UI
with ui.table(columns=[
    {"name": "이름", "label": "이름", "field": "이름"},
    {"name": "나이", "label": "나이", "field": "나이"},
    {"name": "수정", "label": "수정", "field": "수정"},
], rows=data) as grid:
    pass  # 테이블 초기화

# 데이터 변경 다이얼로그
with ui.dialog() as edit_dialog, ui.card():
    ui.label("데이터 수정")
    name_input = ui.input("이름")
    age_input = ui.input("나이")
    
    # 데이터 저장 버튼
    def save_data():
        if selected_row is not None:
            data[selected_row]["이름"] = name_input.value
            data[selected_row]["나이"] = age_input.value
            asyncio.create_task(refresh_grid())  # UI 업데이트
        edit_dialog.close()

    ui.button("저장", on_click=save_data)

selected_row = None  # 현재 선택된 행 인덱스

# 데이터 편집 함수
def edit_data(row_index):
    global selected_row
    selected_row = row_index
    name_input.value = data[row_index]["이름"]
    age_input.value = data[row_index]["나이"]
    edit_dialog.open()

# 수정 버튼 추가 (각 행마다 추가)
for i, row in enumerate(data):
    row["수정"] = ui.button("수정", on_click=lambda i=i: edit_data(i))

# UI 업데이트 함수 (모든 클라이언트에서 데이터 반영)
async def refresh_grid():
    grid.rows = data  # 테이블 데이터 업데이트
    await ui.update()  # 모든 클라이언트에서 UI 업데이트

ui.run(port=8080, native=False, window_size=(400, 300))
