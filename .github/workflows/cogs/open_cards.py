# open_cards.py

"""
Система открытия сундуков ILTA RPG
"""


import random
import discord

from discord.ext import commands


from data.champion_loader import (
    get_all_champions
)


from database.queries import (
    add_card,
    get_player
)




RARITY_CHANCES = {

    "Обычный": 60,

    "Эпический": 25,

    "Легендарный": 10,

    "Мифический": 4,

    "Престижный": 1

}





def random_rarity():

    roll = random.randint(
        1,
        100
    )


    current = 0


    for rarity, chance in RARITY_CHANCES.items():

        current += chance


        if roll <= current:

            return rarity





def random_card():

    champions = get_all_champions()


    champion_name = random.choice(

        list(champions.keys())

    )


    champion = champions[champion_name]


    skins = champion.get(
        "skins",
        []
    )


    skin = random.choice(
        skins
    )


    rarity = random_rarity()


    return {

        "champion":
        champion_name,

        "skin":
        skin["name"],

        "rarity":
        rarity

    }





class OpenCards(commands.Cog):


    def __init__(self, bot):

        self.bot = bot





    @commands.slash_command(

        name="chest",

        description="Открыть сундук с картой"

    )
    async def chest(
        self,
        ctx
    ):


        pool = self.bot.db



        player = await get_player(

            pool,

            ctx.author.id

        )



        if not player:

            await ctx.respond(

                "❌ Создай персонажа"

            )

            return





        card = random_card()



        await add_card(

            pool,

            ctx.author.id,

            card["champion"],

            card["skin"],

            card["rarity"]

        )





        embed = discord.Embed(

            title="🎁 Открытие сундука",

            color=0xF1C40F

        )



        embed.add_field(

            name="Чемпион",

            value=card["champion"],

            inline=True

        )


        embed.add_field(

            name="Скин",

            value=card["skin"],

            inline=True

        )


        embed.add_field(

            name="Редкость",

            value=card["rarity"],

            inline=True

        )


        await ctx.respond(

            embed=embed

        )





async def setup(bot):

    await bot.add_cog(
        OpenCards(bot)
    )
