# loot.py

"""
Система добычи (Loot)
для RPG карточной системы ILTA BOT
"""


import random



# Шансы выпадения редкости

LOOT_RARITY = {

    "Обычный": {
        "chance": 60,
        "color": "#808080"
    },

    "Эпический": {
        "chance": 25,
        "color": "#9B59B6"
    },

    "Легендарный": {
        "chance": 10,
        "color": "#F39C12"
    },

    "Мифический": {
        "chance": 4,
        "color": "#E91E63"
    },

    "Престижный": {
        "chance": 0.8,
        "color": "#FFD700"
    },

    "Предельный": {
        "chance": 0.15,
        "color": "#00FFFF"
    },

    "Чемпионский": {
        "chance": 0.05,
        "color": "#FFFFFF"
    }

}




# Типы наград

LOOT_TABLE = {


    "normal_monster": {

        "gold": {
            "min": 10,
            "max": 50
        },

        "items": [
            "Stone Fragment",
            "Sharp Claw"
        ],

        "cards": {
            "chance": 5
        }

    },



    "elite_monster": {

        "gold": {
            "min": 100,
            "max": 500
        },

        "items": [
            "Rare Essence",
            "Noxian Armor"
        ],

        "cards": {
            "chance": 20
        }

    },



    "boss": {

        "gold": {
            "min": 1000,
            "max": 5000
        },

        "items": [
            "Mythic Chest",
            "Legendary Essence"
        ],

        "cards": {
            "chance": 50
        }

    }

}




# Сундуки

CHESTS = {


    "Bronze Chest": {

        "rarity": [
            "Обычный",
            "Эпический"
        ],

        "cost": 500

    },


    "Silver Chest": {

        "rarity": [
            "Эпический",
            "Легендарный"
        ],

        "cost": 2000

    },


    "Golden Chest": {

        "rarity": [
            "Легендарный",
            "Мифический"
        ],

        "cost": 5000

    },


    "Mythic Chest": {

        "rarity": [
            "Мифический",
            "Престижный",
            "Предельный"
        ],

        "cost": 25000

    }

}




def get_random_rarity():
    """
    Получить случайную редкость
    """

    rarities = []

    for name, data in LOOT_RARITY.items():

        rarities.extend(
            [name] * int(data["chance"] * 10)
        )


    return random.choice(rarities)




def open_chest(chest_name):
    """
    Открытие сундука
    """

    chest = CHESTS.get(chest_name)

    if not chest:
        return None


    rarity = random.choice(
        chest["rarity"]
    )


    return {
        "chest": chest_name,
        "rarity": rarity
    }




def monster_drop(monster_type):
    """
    Награда за убийство моба
    """

    loot = LOOT_TABLE.get(monster_type)


    if not loot:
        return None


    gold = random.randint(
        loot["gold"]["min"],
        loot["gold"]["max"]
    )


    card_drop = random.randint(1,100)


    return {

        "gold": gold,

        "card_drop":
            card_drop <= loot["cards"]["chance"],

        "items":
            random.choice(loot["items"])

  }
