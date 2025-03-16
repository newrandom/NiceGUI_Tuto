from nicegui import ui
from FunctionCollection import FunctionClass

fc = FunctionClass()

@ui.page('/actors_film/{actor_id}')
def actors_film(actor_id:int):
    # query and db
    query = f"""
        select c.first_name, a.film_id, a.title, a.description, a.release_year, d.name as language, 
        a.length , a.rating
        from film a
        join film_actor b on a.film_id = b.film_id 
        join actor c on b.actor_id = c.actor_id
        join public.language d on a.language_id = d.language_id 
        where c.actor_id = '{actor_id}'
    """
    data = fc.loadData(query)

    # data columns init
    columnDef = {
        
    }
    # ui
    ui.label(f"{data.loc[0]['first_name']} 배우가 출연한 영화 목록").style('font-size: 30px')
    dataTable = ui.aggrid.from_pandas(data)


    ui.button("뒤로가기", on_click=lambda:ui.navigate.to(f"/detail/{actor_id}"))