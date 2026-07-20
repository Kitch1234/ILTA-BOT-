import discord
from discord.ext import commands


class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="profile",
        description="Посмотреть профиль игрока"
    )
    async def profile(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="👤 Профиль игрока",
            description=f"{interaction.user.mention}",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="⭐ Уровень",
            value="1",
            inline=True
        )

        embed.add_field(
            name="✨ Опыт",
            value="0 / 100",
            inline=True
        )

        embed.add_field(
            name="💰 Монеты",
            value="0",
            inline=True
        )

        embed.add_field(
            name="🎒 Предметы",
            value="0",
            inline=True
        )

        embed.set_thumbnail(
            url=interaction.user.display_avatar.url
        )

        embed.set_footer(
            text="RPG Universe"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Profile(bot))
