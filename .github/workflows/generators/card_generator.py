# card_generator.py

"""
Генератор игровых карт ILTA RPG
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



def load_font(size):

    return ImageFont.truetype(
        "assets/fonts/arial.ttf",
        size
    )





def create_card(
        champion,
        image_path,
        rarity,
        attack,
        health,
        description
):

    """
    Создание карты
    """

    # фон карты

    card = Image.new(
        "RGBA",
        CARD_SIZE,
        (0,0,0,0)
    )


    draw = ImageDraw.Draw(card)



    # арт чемпиона

    champion_img = Image.open(
        image_path
    ).convert("RGBA")


    champion_img.thumbnail(
        (500,500)
    )


    card.paste(
        champion_img,
        (50,120),
        champion_img
    )



    # рамка

    frame_path = FRAMES.get(
        rarity
    )


    if frame_path and os.path.exists(frame_path):

        frame = Image.open(
            frame_path
        ).convert("RGBA")


        frame = frame.resize(
            CARD_SIZE
        )


        card.alpha_composite(
            frame
        )



    # текст

    title_font = load_font(45)

    text_font = load_font(28)



    draw.text(
        (50,40),
        champion,
        font=title_font,
        fill="white"
    )



    draw.text(
        (50,650),
        description,
        font=text_font,
        fill="white"
    )



    # атака

    draw.text(
        (80,780),
        f"⚔ {attack}",
        font=title_font,
        fill="white"
    )



    # здоровье

    draw.text(
        (400,780),
        f"❤ {health}",
        font=title_font,
        fill="white"
    )



    # сохранить

    filename = (
        f"generated/{champion}.png"
    )


    os.makedirs(
        "generated",
        exist_ok=True
    )


    card.save(
        filename
    )


    return filename
