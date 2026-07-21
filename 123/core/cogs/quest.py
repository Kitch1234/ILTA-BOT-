import discord
from discord.ext import commands

from core.player import create_player, get_player
from database.quest import get_quests


class Quest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="quests",
        description="Посмотреть доступные квесты"
    )
    async def quests(
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

        quests = await get_quests(
            player["region"]
        )

        if not quests:

            await interaction.response.send_message(
                "📜 В этом регионе пока нет заданий."
            )
            return


        embed = discord.Embed(
            title="📜 Доступные квесты",
            color=discord.Color.orange()
        )


        for quest in quests:

            embed.add_field(
                name=f"#{quest['id']} {quest['name']}",
                value=(
                    f"{quest['description']}\n\n"
                    f"💰 {quest['reward_coins']} монет\n"
                    f"⭐ {quest['reward_xp']} XP"
                ),
                inline=False
            )


        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Quest(bot))
