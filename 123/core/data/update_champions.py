import requests
import json
import os


VERSION = "14.20.1"

OUTPUT = "data/champions.json"


def download_champions():

    print("⏳ Загружаю список чемпионов...")

    url = (
        f"https://ddragon.leagueoflegends.com/"
        f"cdn/{VERSION}/data/en_US/champion.json"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Ошибка загрузки чемпионов")
        return

    data = response.json()

    champions = data["data"]

    result = {}


    print(f"Найдено чемпионов: {len(champions)}")


    for champ_id, champ in champions.items():

        print(f"➡️ {champ['name']}")


        # Получаем детальную информацию
        detail_url = (
            f"https://ddragon.leagueoflegends.com/"
            f"cdn/{VERSION}/data/en_US/champion/"
            f"{champ_id}.json"
        )


        detail = requests.get(detail_url).json()

        champion_data = (
            detail["data"][champ_id]
        )


        skins = []


        for skin in champion_data["skins"]:

            skins.append(
                {
                    "name": skin["name"]
                    if skin["name"] != ""
                    else "Classic",

                    "id": int(
                        skin["num"]
                    )
                }
            )


        result[champ_id] = {

            "name": champ["name"],

            "title": champ["title"],

            "skins": skins
        }



    os.makedirs(
        "data",
        exist_ok=True
    )


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            ensure_ascii=False,
            indent=4
        )


    print("")
    print("✅ champions.json создан!")
    print(
        f"📁 Файл: {OUTPUT}"
    )



if __name__ == "__main__":
    download_champions()
