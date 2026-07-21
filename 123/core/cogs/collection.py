import discord
from discord.ext import commands
from discord import app_commands

from database import collection as collection_db


class Collection(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    @app_commands.command(
        name="collection",
        description="Посмотреть коллекцию региона"
    )
    @app_commands.describe(
        region="Регион (Piltover, Noxus)"
    )
    async def collection(
        self,
        interaction: discord.Interaction,
        region: str
    ):


        cards = await collection_db.get_collection_by_region(

            interaction.user.id,
            region

        )


        if not cards:

            await interaction.response.send_message(
                f"🃏 В регионе **{region}** нет карт."
            )

            return



        text = f"🃏 Коллекция: {region}\n\n"


        for card in cards:

            text += (

                f"🃏 {card['champion']}\n"
                f"⭐ {card['rarity']}\n"
                f"⚔️ {card['attack']}\n"
                f"❤️ {card['health']}\n\n"

            )


        await interaction.response.send_message(
            text
        )



async def setup(bot):

    await bot.add_cog(
        Collection(bot)
    )
