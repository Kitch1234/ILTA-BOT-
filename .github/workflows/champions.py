# champions.py

"""
База чемпионов League of Legends
для RPG карточной системы ILTA BOT
"""


CHAMPIONS = {


    "Aatrox": {

        "name": "Атрокс",
        "title": "Клинок Даркинов",

        "region": [
            "Ноксус",
            "Шурима"
        ],

        "role": [
            "Fighter",
            "Darkin"
        ],


        "card_type": "champion",


        "stats": {

            "attack": 95,
            "health": 100,

            "defense": 70,

            "magic_resist": 50
        },


        "difficulty": 3,


        "abilities": [
            "Q",
            "W",
            "E",
            "R"
        ],


        "skins": [

            {
                "name": "Base Aatrox",
                "rarity": "Обычный",
                "image":
                "aatrox/skins/base/aatroxloadscreen.jpg"
            },


            {
                "name": "Mecha Aatrox",
                "rarity": "Легендарный",
                "image":
                "aatrox/skins/skin1/aatroxloadscreen.jpg"
            },


            {
                "name": "Odyssey Aatrox",
                "rarity": "Эпический",
                "image":
                "aatrox/skins/skin2/aatroxloadscreen.jpg"
            },


            {
                "name": "Prestige Blood Moon Aatrox",
                "rarity": "Престижный",
                "image":
                "aatrox/skins/skin3/aatroxloadscreen.jpg"
            }

        ]

    },



    "Ryze": {

        "name": "Райз",

        "title": "Мастер рун",


        "region": [
            "Рунтерра"
        ],


        "role": [
            "Mage"
        ],


        "card_type": "champion",


        "stats": {

            "attack": 55,

            "health": 70,

            "defense": 45,

            "magic_power": 100

        },


        "difficulty": 3,


        "abilities": [
            "Q",
            "W",
            "E",
            "R"
        ],


        "skins": [

            {
                "name": "Base Ryze",
                "rarity": "Обычный",
                "image":
                "ryze/skins/base/ryzeloadscreen.jpg"
            },


            {
                "name": "Zombie Ryze",
                "rarity": "Эпический",
                "image":
                "ryze/skins/skin3/ryzeloadscreen.jpg"
            },


            {
                "name": "Arcade Ryze",
                "rarity": "Эпический",
                "image":
                "ryze/skins/skin8/ryzeloadscreen.jpg"
            }

        ]

    }

}




def get_champion(name):
    """
    Получить чемпиона
    """

    return CHAMPIONS.get(name)



def get_all_champions():
    """
    Получить всех чемпионов
    """

    return CHAMPIONS



def get_champion_skins(name):
    """
    Получить скины чемпиона
    """

    champion = CHAMPIONS.get(name)


    if champion:
        return champion["skins"]


    return []
