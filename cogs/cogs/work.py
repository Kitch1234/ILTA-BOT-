import discord
from discord.ext import commands
import random


class Work(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="work",
        description="Выполнить работу и получить награду"
    )
    async def work(self, interaction: discord.Interaction):

        jobs = [
            "⛏️ Шахтёр",
            "🛠️ Кузнец",
            "📦 Торговец",
            "🌾 Фермер",
            "🧭 Исследователь"
        ]

        job = random.choice(jobs)
        money = random.randint(50, 200)
        exp = random.randint(10, 30)

        embed = discord.Embed(
            title="⚒️ Работа выполнена",
            color=discord.Color.green()
        )

        embed.add_field(
            name="Профессия",
            value=job,
            inline=False
        )

        embed.add_field(
            name="💰 Получено",
            value=f"{money} монет",
            inline=True
        )

        embed.add_field(
            name="✨ Опыт",
            value=f"{exp} XP",
            inline=True
        )

        embed.set_footer(
            text=f"Игрок: {interaction.user.name}"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Work(bot))
