import discord
from discord.ext import commands


class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(
        name="profile",
        description="Посмотреть профиль"
    )
    async def profile(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            f"👤 Профиль игрока: {interaction.user.name}"
        )


async def setup(bot):
    await bot.add_cog(Profile(bot))
