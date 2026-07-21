import discord
from discord.ext import commands

from core.player import create_player, get_player
from data.regions import REGIONS


class Map(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="map",
        description="Посмотреть карту мира"
    )
    async def map(
        self,
        interaction: discord.Interaction
    ):

        await create_player(
            interaction.user.id,
            interaction.user.name
        )

        player = await get_player(
            interaction.user.id
        )

        current_region = player["region"]

        embed = discord.Embed(
            title="🗺️ Карта мира",
            color=discord.Color.green()
        )

        embed.add_field(
            name="📍 Текущий регион",
            value=current_region,
            inline=False
        )


        available = ""

        for key, region in REGIONS.items():

            available += (
                f"{region['name']}\n"
                f"🔹 Требуется уровень: {region['level']}\n\n"
            )


        embed.add_field(
            name="🌎 Регионы",
            value=available,
            inline=False
        )


        embed.set_footer(
            text="Quantum Universe"
        )


        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Map(bot))
