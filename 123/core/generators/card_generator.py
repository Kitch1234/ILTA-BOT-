from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os


CARD_WIDTH = 744
CARD_HEIGHT = 1039


def get_font(size):
    try:
        return ImageFont.truetype(
            "assets/font.ttf",
            size
        )
    except:
        return ImageFont.load_default()



def create_card(
    champion,
    skin,
    rarity,
    attack,
    health,
    defense,
    image_url
):

    # скачиваем арт
    response = requests.get(image_url)

    art = Image.open(
        BytesIO(response.content)
    ).convert("RGBA")


    # размер карты
    art = art.resize(
        (CARD_WIDTH, CARD_HEIGHT)
    )


    card = art.copy()


    draw = ImageDraw.Draw(card)


    # затемнение снизу для текста
    overlay = Image.new(
        "RGBA",
        card.size,
        (0,0,0,0)
    )

    overlay_draw = ImageDraw.Draw(
        overlay
    )

    overlay_draw.rectangle(
        (0,750,CARD_WIDTH,CARD_HEIGHT),
        fill=(0,0,0,170)
    )


    card = Image.alpha_composite(
        card,
        overlay
    )


    draw = ImageDraw.Draw(card)


    title_font = get_font(55)
    text_font = get_font(38)



    # имя чемпиона
    draw.text(
        (40,760),
        champion,
        font=title_font,
        fill="white"
    )


    # скин
    draw.text(
        (40,830),
        skin,
        font=text_font,
        fill="white"
    )



    # характеристики

    draw.text(
        (50,930),
        f"⚔ {attack}",
        font=text_font,
        fill="white"
    )


    draw.text(
        (280,930),
        f"❤️ {health}",
        font=text_font,
        fill="white"
    )


    draw.text(
        (520,930),
        f"🛡 {defense}",
        font=text_font,
        fill="white"
    )



    # редкость

    draw.text(
        (40,40),
        rarity.upper(),
        font=text_font,
        fill="gold"
    )



    # сохранение

    os.makedirs(
        "cards",
        exist_ok=True
    )


    filename = (
        f"cards/"
        f"{champion}_{skin}.png"
    )


    card.convert(
        "RGB"
    ).save(
        filename
    )


    return filename
