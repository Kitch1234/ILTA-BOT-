import discord
from discord.ext import commands
from discord import app_commands

from database import decks as deck_db
from database import deck_slots


class Deck(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    # ==========================
    # Создать колоду
    # ==========================

    @app_commands.command(
        name="deck_create",
        description="Создать боевой отряд из 3 карт"
    )
    @app_commands.describe(
        name="Название отряда"
    )
    async def deck_create(
        self,
        interaction: discord.Interaction,
        name: str
    ):


        deck_id = await deck_db.create_deck(
            interaction.user.id,
            name
        )


        await interaction.response.send_message(

            f"🃏 Отряд создан!\n"
            f"Название: **{name}**\n"
            f"ID: {deck_id}\n\n"
            f"1️⃣ Пусто\n"
            f"2️⃣ Пусто\n"
            f"3️⃣ Пусто"

        )



    # ==========================
    # Список отрядов
    # ==========================

    @app_commands.command(
        name="decks",
        description="Показать свои отряды"
    )
    async def decks(
        self,
        interaction: discord.Interaction
    ):


        decks = await deck_db.get_decks(
            interaction.user.id
        )


        if not decks:

            await interaction.response.send_message(
                "🃏 У вас нет отрядов."
            )

            return



        text = "🃏 Ваши отряды:\n\n"


        for deck in decks:

            text += (
                f"#{deck['id']} — "
                f"{deck['name']}\n"
            )


        await interaction.response.send_message(
            text
        )



    # ==========================
    # Добавить карту в слот
    # ==========================

    @app_commands.command(
        name="deck_add",
        description="Добавить карту в слот отряда"
    )
    @app_commands.describe(
        deck_id="ID отряда",
        card_id="ID карты",
        slot="Слот 1-3"
    )
    async def deck_add(
        self,
        interaction: discord.Interaction,
        deck_id: int,
        card_id: int,
        slot: int
    ):


        if slot not in [1, 2, 3]:

            await interaction.response.send_message(
                "❌ Слот может быть только 1, 2 или 3"
            )

            return



        try:

            await deck_slots.add_card_slot(

                interaction.user.id,
                deck_id,
                card_id,
                slot

            )


            await interaction.response.send_message(

                f"✅ Карта #{card_id} "
                f"добавлена в слот {slot}"

            )


        except Exception as e:

            await interaction.response.send_message(

                f"❌ Ошибка:\n{e}"

            )



    # ==========================
    # Посмотреть отряд
    # ==========================

    @app_commands.command(
        name="deck_view",
        description="Посмотреть боевой отряд"
    )
    @app_commands.describe(
        deck_id="ID отряда"
    )
    async def deck_view(
        self,
        interaction: discord.Interaction,
        deck_id: int
    ):


        cards = await deck_slots.get_deck_slots(
            deck_id
        )


        text = f"🃏 Отряд #{deck_id}\n\n"


        slots = {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣"
        }


        used = []


        for card in cards:

            used.append(card["slot"])


            text += (

                f"{slots[card['slot']]} "
                f"**{card['champion']}**\n"
                f"⭐ {card['rarity']}\n"
                f"⚔️ {card['attack']}\n"
                f"❤️ {card['health']}\n\n"

            )



        for slot in [1,2,3]:

            if slot not in used:

                text += (
                    f"{slots[slot]} Пусто\n\n"
                )



        await interaction.response.send_message(
            text
        )



async def setup(bot):

    await bot.add_cog(
        Deck(bot)
    )
