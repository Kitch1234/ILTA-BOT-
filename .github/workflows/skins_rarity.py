# skins_rarity.py

"""
Система редкости скинов League of Legends
для карточной RPG системы Discord бота
"""


SKIN_RARITY = {

    "Обычный": {
        "level": 1,
        "color": "#808080",
        "drop_chance": 50,
        "card_frame": "common",
        "multiplier": 1.0
    },

    "Эпический": {
        "level": 2,
        "color": "#8A2BE2",
        "drop_chance": 25,
        "card_frame": "epic",
        "multiplier": 1.5
    },

    "Легендарный": {
        "level": 3,
        "color": "#FF8C00",
        "drop_chance": 12,
        "card_frame": "legendary",
        "multiplier": 2.5
    },

    "Мифический": {
        "level": 4,
        "color": "#E91E63",
        "drop_chance": 7,
        "card_frame": "mythic",
        "multiplier": 4.0
    },

    "Престижный": {
        "level": 5,
        "color": "#FFD700",
        "drop_chance": 3,
        "card_frame": "prestige",
        "multiplier": 6.0
    },

    "Предельный": {
        "level": 6,
        "color": "#00FFFF",
        "drop_chance": 2,
        "card_frame": "ultimate",
        "multiplier": 10.0
    },

    "Чемпионский": {
        "level": 7,
        "color": "#FFFFFF",
        "drop_chance": 1,
        "card_frame": "championship",
        "multiplier": 15.0
    }

}


def get_rarity(name):
    """
    Получить данные редкости
    """

    return SKIN_RARITY.get(name)



def get_frame(name):
    """
    Получить рамку карты
    """

    rarity = SKIN_RARITY.get(name)

    if rarity:
        return rarity["card_frame"]

    return "common"



def get_multiplier(name):
    """
    Получить множитель стоимости карты
    """

    rarity = SKIN_RARITY.get(name)

    if rarity:
        return rarity["multiplier"]

    return 1.0
