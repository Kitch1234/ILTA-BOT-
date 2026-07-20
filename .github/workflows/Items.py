# items.py

"""
Предметы League of Legends
для RPG карточной системы ILTA BOT
"""


ITEMS = {


    # Оружие

    "Infinity Edge": {
        "name": "Грань Бесконечности",
        "type": "weapon",
        "rarity": "Легендарный",

        "stats": {
            "attack": 25,
            "critical": 20
        },

        "effect": "Увеличивает критический урон."
    },


    "Bloodthirster": {
        "name": "Кровопийца",
        "type": "weapon",
        "rarity": "Легендарный",

        "stats": {
            "attack": 20,
            "lifesteal": 15
        },

        "effect": "Восстанавливает здоровье от нанесённого урона."
    },


    "Rabadon": {
        "name": "Смертельная Шляпа Рабадона",
        "type": "magic",

        "rarity": "Легендарный",

        "stats": {
            "ability_power": 35
        },

        "effect": "Сильно увеличивает силу заклинаний."
    },



    # Защита


    "Guardian Angel": {
        "name": "Ангел-хранитель",
        "type": "armor",

        "rarity": "Легендарный",

        "stats": {
            "attack": 10,
            "armor": 25
        },

        "effect": "Возрождает владельца после смерти."
    },


    "Warmog": {
        "name": "Броня Вармога",
        "type": "armor",

        "rarity": "Эпический",

        "stats": {
            "health": 500
        },

        "effect": "Увеличивает максимальное здоровье."
    },



    # Артефакты


    "World Rune": {
        "name": "Мировая Руна",
        "type": "artifact",

        "rarity": "Мифический",

        "stats": {
            "magic": 40,
            "power": 20
        },

        "effect": "Древняя сила Рунтерры."
    },


    "Darkin Blade": {
        "name": "Клинок Даркина",
        "type": "artifact",

        "rarity": "Престижный",

        "stats": {
            "attack": 50,
            "lifesteal": 20
        },

        "effect": "Оружие древнего Даркина."
    }

}



def get_item(name):
    """
    Получить предмет
    """

    return ITEMS.get(name)



def get_items_by_type(item_type):
    """
    Получить предметы категории
    """

    return {
        name: item
        for name, item in ITEMS.items()
        if item["type"] == item_type
    }
