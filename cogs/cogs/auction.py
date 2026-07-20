import discord
from discord.ext import commands


class Auction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="auction",
        description="Открыть аукцион"
    )
    async def auction(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🏛️ Аукцион",
            color=discord.Color.gold()
        )

        embed.add_field(
            name="⚔️ Меч рыцаря",
            value="Текущая ставка: 1000 🪙\nПродавец: Игрок",
            inline=False
        )

        embed.add_field(
            name="💎 Редкий кристалл",
            value="Текущая ставка: 2500 🪙\nПродавец: Игрок",
            inline=False
        )

        embed.add_field(
            name="🧪 Эликсир здоровья",
            value="Текущая ставка: 500 🪙\nПродавец: Игрок",
            inline=False
        )

        embed.set_footer(
            text="Настоящий аукцион будет подключён к базе данных"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Auction(bot))
