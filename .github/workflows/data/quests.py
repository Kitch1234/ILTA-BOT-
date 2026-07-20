# quests.py

import json
import os

import discord

from discord.ext import commands



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






class Quests(commands.Cog):


    def __init__(self, bot):

        self.bot = bot






    @commands.slash_command(

        name="quests",

        description="Показать доступные задания"

    )
    async def quests(

        self,

        ctx

    ):


        data = load_quests()



        embed = discord.Embed(

            title="📜 Задания",

            color=0xF1C40F

        )



        daily = data.get(

            "daily",

            []

        )



        text = ""



        for quest in daily:


            text += (

                f"🟢 {quest['name']}\n"

                f"{quest['description']}\n"

                f"🎁 {quest['reward_xp']} XP "
                f"+ {quest['reward_gold']} золота\n\n"

            )



        embed.add_field(

            name="Ежедневные",

            value=text or "Нет",

            inline=False

        )



        regions = data.get(

            "regions",

            []

        )



        text = ""



        for quest in regions:


            text += (

                f"🌍 {quest['name']}\n"

                f"{quest['description']}\n\n"

            )



        embed.add_field(

            name="Региональные",

            value=text or "Нет",

            inline=False

        )



        await ctx.respond(

            embed=embed

        )






async def setup(bot):

    await bot.add_cog(

        Quests(bot)

  )
