# map.py

"""
Карта мира ILTA RPG
"""


import discord

from discord.ext import commands


from game.world import (

    get_regions,

    get_region,

    get_neighbors

)


from game.movement import (

    move_player,

    get_player_location

)






class Map(commands.Cog):


    def __init__(

            self,

            bot

    ):

        self.bot = bot






    @commands.slash_command(

        name="map",

        description="Показать карту мира"

    )
    async def map(

            self,

            ctx

    ):


        regions = get_regions()



        embed = discord.Embed(

            title="🗺 Карта Рунтерры",

            color=0x3498DB

        )



        text = ""



        for region in regions:


            text += (

                f"🌍 **{region['name']}**\n"

                f"Уровень: {region['level']}\n"

                f"Опасность: {region['danger']}\n\n"

            )



        embed.add_field(

            name="Регионы",

            value=text,

            inline=False

        )


        await ctx.respond(

            embed=embed

        )









    @commands.slash_command(

        name="location",

        description="Твоя текущая локация"

    )
    async def location(

            self,

            ctx

    ):


        pool = self.bot.db



        position = await get_player_location(

            pool,

            ctx.author.id

        )



        if not position:


            await ctx.respond(

                "❌ Персонаж не создан."

            )

            return





        region = get_region(

            position["region_id"]

        )



        embed = discord.Embed(

            title=

            f"📍 {region['name']}",

            description=

            region["description"],

            color=0x2ECC71

        )



        embed.add_field(

            name="🐺 Мобы",

            value=

            "\n".join(

                region["monsters"]

            ),

            inline=False

        )



        embed.add_field(

            name="⛏ Ресурсы",

            value=

            "\n".join(

                region["resources"]

            ),

            inline=False

        )



        await ctx.respond(

            embed=embed

        )









    @commands.slash_command(

        name="move",

        description="Перейти в регион"

    )
    async def move(

            self,

            ctx,

            region: str

    ):


        pool = self.bot.db



        result = await move_player(

            pool,

            ctx.author.id,

            region

        )



        if not result["success"]:


            await ctx.respond(

                "❌ "

                + result["message"]

            )

            return






        embed = discord.Embed(

            title="🚶 Переход выполнен",

            color=0x1ABC9C

        )


        embed.add_field(

            name="Новая локация",

            value=

            result["region"]

        )


        embed.add_field(

            name="Описание",

            value=

            result["description"],

            inline=False

        )


        await ctx.respond(

            embed=embed

        )







async def setup(bot):

    await bot.add_cog(

        Map(bot)

    )
