# main page > button > sql 에서 data 가져오기 > table 로 나타내기

from nicegui import ui, app
from config import load_config
import psycopg2, pandas as pd

# MainPage 생성
ui.label("Hello World").tooltip("this is a label")

def dbConnectionTest():
    msg = ""
    try:
        with psycopg2.connect(**load_config()) as conn:
            print('Connected to the PostgreSQL server.')
            msg = 'Connected to the PostgreSQL server.'
            return (conn, msg)
    except (Exception, psycopg2.DatabaseError) as error:
        msg = error
        return (None, msg)

# sql에서 데이터 가져오기
def loadData():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ACTOR")
                rows = cur.fetchall()
                if rows:
                    # df = pd.DataFrame(rows, columns=['actor_id', 'first_name', 'last_name', 'last_update'])
                    query_cols = [cur.description[i][0] for i in range(len(cur.description))]
                    df = pd.DataFrame(rows, columns = query_cols)
                    ui.notify(f"{len(rows)} 데이터를 가져왔습니다.")
                    print(df.head())
                return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# button 생성
# ui.button("DB접속하기", on_click=dbConnectionTest)
with ui.row():
    ui.button("DB접속하기", on_click=lambda:ui.notify(dbConnectionTest()[1]))
    with ui.button("데이터 가져오기", on_click=loadData) as btn:
        pass

# table 생성
table = ui.table(columns=[], rows=[]).classes('w-full')

def update_table(df:pd.DataFrame):
    table.columns = [{'name': col, 'label':col, 'field':col} for col in df.columns]
    table.rows = df.to_dict(orient='records')
# ui.table.from_pandas(df)#.classes('max-h-40')

map = ui.leaflet(center=(37.512, -232.929), zoom=9)
ui.label().bind_text_from(map, 'center', lambda center:f"Center:{center[0]:.3f}, {center[1]:.3f}")
ui.label().bind_text_from(map, 'zoom', lambda zoom:f'Zoom : {zoom}')

# 프로그램 실행
dev = False
if dev:
    app.native.settings['OPEN_DEVTOOLS_IN_DEBUG'] = True
    app.native.start_args['debug'] = True

ui.run(native=True, language='ko-KR')