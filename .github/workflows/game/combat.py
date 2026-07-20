# combat.py

"""
Боевая система ILTA RPG
Игрок против мобов
"""


import random

from data.monsters import get_monster
from data.loot import monster_drop



def calculate_damage(attack, defense):
    """
    Расчёт урона
    """

    damage = attack - defense


    if damage < 1:
        damage = 1


    # критический удар

    critical = random.randint(1,100)


    if critical <= 10:

        damage *= 2

        return damage, True



    return damage, False





def start_battle(player, monster_name):
    """
    Начало боя
    """


    monster = get_monster(monster_name)


    if not monster:

        return {
            "success": False,
            "message": "Монстр не найден."
        }



    player_hp = player["health"]

    monster_hp = monster["stats"]["health"]



    battle_log = []



    while player_hp > 0 and monster_hp > 0:


        # ход игрока

        damage, critical = calculate_damage(

            player["attack"],

            monster["stats"]["defense"]

        )


        monster_hp -= damage


        battle_log.append(

            f"Вы нанесли {damage} урона."

        )


        if critical:

            battle_log.append(
                "Критический удар!"
            )



        if monster_hp <= 0:
            break



        # ход монстра


        damage, critical = calculate_damage(

            monster["stats"]["attack"],

            player["defense"]

        )


        player_hp -= damage


        battle_log.append(

            f"{monster['name']} нанёс {damage} урона."

        )



    # победа

    if player_hp > 0:


        reward = monster["reward"]


        loot = monster_drop(
            monster["type"]
        )


        return {

            "success": True,

            "result": "win",

            "monster": monster["name"],

            "experience":
            reward["experience"],

            "gold":
            reward["gold"],

            "loot":
            loot,

            "log":
            battle_log

        }



    # поражение


    return {

        "success": True,

        "result": "lose",

        "monster": monster["name"],

        "log": battle_log

      }
