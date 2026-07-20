# world.py

"""
Мир ILTA RPG
"""


import json
import os





WORLD_FILE = (

    "data/world_map.json"

)





def load_world():

    """
    Загрузить карту мира
    """

    if not os.path.exists(
        WORLD_FILE
    ):

        return {}


    with open(

        WORLD_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)








def get_regions():

    """
    Получить все регионы
    """

    world = load_world()


    return world.get(

        "regions",

        []

    )








def get_region(

        region_id

):

    """
    Найти регион
    """


    regions = get_regions()



    for region in regions:


        if region["id"] == region_id:


            return region



    return None








def get_neighbors(

        region_id

):

    """
    Соседние регионы
    """


    region = get_region(

        region_id

    )



    if not region:

        return []



    return region.get(

        "neighbors",

        []

    )








def can_move(

        current_region,

        target_region

):

    """
    Проверка перехода
    """



    neighbors = get_neighbors(

        current_region

    )



    return target_region in neighbors








def get_monsters(

        region_id

):

    """
    Получить мобов региона
    """



    region = get_region(

        region_id

    )



    if not region:

        return []



    return region.get(

        "monsters",

        []

    )








def get_resources(

        region_id

):

    """
    Получить ресурсы
    """



    region = get_region(

        region_id

    )


    if not region:

        return []



    return region.get(

        "resources",

        []

    )








def get_events(

        region_id

):

    """
    Получить события региона
    """


    region = get_region(

        region_id

    )


    if not region:

        return []



    return region.get(

        "events",

        []

  )
