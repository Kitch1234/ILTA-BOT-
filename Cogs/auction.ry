# auction.py

"""
Аукцион ILTA RPG
"""


import discord

from discord.ext import commands



class Auction(commands.Cog):


    def __init__(self, bot):

        self.bot = bot







    @commands.slash_command(

        name="auction",

        description="Открыть аукцион"

    )
    async def auction(

        self,

        ctx

    ):



        embed = discord.Embed(

            title="🏛 Аукцион ILTA",

            description=(

                "Активные лоты:\n\n"

                "🎴 Aatrox - Легендарный\n"

                "💰 Ставка: 5000"

            ),

            color=0xE67E22

        )



        await ctx.respond(

            embed=embed

        )









    @commands.slash_command(

        name="sell_card",

        description="Продать карту"

    )
    async def sell_card(

        self,

        ctx,

        card_id: int,

        price: int

    ):



        # временная логика

        # позже подключим PostgreSQL



        await ctx.respond(

            f"🎴 Карта выставлена!\n"

            f"Цена: {price} золота"

        )









    @commands.slash_command(

        name="bid",

        description="Сделать ставку"

    )
    async def bid(

        self,

        ctx,

        auction_id: int,

        amount: int

    ):



        await ctx.respond(

            f"💰 Ставка {amount} принята!"

        )







async def setup(bot):

    await bot.add_cog(

        Auction(bot)

    )
