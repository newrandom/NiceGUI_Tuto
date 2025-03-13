from nicegui import ui
class FunctionCollection():
    # def __init__(self):
    #     self.funcs = []
    # def __init__(self):
    #     pass

    def on_click(self) -> None:
        ui.notify('button was pressed Man!!')

    def on_change(self, name:str, id:int) -> None:
        ui.notify(f'{name} change this checkbox {id}')