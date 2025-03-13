from nicegui import ui, html

@ui.page("/")
def home():
    ui.label("Welcome to the Home Page!")
    # ui.button("Go to About Page", on_click=lambda:ui.navigate("/about"))
    ui.button("Go to About Page", on_click=lambda:ui.navigate.to("/about"))
    ui.button("Go to Counter Page", on_click=lambda:ui.navigate.to("/counter"))

# About 페이지
@ui.page("/about")
def about():
    ui.label("Welcome to the About Page!")
    # ui.button("Back to Home", on_click=lambda:ui.navigate.back())    
    ui.button("Back to Home", on_click=lambda:ui.navigate.to("/"))

@ui.page("/counter")
def counter():
    # count = ui.state(0)
    # ui.label(f"Counter: {count}")
    # ui.button("Increment", on_click=lambda:count.set(count.get() + 1))    
    # count = ui.state(0)
    ui.label("Counter Page")
    # ui.label(f"Counter: {count.count(0)}")
    ui.button("click", on_click = None)
    html.hr()
    html.em('This is italic.').tooltip('Nice!')

@ui.page("/test")
def test():
    with html.section().style('font-size: 120%'):
        html.strong('This is bold.').classes('cursor-pointer').on('click', lambda: ui.notify('Bold!'))
        html.hr()
        html.em('This is italic.').on('click',lambda:ui.notify('Italic')).tooltip('Nice!')
    with ui.row():
        html.img().props('src=https://placehold.co/60')
        html.img(src='https://placehold.co/60')    

@ui.page("/test2")
def test2():
    columns = [
        {'name':'name', 'label':'Name', 'field':'name','required':True, 'align':'left'},
        {'name':'age', 'label':'Age', 'field':'age', 'sortable':True},
    ]
    rows = [
        {'name':'Alice', 'age':18},
    ]

    ui.table(columns=columns,rows=rows)


# UI Run
ui.run()        

