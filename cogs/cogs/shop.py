import discord
from discord.ext import commands


class Shop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="shop",
        description="Открыть магазин"
    )
    async def shop(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🛒 Магазин",
            color=discord.Color.green()
        )

        embed.add_field(
            name="⚔️ Меч новичка",
            value="Цена: 500 🪙",
            inline=False
        )

        embed.add_field(
            name="🛡️ Деревянный щит",
            value="Цена: 300 🪙",
            inline=False
        )

        embed.add_field(
            name="🧪 Малое зелье лечения",
            value="Цена: 100 🪙",
            inline=False
        )

        embed.set_footer(
            text="Покупки скоро будут доступны"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Shop(bot))
