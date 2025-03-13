from nicegui import ui
import asyncio

# 공유할 데이터 (모든 클라이언트가 이 데이터를 공유)
data = [{"이름": "홍길동", "나이": 30}, {"이름": "김철수", "나이": 25}]

# UI에 표시할 그리드
grid = ui.table(columns=[
    {"name": "이름", "label": "이름", "field": "이름", "editable": True},
    {"name": "나이", "label": "나이", "field": "나이", "editable": True},
], rows=data)

# 데이터 변경 시 호출될 함수
def update_data(event):
    row_index = event.args["rowIndex"]  # 변경된 행의 인덱스
    field = event.args["column"]["field"]  # 변경된 컬럼
    new_value = event.args["value"]  # 변경된 값

    data[row_index][field] = new_value  # 데이터 업데이트
    ui.notify(f"데이터 변경됨: {data}")  # 변경 알림

    # 모든 클라이언트가 UI 업데이트하도록 강제 렌더링
    asyncio.create_task(refresh_grid())

# UI 업데이트 함수 (모든 클라이언트가 새 데이터 반영)
async def refresh_grid():
    grid.rows = data  # 테이블 데이터 갱신
    await ui.update()  # 모든 클라이언트에서 UI 업데이트

# 테이블에서 값이 변경되었을 때 이벤트 연결
grid.on("cellEdit", update_data)

ui.run(port=8080, native=False,window_size=(400, 300), fullscreen=False, language='ko-KR',)
