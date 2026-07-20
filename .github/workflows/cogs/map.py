# map.py

import discord

from discord.ext import commands

from data.maps import get_location

from game.movement import move_player

from database.queries import (
    get_player,
    update_location
)



class Map(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.slash_command(
        name="map",
        description="Показать текущую локацию"
    )
    async def map(
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
                "❌ Сначала создай персонажа."
            )

            return



        location = get_location(
            player["location"]
        )


        embed = discord.Embed(

            title=f"🌍 {player['location']}",

            description=
            location["description"],

            color=0x3498DB
        )



        neighbors = "\n".join(

            [
                f"➡ {x}"
                for x in location["neighbors"]
            ]

        )


        embed.add_field(

            name="Доступные направления",

            value=neighbors,

            inline=False
        )


        embed.add_field(

            name="Уровень региона",

            value=
            str(location["level_required"]),

            inline=True
        )


        monsters = "\n".join(

            location["monsters"]

        )


        embed.add_field(

            name="👹 Опасности",

            value=monsters,

            inline=True
        )


        await ctx.respond(
            embed=embed
        )





    @commands.slash_command(
        name="move",
        description="Перейти в другой регион"
    )
    async def move(
        self,
        ctx,
        region: str
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





        data = {

            "location":
            player["location"],

            "level":
            player["level"]

        }





        result = move_player(
            data,
            region
        )



        if not result["success"]:

            await ctx.respond(
                "❌ "
                +
                result["message"]
            )

            return





        await update_location(

            pool,

            ctx.author.id,

            region

        )




        embed = discord.Embed(

            title="🚶 Путешествие",

            description=
            result["message"],

            color=0x2ECC71

        )


        event = result.get(
            "event"
        )


        if event:


            embed.add_field(

                name="Событие",

                value=
                event["message"],

                inline=False
            )


        await ctx.respond(
            embed=embed
        )





async def setup(bot):

    await bot.add_cog(
        Map(bot)
      )
