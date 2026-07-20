# maps.py

"""
Карта мира ILTA RPG
Регионы и перемещение игроков
"""


WORLD_MAP = {

    "Демасия": {

        "description": "Королевство чести и рыцарей.",

        "level_required": 1,

        "neighbors": [
            "Пилтовер",
            "Фрельйорд"
        ],

        "monsters": [
            "Forest Wolf",
            "Silverwing"
        ],

        "npcs": [
            "Garen",
            "Lux"
        ]

    },


    "Пилтовер": {

        "description": "Город технологий и изобретений.",

        "level_required": 5,

        "neighbors": [
            "Демасия",
            "Заун",
            "Иония"
        ],

        "monsters": [
            "Hextech Drone"
        ],

        "npcs": [
            "Jayce",
            "Heimerdinger"
        ]

    },


    "Заун": {

        "description": "Подземный город химии.",

        "level_required": 10,

        "neighbors": [
            "Пилтовер"
        ],

        "monsters": [
            "Chemtech Mutant",
            "Experiment"
        ],

        "npcs": [
            "Singed",
            "Ekko"
        ]

    },


    "Иония": {

        "description": "Земля духов и древней магии.",

        "level_required": 15,

        "neighbors": [
            "Пилтовер",
            "Ноксус"
        ],

        "monsters": [
            "Spirit Wolf",
            "Ionian Guard"
        ],

        "npcs": [
            "Yasuo",
            "Irelia"
        ]

    },


    "Ноксус": {

        "description": "Империя силы и войны.",

        "level_required": 20,

        "neighbors": [
            "Иония",
            "Шурима"
        ],

        "monsters": [
            "Noxian Soldier",
            "War Beast"
        ],

        "npcs": [
            "Darius",
            "Swain"
        ]

    },


    "Шурима": {

        "description": "Древняя империя песков.",

        "level_required": 30,

        "neighbors": [
            "Ноксус",
            "Пустота"
        ],

        "monsters": [
            "Sand Wraith",
            "Krug"
        ],

        "npcs": [
            "Azir",
            "Nasus"
        ]

    },


    "Пустота": {

        "description": "Измерение неизвестной силы.",

        "level_required": 50,

        "neighbors": [
            "Шурима"
        ],

        "monsters": [
            "Voidling",
            "Voidborn"
        ],

        "npcs": [
            "Kai'Sa"
        ]

    },


    "Фрельйорд": {

        "description": "Земля льда и древних племён.",

        "level_required": 10,

        "neighbors": [
            "Демасия"
        ],

        "monsters": [
            "Ice Wolf",
            "Yeti"
        ],

        "npcs": [
            "Ashe",
            "Braum"
        ]

    }

}



def get_location(name):
    """
    Получить регион
    """

    return WORLD_MAP.get(name)



def can_move(current, target, level):
    """
    Проверка перемещения
    """

    location = WORLD_MAP.get(current)

    if not location:
        return False


    if target not in location["neighbors"]:
        return False


    if level < WORLD_MAP[target]["level_required"]:
        return False


    return True
