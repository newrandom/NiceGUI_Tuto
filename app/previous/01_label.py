from nicegui import ui

# ui.label('hello world')
data = [
    {'name': '재선', 'age': 34, 'phone' : '010-3829-2451'},
    {'name':'test','age':15, 'phone':'010-1234-5678'},
    {'name':'test2','age':25, 'phone':'010-1234-5678'},
    {'name':'test3','age':35, 'phone':'010-1234-5678'},
]

ui.table(
    rows=data,
    columns=data,
    
)


ui.run(native=True)