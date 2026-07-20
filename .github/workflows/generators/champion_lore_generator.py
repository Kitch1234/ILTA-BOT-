# champion_lore_generator.py

"""
Генератор данных коллекции чемпионов ILTA RPG
"""


import json
import os



CHAMPIONS_FILE = (
    "data/champions.json"
)


OUTPUT_FOLDER = (
    "data/champions"
)





def create_folder():

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
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







def create_lore_data(
        name,
        data
):


    return {


        "name":

        data.get(
            "name",
            name
        ),



        "title":

        data.get(
            "title",
            "Неизвестный чемпион"
        ),



        "region":

        data.get(

            "region",

            [

                "Рунтерра"

            ]

        ),



        "role":

        data.get(

            "role",

            [

                "Чемпион"

            ]

        ),



        "description":

        "Описание персонажа будет добавлено.",



        "lore":

        "История персонажа будет добавлена.",



        "quotes":

        [

            "Реплики будут добавлены."

        ],



        "abilities":

        {


            "Q":

            "Способность Q",


            "W":

            "Способность W",


            "E":

            "Способность E",


            "R":

            "Способность R"


        },



        "skins_count":

        len(

            data.get(
                "skins",
                []
            )

        )

    }







def generate():


    create_folder()



    champions = load_champions()



    count = 0



    for name, data in champions.items():


        lore = create_lore_data(

            name,

            data

        )



        filename = (

            f"{OUTPUT_FOLDER}/"
            f"{name.lower()}.json"

        )



        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                lore,

                file,

                ensure_ascii=False,

                indent=4

            )


        count += 1



        print(

            "Создан:",

            filename

        )





    print(

        f"Всего создано: {count}"

    )







if __name__ == "__main__":

    generate()
