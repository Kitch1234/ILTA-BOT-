# rewards.py

"""
Система наград ILTA RPG
"""


import random

from data.loot import (
    get_random_rarity
)



def create_reward(
    experience=0,
    gold=0,
    item=None,
    card=None
):
    """
    Создание награды
    """

    return {

        "experience": experience,

        "gold": gold,

        "item": item,

        "card": card

    }





def battle_reward(monster):
    """
    Награда за победу над мобом
    """


    reward = monster["reward"]


    result = create_reward(

        experience=reward["experience"],

        gold=reward["gold"]

    )


    # шанс предмета

    if random.randint(1,100) <= 30:

        result["item"] = random.choice(

            monster["loot"]

        )


    # шанс карты

    if random.randint(1,100) <= 5:

        result["card"] = {

            "rarity":
            get_random_rarity()

        }


    return result





def quest_reward(
    quest_type
):
    """
    Награды за квесты
    """


    quests = {


        "daily": {

            "experience": 500,

            "gold": 200

        },


        "weekly": {

            "experience": 3000,

            "gold": 1500

        },


        "legendary": {

            "experience": 10000,

            "gold": 10000,

            "card": True

        }

    }



    return quests.get(
        quest_type,
        {}
    )





def event_reward(event):
    """
    Награды за события мира
    """

    events = {


        "treasure": {

            "gold": random.randint(
                500,
                2000
            ),

            "item": "Rare Essence"

        },


        "ancient_ruin": {

            "experience": 2000,

            "card": {

                "rarity":
                "Мифический"

            }

        },


        "boss": {

            "experience": 10000,

            "gold": 5000,

            "card": {

                "rarity":
                "Легендарный"

            }

        }

    }



    return events.get(
        event,
        {}
    )
