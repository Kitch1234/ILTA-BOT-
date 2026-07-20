import discord
from discord.ext import commands


class Balance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="balance",
        description="Посмотреть баланс"
    )
    async def balance(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="💰 Баланс",
            color=discord.Color.gold()
        )

        embed.add_field(
            name="Монеты",
            value="0 🪙",
            inline=False
        )

        embed.add_field(
            name="Банк",
            value="0 🏦",
            inline=False
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Balance(bot))
