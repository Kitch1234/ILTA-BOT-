# monsters.py

"""
Мобы League of Legends / Runeterra
для RPG карточной системы ILTA BOT
"""


MONSTERS = {


    # ===== Обычные =====


    "Voidling": {
        "name": "Порождение Пустоты",
        "type": "normal",

        "region": "Пустота",
        "level": 5,

        "stats": {
            "attack": 15,
            "health": 80,
            "defense": 5
        },

        "reward": {
            "experience": 50,
            "gold": 20
        },

        "loot": [
            "Void Crystal"
        ]
    },


    "Krug": {
        "name": "Круг",
        "type": "normal",

        "region": "Шурима",
        "level": 8,

        "stats": {
            "attack": 25,
            "health": 200,
            "defense": 15
        },

        "reward": {
            "experience": 100,
            "gold": 40
        },

        "loot": [
            "Stone Fragment"
        ]
    },


    "Raptor": {
        "name": "Хищник",
        "type": "normal",

        "region": "Шурима",
        "level": 10,

        "stats": {
            "attack": 35,
            "health": 250,
            "defense": 10
        },

        "reward": {
            "experience": 120,
            "gold": 50
        },

        "loot": [
            "Sharp Claw"
        ]
    },


    # ===== Элитные =====


    "Elite Voidborn": {
        "name": "Элитное создание Пустоты",
        "type": "elite",

        "region": "Пустота",
        "level": 25,

        "stats": {
            "attack": 120,
            "health": 1500,
            "defense": 60
        },

        "reward": {
            "experience": 800,
            "gold": 300
        },

        "loot": [
            "Void Crystal",
            "Rare Essence"
        ]
    },


    "Noxian Commander": {
        "name": "Командир Ноксуса",
        "type": "elite",

        "region": "Ноксус",
        "level": 30,

        "stats": {
            "attack": 150,
            "health": 2000,
            "defense": 80
        },

        "reward": {
            "experience": 1200,
            "gold": 500
        },

        "loot": [
            "Noxian Armor"
        ]
    },


    # ===== Боссы =====


    "Baron Nashor": {
        "name": "Барон Нашор",
        "type": "boss",

        "region": "Рунтерра",
        "level": 100,

        "stats": {
            "attack": 800,
            "health": 50000,
            "defense": 300
        },

        "abilities": [
            "Acid Spit",
            "Void Strike",
            "Baron Roar"
        ],

        "reward": {
            "experience": 10000,
            "gold": 5000
        },

        "loot": [
            "Baron Essence",
            "Mythic Chest"
        ]
    },


    "Elder Dragon": {
        "name": "Старший Дракон",
        "type": "boss",

        "region": "Рунтерра",
        "level": 120,

        "stats": {
            "attack": 1000,
            "health": 70000,
            "defense": 400
        },

        "abilities": [
            "Dragon Breath",
            "Infernal Fire",
            "Ancient Power"
        ],

        "reward": {
            "experience": 15000,
            "gold": 8000
        },

        "loot": [
            "Dragon Soul",
            "Legendary Chest"
        ]
    }

}



def get_monster(name):
    """
    Получить моба
    """

    return MONSTERS.get(name)



def get_monsters_by_region(region):
    """
    Получить мобов региона
    """

    return {
        name: monster
        for name, monster in MONSTERS.items()
        if monster["region"] == region
    }



def get_bosses():
    """
    Получить список боссов
    """

    return {
        name: monster
        for name, monster in MONSTERS.items()
        if monster["type"] == "boss"
  }
