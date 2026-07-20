import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def get_champion_skins(champion_name: str):
    version = "14.24.1"
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/ru_RU/champion/{champion_name}.json"
    try:
        data = requests.get(url).json()['data'][champion_name]
        return data['skins']
    except:
        return []

def get_skin_rarity(skin_id: int, skin_name: str):
    if "Prestige" in skin_name:
        return "Prestige"
    if "Ultimate" in skin_name:
        return "Ultimate"
    if "Mythic" in skin_name:
        return "Mythic"
    if "Championship" in skin_name or "Worlds" in skin_name:
        return "Championship"
    if skin_id >= 100:
        return "Legendary"
    elif skin_id >= 30:
        return "Epic"
    else:
        return "Common"

def create_lol_card(
    champion_name: str,
    skin_num: int = 0,
    attack: int = None,
    health: int = None,
    mana: int = 4,
    description: str = "Описание способности"
):
    version = "14.24.1"
    champ_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/ru_RU/champion/{champion_name}.json"
    
    try:
        data = requests.get(champ_url).json()['data'][champion_name]
    except:
        print("❌ Чемпион не найден")
        return None
    
    name = data['name']
    skins = data['skins']
    selected_skin = next((s for s in skins if s['num'] == skin_num), skins[0])
    skin_name = selected_skin['name']
    rarity = get_skin_rarity(selected_skin['num'], skin_name)
    
    # Рамка
    rarity_to_frame = {
        "Ultimate": "Ultimate", "Prestige": "Epic", "Mythic": "Epic",
        "Legendary": "ChampLevel1", "Championship": "Rare",
        "Epic": "Epic", "Common": "Common"
    }
    frame_type = rarity_to_frame.get(rarity, "Common")
    frame_url = f"https://raw.communitydragon.org/runeterra/assets/art/cards/cardframes/neutral/Bot_block_{frame_type}_frame.png"
    
    art_url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion_name}_{skin_num}.jpg"
    
    if attack is None: attack = 5 + (selected_skin['num'] % 6)
    if health is None: health = 5 + (selected_skin['num'] % 5)
    
    # Создание карточки
    frame_img = Image.open(BytesIO(requests.get(frame_url).content)).convert("RGBA")
    card = Image.new("RGBA", frame_img.size, (0, 0, 0, 0))
    card.paste(frame_img, (0, 0), frame_img)
    draw = ImageDraw.Draw(card)
    
    # Арта
    try:
        art = Image.open(BytesIO(requests.get(art_url).content)).convert("RGBA")
        art = art.resize((int(frame_img.width * 0.71), int(frame_img.height * 0.47)))
        card.paste(art, (int(frame_img.width * 0.145), int(frame_img.height * 0.165)), art)
    except:
        pass
    
    # Текст
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 46)
        stat_font = ImageFont.truetype("arialbd.ttf", 58)
        desc_font = ImageFont.truetype("arial.ttf", 26)
    except:
        title_font = stat_font = desc_font = ImageFont.load_default()
    
    draw.text((72, 62), name.upper(), fill="white", font=title_font, stroke_width=3, stroke_fill="black")
    draw.text((48, 38), str(mana), fill="white", font=stat_font, stroke_width=4, stroke_fill="black")
    draw.text((118, frame_img.height - 162), str(attack), fill="white", font=stat_font, stroke_width=4, stroke_fill="black")
    draw.text((frame_img.width - 172, frame_img.height - 162), str(health), fill="white", font=stat_font, stroke_width=4, stroke_fill="black")
    
    draw.text((80, 115), f"{rarity} • {skin_name}", fill="#FFD700", font=desc_font, stroke_width=2, stroke_fill="black")
    draw.multiline_text((82, frame_img.height - 285), description[:220], fill="white", font=desc_font, stroke_width=2, stroke_fill="black", spacing=5)
    
    filename = f"{name}_{skin_name.replace(' ', '_')}.png"
    card.save(filename)
    print(f"✅ Сохранено: {filename} | Редкость: {rarity}")
    return card


# Для теста
if __name__ == "__main__":
    create_lol_card("Yasuo", skin_num=0, description="Смерть — это только начало.")
