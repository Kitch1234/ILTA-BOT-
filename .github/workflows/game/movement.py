# movement.py

"""
Система перемещения игрока по карте ILTA RPG
"""


import random

from data.maps import (
    WORLD_MAP,
    can_move
)



def move_player(player, target_location):
    """
    Перемещение игрока

    player:
    {
        "location": "Демасия",
        "level": 10
    }

    target_location:
    куда хочет пойти игрок
    """

    current_location = player["location"]
    level = player["level"]


    if not can_move(
        current_location,
        target_location,
        level
    ):
        return {
            "success": False,
            "message":
            "Нельзя переместиться туда."
        }



    player["location"] = target_location


    event = random_event(
        target_location
    )


    return {
        "success": True,

        "message":
        f"Вы прибыли в {target_location}",

        "event": event
    }





def random_event(location):
    """
    Случайное событие при переходе
    """


    region = WORLD_MAP.get(location)


    if not region:
        return None



    chance = random.randint(1,
