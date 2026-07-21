import discord
from discord.ext import commands
from discord import app_commands

from database import quest as quest_db


class QuestReward(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(
        name="quest_claim",
        description="Забрать награду за квест"
    )
    @app_commands.describe(
        quest_id="ID выполненного квеста"
    )
    async def quest_claim(
        self,
        interaction: discord.Interaction,
        quest_id: int
    ):

        user_id = interaction.user.id


        quest = await quest_db.get_quest(
            quest_id
        )


        if not quest:
            await interaction.response.send_message(
                "❌ Квест не найден."
            )
            return


        player_quests = await quest_db.get_player_quests(
            user_id
        )


        target = None

        for q in player_quests:

            if q["quest_id"] == quest_id:
                target = q
                break


        if not target:

            await interaction.response.send_message(
                "❌ Вы не брали этот квест."
            )
            return


        if not target["completed"]:

            await interaction.response.send_message(
                "❌ Квест ещё не выполнен."
            )
            return


        if target["claimed"]:

            await interaction.response.send_message(
                "❌ Награда уже получена."
            )
            return


        await quest_db.claim_quest(
            user_id,
            quest_id
        )


        await interaction.response.send_message(
            f"🎁 Награда получена!\n"
            f"💰 +{quest['reward_coins']} монет\n"
            f"⭐ +{quest['reward_xp']} опыта"
        )



async def setup(bot):

    await bot.add_cog(
        QuestReward(bot)
    )
