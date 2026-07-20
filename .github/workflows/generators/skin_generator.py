# skin_generator.py

"""
Генератор артов чемпионов и скинов ILTA RPG
"""

import os
import json
import requests


CHAMPIONS_FILE = "data/champions.json"


BASE_URL = (
    "https://raw.communitydragon.org/"
    "latest/plugins/"
    "rcp-be-lol-game-data/"
    "global/default/assets/characters/"
)



def create_folders():

    folders = [

        "assets/champions"

    ]

    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )





def load_champions():

    if not os.path.exists(
        CHAMPIONS_FILE
    ):

        print(
            "Нет файла champions.json"
        )

        return {}


    with open(
        CHAMPIONS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)






def download_image(
        url,
        path
):

    if os.path.exists(path):

        return


    try:

        response = requests.get(
            url,
            timeout=15
        )


        if response.status_code == 200:

            with open(
                path,
                "wb"
            ) as file:

                file.write(
                    response.content
                )


            print(
                "Скачано:",
                path
            )


        else:

            print(
                "Ошибка:",
                url
            )


    except Exception as error:

        print(
            "Ошибка загрузки:",
            error
        )






def generate_skins():


    create_folders()


    champions = load_champions()



    for name, data in champions.items():


        folder_name = name.lower()



        champion_folder = (

            f"assets/champions/{folder_name}"

        )


        os.makedirs(
            champion_folder,
            exist_ok=True
        )



        skins = data.get(
            "skins",
            []
        )



        for index, skin in enumerate(skins):


            image = skin.get(
                "image"
            )


            if not image:

                continue



            url = BASE_URL + image



            if index == 0:

                filename = "base.jpg"

            else:

                filename = (
                    f"skin{index}.jpg"
                )



            path = (

                f"{champion_folder}/"
                f"{filename}"

            )



            download_image(
                url,
                path
            )





if __name__ == "__main__":

    generate_skins()
