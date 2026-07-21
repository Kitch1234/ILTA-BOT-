import discord
from discord.ext import commands
from discord import app_commands

from database import decks as deck_db


class Deck(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Создание колоды

    @app_commands.command(
        name="deck_create",
        description="Создать новую колоду"
    )
    @app_commands.describe(
        name="Название колоды"
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
            f"🃏 Колода создана!\n"
            f"Название: **{name}**\n"
            f"ID: {deck_id}\n\n"
            f"Карт: 0/40"
        )



    # Список колод

    @app_commands.command(
        name="decks",
        description="Показать свои колоды"
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
                "🃏 У вас нет колод."
            )

            return


        text = "🃏 Ваши колоды:\n\n"


        for deck in decks:

            text += (
                f"#{deck['id']} "
                f"{deck['name']}\n"
            )


        await interaction.response.send_message(
            text
        )



async def setup(bot):

    await bot.add_cog(
        Deck(bot)
    )
