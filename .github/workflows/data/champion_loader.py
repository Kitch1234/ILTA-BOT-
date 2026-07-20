# champion_loader.py

"""
Загрузчик чемпионов ILTA RPG
"""

import json
import os


CHAMPIONS_FILE = "data/champions.json"



def load_champions():
    """
    Загрузка всех чемпионов из JSON
    """

    if not os.path.exists(CHAMPIONS_FILE):

        return {}


    with open(
        CHAMPIONS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)





def get_champion(name):
    """
    Получить одного чемпиона
    """

    champions = load_champions()


    return champions.get(name)





def get_all_champions():
    """
    Получить всех чемпионов
    """

    return load_champions()





def search_champions(text):
    """
    Поиск чемпионов
    """

    champions = load_champions()


    result = {}


    for name, data in champions.items():

        if text.lower() in name.lower():

            result[name] = data


    return result





def get_skins(champion_name):
    """
    Получить все скины чемпиона
    """

    champion = get_champion(
        champion_name
    )


    if champion:

        return champion.get(
            "skins",
            []
        )


    return []





def get_skin(
    champion_name,
    skin_name
):
    """
    Получить конкретный скин
    """

    skins = get_skins(
        champion_name
    )


    for skin in skins:

        if skin["name"] == skin_name:

            return skin


    return None
