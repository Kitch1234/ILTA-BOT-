# leveling.py

"""
Система уровней ILTA RPG
"""


LEVELS = {

    1: {
        "xp_required": 0,
        "reward": "Начало пути"
    },

    2: {
        "xp_required": 100,
        "reward": "+5 здоровья"
    },

    3: {
        "xp_required": 250,
        "reward": "+5 атаки"
    },

    4: {
        "xp_required": 450,
        "reward": "+5 защиты"
    },

    5: {
        "xp_required": 700,
        "reward": "Открыт Пилтовер"
    },

    10: {
        "xp_required": 3000,
        "reward": "Открыты элитные мобы"
    },

    20: {
        "xp_required": 15000,
        "reward": "Открыт Ноксус"
    },

    30: {
        "xp_required": 50000,
        "reward": "Открыта Шурима"
    },

    50: {
        "xp_required": 200000,
        "reward": "Открыта Пустота"
    }

}



def get_level_from_xp(xp):
    """
    Определяет уровень по опыту
    """

    current_level = 1


    for level, data in LEVELS.items():

        if xp >= data["xp_required"]:

            current_level = level


    return current_level





def add_experience(player, amount):
    """
    Добавить опыт игроку
    """

    old_level = player["level"]


    player["experience"] += amount


    new_level = get_level_from_xp(
        player["experience"]
    )


    player["level"] = new_level



    result = {

        "xp_added": amount,

        "old_level": old_level,

        "new_level": new_level,

        "level_up": False

    }


    if new_level > old_level:

        result["level_up"] = True

        apply_level_bonus(
            player,
            new_level
        )


    return result





def apply_level_bonus(player, level):
    """
    Награды за уровень
    """

    player["health"] += 20


    if level % 3 == 0:

        player["attack"] += 5


    if level % 5 == 0:

        player["defense"] += 5





def get_next_level(xp):
    """
    Опыт до следующего уровня
    """

    for level, data in sorted(
        LEVELS.items()
    ):

        if xp < data["xp_required"]:

            return {

                "level": level,

                "need_xp":
                data["xp_required"] - xp

            }


    return None
