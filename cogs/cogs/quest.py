import discord
from discord.ext import commands
import random


class Quest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="quest",
        description="Посмотреть доступные квесты"
    )
    async def quest(self, interaction: discord.Interaction):

        quests = [
            {
                "name": "🐺 Охота на волков",
                "reward": "500 🪙 + 100 XP"
            },
            {
                "name": "📦 Доставка груза",
                "reward": "300 🪙 + 50 XP"
            },
            {
                "name": "⛏️ Найти редкую руду",
                "reward": "800 🪙 + 150 XP"
            }
        ]

        quest = random.choice(quests)

        embed = discord.Embed(
            title="📜 Активный квест",
            color=discord.Color.orange()
        )

        embed.add_field(
            name="Задание",
            value=quest["name"],
            inline=False
        )

        embed.add_field(
            name="Награда",
            value=quest["reward"],
            inline=False
        )

        embed.set_footer(
            text=f"Игрок: {interaction.user.name}"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Quest(bot))
