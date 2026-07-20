# card_generator.py

"""
Генератор карт ILTA RPG
"""

from PIL import Image, ImageDraw, ImageFont
import os



CARD_SIZE = (600, 900)



FRAMES = {

    "Обычный":
        "assets/frames/common.png",

    "Эпический":
        "assets/frames/epic.png",

    "Легендарный":
        "assets/frames/legendary.png",

    "Мифический":
        "assets/frames/mythic.png",

    "Престижный":
        "assets/frames/prestige.png",

    "Предельный":
        "assets/frames/ultimate.png",

    "Чемпионский":
        "assets/frames/championship.png"

}



def get_font(size):

    font = "assets/fonts/arial.ttf"

    if os.path.exists(font):

        return ImageFont.truetype(
            font,
            size
        )

    return ImageFont.load_default()





def load_frame(rarity):

    path = FRAMES.get(
        rarity
    )


    if path and os.path.exists(path):

        frame = Image.open(
            path
        ).convert("RGBA")


        return frame.resize(
            CARD_SIZE
        )


    return None





def create_card(

        champion_name,

        image_path,

        rarity,

        attack,

        defense,

        health,

        description

):


    os.makedirs(
        "generated/cards",
        exist_ok=True
    )



    # основа карты

    card = Image.new(

        "RGBA",

        CARD_SIZE,

        (0,0,0,0)

    )



    # арт чемпиона

    image = Image.open(
        image_path
    ).convert("RGBA")



    image.thumbnail(
        (540,540)
    )



    card.paste(

        image,

        (
            30,
            120
        ),

        image

    )




    # рамка

    frame = load_frame(
        rarity
    )


    if frame:

        card.alpha_composite(
            frame
        )



    draw = ImageDraw.Draw(
        card
    )



    title_font = get_font(45)

    text_font = get_font(28)

    stat_font = get_font(40)



    # название

    draw.text(

        (40,40),

        champion_name,

        font=title_font,

        fill="white"

    )



    # описание

    draw.text(

        (40,650),

        description,

        font=text_font,

        fill="white"

    )



    # характеристики

    draw.text(

        (50,800),

        f"⚔ {attack}",

        font=stat_font,

        fill="white"

    )



    draw.text(

        (250,800),

        f"🛡 {defense}",

        font=stat_font,

        fill="white"

    )



    draw.text(

        (430,800),

        f"❤ {health}",

        font=stat_font,

        fill="white"

    )



    # сохранить

    filename = (

        f"generated/cards/"
        f"{champion_name}.png"

    )


    card.save(
        filename
    )


    return filename
