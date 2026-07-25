# generate_all_cards.py

"""
Массовая генерация карт ILTA RPG
"""

import os
import json


from generators.card_generator import (
    create_card
)



CHAMPIONS_FILE = (
    "data/champions.json"
)



def load_champions():

    if not os.path.exists(
        CHAMPIONS_FILE
    ):

        print(
            "Нет champions.json"
        )

        return {}



    with open(

        CHAMPIONS_FILE,

        "r",

        encoding="utf-8"

    ) as file:

        return json.load(file)





def calculate_stats(
        champion
):
    """
    Временная генерация характеристик

    Потом заменим на реальные
    """

    return {

        "attack": 50,

        "defense": 50,

        "health": 100

    }





def generate_all():


    champions = load_champions()



    total = 0



    for name, data in champions.items():


        skins = data.get(
            "skins",
            []
        )



        stats = calculate_stats(
            data
        )



        for index, skin in enumerate(skins):


            rarity = skin.get(

                "rarity",

                "Обычный"

            )



            image = skin.get(
                "local_image"
            )



            if not image:


                if index == 0:

                    image = (

                    f"assets/champions/"
                    f"{name.lower()}/base.jpg"

                    )


                else:

                    image = (

                    f"assets/champions/"
                    f"{name.lower()}/"
                    f"skin{index}.jpg"

                    )




            if not os.path.exists(
                image
            ):

                print(
                    "Нет изображения:",
                    image
                )

                continue





            filename = create_card(

                champion_name=name,

                image_path=image,

                rarity=rarity,

                attack=stats["attack"],

                defense=stats["defense"],

                health=stats["health"],

                description=data.get(

                    "title",

                    "Чемпион Рунтерры"

                )

            )



            total += 1


            print(
                "Создана:",
                filename
            )





    print(
        f"Всего создано карт: {total}"
    )





if __name__ == "__main__":

    generate_all()
