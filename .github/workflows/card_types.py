# card_types.py

"""
Типы карт для League of Legends RPG Discord Bot
"""


CARD_TYPES = {

    "champion": {
        "name": "Чемпион",
        "description": "Главные герои League of Legends.",
        "icon": "⚔️",

        "stats": [
            "attack",
            "health",
            "abilities"
        ],

        "can_level_up": True,

        "rarity_bonus": True
    },


    "spell": {
        "name": "Заклинание",
        "description": "Магические способности и умения.",
        "icon": "✨",

        "stats": [
            "mana_cost",
            "damage",
            "effect"
        ],

        "can_level_up": False,

        "rarity_bonus": True
    },


    "item": {
        "name": "Предмет",
        "description": "Оружие, броня и артефакты.",
        "icon": "🛡️",

        "stats": [
            "attack",
            "defense",
            "special_effect"
        ],

        "can_level_up": True,

        "rarity_bonus": True
    },


    "monster": {
        "name": "Монстр",
        "description": "Существа Рунтерры.",
        "icon": "👹",

        "stats": [
            "attack",
            "health",
            "loot"
        ],

        "can_level_up": True,

        "rarity_bonus": False
    },


    "boss": {
        "name": "Босс",
        "description": "Уникальные сильные противники.",
        "icon": "👑",

        "stats": [
            "attack",
            "health",
            "skills",
            "rewards"
        ],

        "can_level_up": True,

        "rarity_bonus": True
    },


    "region": {
        "name": "Регион",
        "description": "Карты регионов Рунтерры.",
        "icon": "🌎",

        "stats": [
            "bonus",
            "effects"
        ],

        "can_level_up": False,

        "rarity_bonus": False
    },


    "skin": {
        "name": "Образ",
        "description": "Альтернативные облики чемпионов.",
        "icon": "🎭",

        "stats": [
            "visual",
            "rarity",
            "value"
       
