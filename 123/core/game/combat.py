import random


# ==========================
# Расчёт урона
# ==========================

def calculate_damage(
        attack,
        defense
):

    damage = attack - defense

    if damage < 1:
        damage = 1

    return damage



# ==========================
# Атака карты
# ==========================

def card_attack(
        card,
        monster
):

    damage = calculate_damage(
        card["attack"],
        monster["defense"]
    )


    monster["health"] -= damage


    return {
        "damage": damage,
        "monster_hp": monster["health"]
    }



# ==========================
# Атака монстра
# ==========================

def monster_attack(
        monster,
        card
):

    damage = calculate_damage(
        monster["attack"],
        card["defense"]
    )


    card["health"] -= damage


    return {
        "damage": damage,
        "card_hp": card["health"]
    }



# ==========================
# Проверка победы
# ==========================

def is_monster_dead(
        monster
):

    return monster["health"] <= 0



def is_card_dead(
        card
):

    return card["health"] <= 0
