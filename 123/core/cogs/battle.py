import discord
from discord.ext import commands
from discord import app_commands

from database import monsters
from game.quest_events import monster_killed


class Battle(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(
        name="battle",
        description="Сразиться с монстром"
    )
    async def battle(
        self,
        interaction: discord.Interaction
    ):

        user_id = interaction.user.id


        # Берём монстров стартового региона
        mobs = await monsters.get_monsters(
            "start"
        )


        if not mobs:

            await interaction.response.send_message(
                "❌ В этом регионе нет монстров."
            )

            return


        mob = mobs[0]


        player_damage = 15


        damage = player_damage - mob["defense"]


        if damage < 1:
            damage = 1


        hits = mob["health"] // damage + 1


        await monster_killed(
            user_id
        )


        await interaction.response.send_message(
            f"⚔️ Вы победили!\n\n"
            f"🐺 Монстр: {mob['name']}\n"
            f"💥 Ударов нанесено: {hits}\n\n"
            f"💰 Золото: +{mob['reward_gold']}\n"
            f"⭐ Опыт: +{mob['reward_xp']}\n\n"
            f"📜 Прогресс квестов обновлён."
        )



async def setup(bot):

    await bot.add_cog(
        Battle(bot)
    )
