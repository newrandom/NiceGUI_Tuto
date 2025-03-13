from nicegui import ui
import pandas as pd
#https://nicegui.io/documentation/table#table

def table1():
    ui.label(f'기본적인 Table')    
    columns = [
        {'name' : 'name', 'label' : '이름', 'field':'name', 'required':True, 'align':'left'},
        {'name' : 'age', 'label' : '나이', 'field':'age', 'required':False, 'align':'center'},
        {'name': 'phone', 'label' : '전화번호', 'field':'phone', 'required':False, 'align':'right'},
    ]

    data = [
        {'name':'홍길동', 'age':20, 'phone':'010-1234-5678'},
        {'name':'김철수', 'phone':'010-2345-6789'},
        {'name':'이영희', 'age':30, },
    ]

    ui.table(columns=columns, rows=data, row_key='name')

def table2():
    ui.label(f'데이터에서 Table 컬럼 자동 생성 (Omitting columns)')
    ui.table(rows=[
        {'make':'Toyota', 'model': 'Celica', 'price':35000},
        {'make':'Ford', 'model': 'Mondeo', 'price':32000},
        {'make':'Porsche', 'model': 'Boxster', 'price':72000},
    ])

def table3():
    ui.label(f'컬럼 속성 기본설정 (Default column parameters)')
    ui.table(rows=[
                {'name':'Alice', 'age':18, 'phone':'010-1234-5678'},
                {'name':'Bob', 'age':25, 'phone':'010-2345-6789'},
                {'name':'Charlie', 'age':30, 'phone':'010-3456-7890'},
            ], columns=[
                {'name':'name', 'label':'이름', 'field':'name', 'required':True,},
                {'name':'age','label':'나이', 'field':'age', 'required':False,},
                {'name':'phone', 'label':'전화번호', 'field':'phone', 'required':False,},
            ], column_defaults={
                'align':'left',
                'headerClasses':'uppercase text-primary',
            })
    
def table4():
    def canNotify(selection:list):
        if selection:
            # ui.notify(f"{selection}를 선택하셨습니다.")
            names = [row['name'] for row in selection]
            ui.notify(f"{', '.join(names)} 를 선택하셨습니다.")
        else:
            ui.notify(f"선택된 데이터가 없습니다.")

    ui.label(f'Selection 추가')
    table = ui.table(
        columns=[{'name':'name', 'label':'Name', 'field':'name'}],
        rows=[{'name':'Alice'}, {'name':'Bob'}, {'name':'Charlie'}],
        row_key='name',
        # on_select=lambda row: ui.notify(f'selected: {row.selection}') if row.selection else None,
        on_select=lambda row: canNotify(row.selection),
    )    
    ui.radio({None:'none', 'silgle':'single', 'multiple':'multiple'},
             on_change=lambda e: table.set_selection(e.value))
    
def table5():
    ui.link("행 확장 (expandable rows)", "https://quasar.dev/vue-components/table/#expanding-rows", new_tab=True)
    columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name'},
    {'name': 'age', 'label': 'Age', 'field': 'age'},
    ]
    rows = [
        {'name': 'Alice', 'age': 18},
        {'name': 'Bob', 'age': 21},
        {'name': 'Carol'},
    ]

    table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-72')
    table.add_slot('header', r'''
        <q-tr :props="props">
            <q-th auto-width />
            <q-th v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.label }}
            </q-th>
        </q-tr>
    ''')
    table.add_slot('body', r'''
        <q-tr :props="props">
            <q-td auto-width>
                <q-btn size="sm" color="accent" round dense
                    @click="props.expand = !props.expand"
                    :icon="props.expand ? 'remove' : 'add'" />
            </q-td>
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.value }}
            </q-td>
        </q-tr>
        <q-tr v-show="props.expand" :props="props">
            <q-td colspan="100%">
                <div class="text-left">This is {{ props.row.name }}.</div>
            </q-td>
        </q-tr>
    ''')    

def table6():
    ui.link("Pandas를 이용한 테이블", "https://nicegui.io/documentation/table#table_from_pandas_dataframe", new_tab=True)
    df = pd.DataFrame(data={'col1':[1,2], 'col2':[3,4]})
    ui.table.from_pandas(df).classes('max-h-40')

def table7():
    ui.link("셀에 링크달기", "https://nicegui.io/documentation/table#table_cells_with_links", new_tab=True)
    columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
    {'name': 'link', 'label': 'Link', 'field': 'link', 'align': 'left'},
    ]
    rows = [
        {'name': 'Google', 'link': 'https://google.com'},
        {'name': 'Facebook', 'link': 'https://facebook.com'},
        {'name': 'Twitter', 'link': 'https://twitter.com'},
    ]
    table = ui.table(columns=columns, rows=rows, row_key='name')
    table.add_slot('body-cell-link', '''
        <q-td :props="props">
            <a :href="props.value">{{ props.value }}</a>
        </q-td>
    ''')        # body-cell-{name}, props.row.{name}, props.value 등등 사용하기

tables = [table1, table2, table3, table4, table5, table6, table7]
for i in range(0, len(tables), 3):
    ui.separator()
    with ui.row(align_items='stretch'):
        for table in tables[i:i+3]:
            with ui.card(align_items='center'):
                table()

    

ui.run()