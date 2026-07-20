import discord
from discord.ext import commands

from core.player import create_player, get_player


class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="profile",
        description="Посмотреть профиль игрока"
    )
    async def profile(self, interaction: discord.Interaction):

        # создаём игрока, если его ещё нет
        await create_player(
            interaction.user.id,
            interaction.user.name
        )

        # получаем данные
        player = await get_player(
            interaction.user.id
        )

        if player is None:
            await interaction.response.send_message(
                "❌ Не удалось загрузить профиль"
            )
            return


        embed = discord.Embed(
            title="👤 Профиль игрока",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(
            url=interaction.user.display_avatar.url
        )

        embed.add_field(
            name="Игрок",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="⭐ Уровень",
            value=str(player["level"]),
            inline=True
        )

        embed.add_field(
            name="✨ Опыт",
            value=str(player["xp"]),
            inline=True
        )

        embed.add_field(
            name="💰 Монеты",
            value=str(player["coins"]),
            inline=True
        )

        embed.set_footer(
            text="RPG Universe"
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Profile(bot))
