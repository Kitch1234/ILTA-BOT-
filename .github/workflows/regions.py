# regions.py

"""
Регионы League of Legends / Runeterra
для карточной RPG системы Discord бота
"""


REGIONS = {

    "Демасия": {
        "color": "#FFFFFF",
        "description": "Королевство чести, порядка и воинов.",
        "bonus": {
            "armor": 10,
            "health": 5
        }
    },


    "Ноксус": {
        "color": "#8B0000",
        "description": "Империя силы, войны и амбиций.",
        "bonus": {
            "attack": 10,
            "critical": 5
        }
    },


    "Иония": {
        "color": "#FF69B4",
        "description": "Земля духов, гармонии и древних боевых искусств.",
        "bonus": {
            "speed": 10,
            "dodge": 5
        }
    },


    "Пилтовер": {
        "color": "#FFD700",
        "description": "Город прогресса и технологий.",
        "bonus": {
            "magic_power": 10,
            "craft": 5
        }
    },


    "Заун": {
        "color": "#00FF00",
        "description": "Подземный город химии и экспериментов.",
        "bonus": {
            "poison": 10,
            "alchemy": 10
        }
    },


    "Фрельйорд": {
        "color": "#00BFFF",
        "description": "Холодный край льда и древних племён.",
        "bonus": {
            "health": 15,
            "resistance": 10
        }
    },


    "Шурима": {
        "color": "#DAA520",
        "description": "Древняя империя песков.",
        "bonus": {
            "sun_power": 10,
            "attack": 5
        }
    },


    "Теневые острова": {
        "color": "#800080",
        "description": "Земля проклятых душ и нежити.",
        "bonus": {
            "life_steal": 10,
            "dark_magic": 15
        }
    },


    "Пустота": {
        "color": "#9400D3",
        "description": "Неизведанное измерение разрушения.",
        "bonus": {
            "damage": 15,
            "mutation": 5
        }
    },


    "Бандл-Сити": {
        "color": "#FF1493",
        "description": "Дом йордлов и магических существ.",
        "bonus": {
            "luck": 10,
            "gold": 10
        }
    },


    "Рунтерра": {
        "color": "#808080",
        "description": "Общий мир, где пересекаются все силы.",
        "bonus": {
            "experience": 10
        }
    }

}



def get_region(name):
    """
    Получить данные региона
    """
    return REGIONS.get(name)



def get_region_bonus(name):
    """
    Получить бонус региона
    """
    region = REGIONS.get(name)

    if region:
        return region["bonus"]

    return {}
