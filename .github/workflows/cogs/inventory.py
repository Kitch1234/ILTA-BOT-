# inventory.py

"""
Инвентарь игрока ILTA RPG
"""


import discord

from discord.ext import commands


from database.queries import (
    get_inventory,
    get_cards
)




class Inventory(commands.Cog):


    def __init__(self, bot):

        self.bot = bot






    @commands.slash_command(

        name="inventory",

        description="Показать инвентарь"

    )
    async def inventory(

        self,

        ctx

    ):


        pool = self.bot.db



        items = await get_inventory(

            pool,

            ctx.author.id

        )



        if not items:


            await ctx.respond(

                "🎒 Инвентарь пуст."

            )

            return





        embed = discord.Embed(

            title="🎒 Инвентарь",

            color=0x2ECC71

        )



        text = ""



        for item in items[:20]:


            text += (

                f"▫ {item['item']}"

                f" x{item['amount']}\n"

            )





        embed.add_field(

            name="Предметы",

            value=text,

            inline=False

        )



        embed.set_footer(

            text=
            f"Всего предметов: {len(items)}"

        )



        await ctx.respond(

            embed=embed

        )








    @commands.slash_command(

        name="collection",

        description="Показать коллекцию карт"

    )
    async def collection(

        self,

        ctx

    ):


        pool = self.bot.db



        cards = await get_cards(

            pool,

            ctx.author.id

        )



        if not cards:


            await ctx.respond(

                "🎴 У тебя нет карт."

            )

            return






        embed = discord.Embed(

            title="🎴 Коллекция чемпионов",

            color=0x9B59B6

        )



        text = ""



        for card in cards[:25]:


            text += (

                f"⚔ {card['champion']}\n"

                f"   🎭 {card['skin']}\n"

                f"   ⭐ {card['rarity']}\n\n"

            )




        embed.add_field(

            name="Карты",

            value=text,

            inline=False

        )



        embed.set_footer(

            text=
            f"Всего карт: {len(cards)}"

        )



        await ctx.respond(

            embed=embed

        )







async def setup(bot):

    await bot.add_cog(

        Inventory(bot)

          )
