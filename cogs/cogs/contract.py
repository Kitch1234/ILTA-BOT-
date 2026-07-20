import discord
from discord.ext import commands
import random


class Contract(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="contract",
        description="Посмотреть доступные контракты"
    )
    async def contract(self, interaction: discord.Interaction):

        contracts = [
            {
                "name": "⚔️ Охотник на монстров",
                "description": "Победить 10 монстров",
                "reward": "1000 🪙 + 200 XP"
            },
            {
                "name": "📦 Торговый контракт",
                "description": "Доставить товары",
                "reward": "700 🪙 + 150 XP"
            },
            {
                "name": "⛏️ Добыча ресурсов",
                "description": "Собрать 20 материалов",
                "reward": "500 🪙 + 100 XP"
            }
        ]

        contract = random.choice(contracts)

        embed = discord.Embed(
            title="📜 Контракт",
            color=discord.Color.dark_gold()
        )

        embed.add_field(
            name="Название",
            value=contract["name"],
            inline=False
        )

        embed.add_field(
            name="Задача",
            value=contract["description"],
            inline=False
        )

        embed.add_field(
            name="Награда",
            value=contract["reward"],
            inline=False
        )

        embed.set_footer(
            text=f"Игрок: {interaction.user.name}"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Contract(bot))
