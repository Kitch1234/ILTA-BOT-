# champions.py

import json
import os


CHAMPIONS_FILE = "data/champions.json"


def load_champions():
    """
    Загружает всех чемпионов из базы
    """

    if not os.path.exists(CHAMPIONS_FILE):
        return {}

    with open(CHAMPIONS_FILE, "r", encoding="utf-8") as file:
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



def search_champion(text):
    """
    Поиск чемпиона
    """

    champions = load_champions()

    result = {}

    for name, data in champions.items():

        if text.lower() in name.lower():
            result[name] = data

    return result
