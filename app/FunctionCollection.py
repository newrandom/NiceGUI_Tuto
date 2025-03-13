from config import load_config
import psycopg2, pandas as pd
from nicegui import ui, app

class FunctionClass():
    def __init__(self):
        pass

    # DB 연결 테스트
    def dbConnectionTest(self) -> tuple:
        msg = ""
        try:
            with psycopg2.connect(**load_config()) as conn:
                print('Connected to the PostgreSQL server.')
                msg = 'Connected to the PostgreSQL server.'
                return (conn, msg)
        except (Exception, psycopg2.DatabaseError) as error:
            msg = error
            return (None, msg)
    
    # DB 연결 테스트 결과 (on_click 호출용)
    def dbConResult(self) -> None:
        result = self.dbConnectionTest()
        ui.notify(result[1])
        
    # Select Query 실행
    def loadData(self, select_query:str="") -> pd.DataFrame:
        df = pd.DataFrame()
        if select_query != "":
            config = load_config()
            try:
                with psycopg2.connect(**config) as conn:
                    with conn.cursor() as cur:
                        cur.execute(select_query)
                        rows = cur.fetchall()
                        if rows:
                            query_cols = [cur.description[i][0] for i in range(len(cur.description))]
                            df = pd.DataFrame(rows, columns = query_cols)
                            ui.notify(f"{len(rows)} 데이터를 가져왔습니다.")
            except (Exception, psycopg2.DatabaseError) as error:
                ui.notify(error)
            finally:
                return df
        else:
            ui.notify("Query를 입력해주세요.")
            return df
        
    # Table에 데이터 넣기
    def setTable(self, target_table:ui.table, source_df:pd.DataFrame) -> None:
        target_table.columns = [
            {'name': col, 'label':col, 'field':col} for col in source_df.columns
        ]
        target_table.rows = source_df.to_dict(orient='records')
        
    # Table 데이터 리셋
    def resetTable(self, target_table:ui.table) -> None:
        target_table.columns = []
        target_table.rows = []
        ui.notify("테이블을 초기화했습니다.")

    # Select 쿼리의 컬럼 label 설정
    def queryColumnLabel(self, target_table:ui.table, labelList:list) -> None:
        if len(labelList) == len(target_table.columns):
            for i in range(len(target_table.columns)):
                target_table.columns[i]['label'] = labelList[i]