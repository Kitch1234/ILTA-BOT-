# abilities.py

"""
Способности чемпионов League of Legends
для RPG карточной системы ILTA BOT
"""


ABILITIES = {

    "Ryze": {

        "Q": {
            "name": "Перегрузка",
            "type": "magic_damage",
            "damage": 80,
            "mana_cost": 40,
            "cooldown": 4,
            "effect": "Наносит магический урон."
        },


        "W": {
            "name": "Руна потока",
            "type": "control",
            "damage": 30,
            "mana_cost": 50,
            "cooldown": 13,
            "effect": "Замедляет врага."
        },


        "E": {
            "name": "Заклинание потока",
            "type": "magic_damage",
            "damage": 60,
            "mana_cost": 40,
            "cooldown": 3,
            "effect": "Распространяет магию между врагами."
        },


        "R": {
            "name": "Пространственный разлом",
            "type": "ultimate",
            "damage": 0,
            "mana_cost": 100,
            "cooldown": 180,
            "effect": "Создаёт портал и перемещает союзников."
        }

    },


    "Aatrox": {

        "Q": {
            "name": "Темный клинок",
            "type": "physical_damage",
            "damage": 120,
            "mana_cost": 0,
            "cooldown": 14,
            "effect": "Мощный удар огромным мечом."
        },


        "W": {
            "name": "Адские цепи",
            "type": "control",
            "damage": 50,
            "mana_cost": 0,
            "cooldown": 20,
            "effect": "Замедляет и притягивает врага."
        },


        "E": {
            "name": "Рывок тени",
            "type": "mobility",
            "damage": 0,
            "mana_cost": 0,
            "cooldown": 9,
            "effect": "Перемещение и восстановление здоровья."
        },


        "R": {
            "name": "Истребитель богов",
            "type": "ultimate",
            "damage": 200,
            "mana_cost": 0,
            "cooldown": 120,
            "effect": "Переходит в демоническую форму."
        }

    }

}



def get_champion_abilities(champion):
    """
    Получить способности чемпиона
    """

    return ABILITIES.get(champion, {})



def get_ability(champion, key):
    """
    Получить конкретную способность
    """

    champion_data = ABILITIES.get(champion)

    if champion_data:
        return champion_data.get(key)

    return None
