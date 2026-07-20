import discord
from discord.ext import commands
import random


class Daily(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="daily",
        description="Получить ежедневную награду"
    )
    async def daily(self, interaction: discord.Interaction):

        money = random.randint(300, 700)
        exp = random.randint(20, 50)

        embed = discord.Embed(
            title="🎁 Ежедневная награда",
            color=discord.Color.gold()
        )

        embed.add_field(
            name="💰 Монеты",
            value=f"{money} 🪙",
            inline=True
        )

        embed.add_field(
            name="✨ Опыт",
            value=f"{exp} XP",
            inline=True
        )

        embed.set_footer(
            text=f"Получил: {interaction.user.name}"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Daily(bot))
