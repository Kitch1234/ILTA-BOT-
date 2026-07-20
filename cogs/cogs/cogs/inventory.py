import discord
from discord.ext import commands


class Inventory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="inventory",
        description="Посмотреть свой инвентарь"
    )
    async def inventory(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🎒 Инвентарь",
            color=discord.Color.purple()
        )

        embed.add_field(
            name="⚔️ Оружие",
            value="Нет предметов",
            inline=False
        )

        embed.add_field(
            name="🛡️ Броня",
            value="Нет предметов",
            inline=False
        )

        embed.add_field(
            name="🧪 Расходники",
            value="Нет предметов",
            inline=False
        )

        embed.add_field(
            name="📦 Материалы",
            value="Нет предметов",
            inline=False
        )

        embed.set_footer(
            text=f"Игрок: {interaction.user.name}"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Inventory(bot))
