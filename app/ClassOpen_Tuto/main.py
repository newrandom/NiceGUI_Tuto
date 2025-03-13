from nicegui import ui
from def_collection import FunctionCollection


# def on_click():
#     ui.notify('button was pressed')

# def on_change(name:str, id:int):
#     # ui.notify(f'checkbox was changed to {ui.get_value(name)}')
#     ui.notify(f'{name} change this checkbox {id}')
fc = FunctionCollection()

ui.label('Hello NiceGUI!')
# ui.button('BUTTON', on_click=lambda:ui.notify('button was pressed'))
# ui.button('BUTTON', on_click=fc.on_click)
# ui.button('click', on_click=lambda :fc().on_click())
ui.button('click me', on_click=fc.on_click)
# ui.checkbox('CHECKBOX', on_change=lambda:ui.notify('checkbox was changed'))
# ui.checkbox('checkbox', on_change=lambda:on_change('newrandom',33))

ui.button('when you click me, print on console', on_click=lambda:print('button was pressed'))


ui.run()


# numbers = [1,2,3,4,5,6]
# filter(lambda n:n % 2 == 0, numbers)