# quest_manager.py

"""
Менеджер квестов ILTA RPG
"""


import json
import os

import discord

from discord.ext import commands


from database.quest_queries import (

    create_quest,

    get_player_quests,

    update_quest_progress,

    complete_quest

)





QUEST_FILE = (
    "data/quests.json"
)





def load_quests():

    if not os.path.exists(
        QUEST_FILE
    ):

        return {}


    with open(

        QUEST_FILE,

        "r",

        encoding="utf-8"

    ) as file:

        return json.load(file)






class QuestManager(commands.Cog):


    def __init__(self, bot):

        self.bot = bot






    @commands.slash_command(

        name="startquests",

        description="Получить начальные задания"

    )
    async def startquests(

        self,

        ctx

    ):


        pool = self.bot.db


        quests = load_quests()



        daily = quests.get(

            "daily",

            []

        )



        if not daily:

            await ctx.respond(

                "Нет доступных заданий."

            )

            return





        quest = daily[0]



        await create_quest(

            pool,

            ctx.author.id,

            quest["id"],

            quest["target"]

        )



        await ctx.respond(

            f"📜 Получен квест: "
            f"**{quest['name']}**"

        )









    @commands.slash_command(

        name="myquests",

        description="Мои задания"

    )
    async def myquests(

        self,

        ctx

    ):


        pool = self.bot.db



        quests = await get_player_quests(

            pool,

            ctx.author.id

        )



        if not quests:


            await ctx.respond(

                "📜 У тебя нет заданий."

            )

            return





        embed = discord.Embed(

            title="📜 Мои задания",

            color=0xF1C40F

        )



        text = ""



        for quest in quests:


            status = (

                "✅"

                if quest["completed"]

                else

                "⏳"

            )


            text += (

                f"{status} "
                f"{quest['quest_id']} "
                f"{quest['progress']}/"
                f"{quest['target']}\n"

            )



        embed.add_field(

            name="Прогресс",

            value=text,

            inline=False

        )



        await ctx.respond(

            embed=embed

        )








    async def progress(

        self,

        user_id,

        quest_id,

        amount=1

    ):

        """
        Добавление прогресса
        вызывается из боя
        """


        pool = self.bot.db



        await update_quest_progress(

            pool,

            user_id,

            quest_id,

            amount

        )



        await complete_quest(

            pool,

            user_id,

            quest_id

        )







async def setup(bot):

    await bot.add_cog(

        QuestManager(bot)

    )
