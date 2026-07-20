# shop.py

"""
Магазин ILTA RPG
"""


import json
import os

import discord

from discord.ext import commands


from database.queries import (

    get_player,

    add_item,

    add_gold

)





SHOP_FILE = (
    "data/shop.json"
)





def load_shop():


    if not os.path.exists(
        SHOP_FILE
    ):

        return []


    with open(

        SHOP_FILE,

        "r",

        encoding="utf-8"

    ) as file:

        data = json.load(file)


    return data["items"]





class Shop(commands.Cog):


    def __init__(self, bot):

        self.bot = bot







    @commands.slash_command(

        name="shop",

        description="Открыть магазин"

    )
    async def shop(

        self,

        ctx

    ):


        items = load_shop()



        embed = discord.Embed(

            title="🏪 Магазин ILTA",

            color=0xF39C12

        )



        text = ""



        for item in items:


            text += (

                f"🛒 {item['name']}\n"

                f"💰 Цена: {item['price']}\n"

                f"ID: `{item['id']}`\n\n"

            )



        embed.add_field(

            name="Товары",

            value=text,

            inline=False

        )


        await ctx.respond(

            embed=embed

        )









    @commands.slash_command(

        name="buy",

        description="Купить товар"

    )
    async def buy(

        self,

        ctx,

        item_id: str

    ):



        pool = self.bot.db



        player = await get_player(

            pool,

            ctx.author.id

        )


        if not player:

            await ctx.respond(

                "❌ Нет персонажа."

            )

            return





        items = load_shop()



        item = next(

            (

                x for x in items

                if x["id"] == item_id

            ),

            None

        )



        if not item:


            await ctx.respond(

                "❌ Товар не найден."

            )

            return






        if player["gold"] < item["price"]:


            await ctx.respond(

                "❌ Не хватает золота."

            )

            return






        await add_gold(

            pool,

            ctx.author.id,

            -item["price"]

        )





        await add_item(

            pool,

            ctx.author.id,

            item["name"]

        )





        embed = discord.Embed(

            title="✅ Покупка",

            description=(

                f"Ты купил:\n"

                f"**{item['name']}**"

            ),

            color=0x2ECC71

        )


        await ctx.respond(

            embed=embed

        )








async def setup(bot):

    await bot.add_cog(

        Shop(bot)

    )
