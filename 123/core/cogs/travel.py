import discord
from discord.ext import commands

from core.player import (
    create_player,
    get_player,
    change_region
)

from data.regions import REGIONS


class Travel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="travel",
        description="Путешествовать между регионами"
    )
    async def travel(
        self,
        interaction: discord.Interaction,
        region: str
    ):

        await create_player(
            interaction.user.id,
            interaction.user.name
        )

        player = await get_player(
            interaction.user.id
        )


        if region not in REGIONS:

            await interaction.response.send_message(
                "❌ Такого региона нет.\n"
                "Пример: `/travel demacia`"
            )
            return


        target = REGIONS[region]


        if player["level"] < target["level"]:

            await interaction.response.send_message(
                f"🔒 Для путешествия в {target['name']} "
                f"нужен {target['level']} уровень."
            )
            return


        await change_region(
            interaction.user.id,
            target["name"]
        )


        embed = discord.Embed(
            title="🗺️ Путешествие завершено",
            description=(
                f"Вы прибыли в **{target['name']}**\n\n"
                f"{target['description']}"
            ),
            color=discord.Color.gold()
        )

        embed.add_field(
            name="Требуемый уровень",
            value=str(target["level"])
        )


        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Travel(bot))
