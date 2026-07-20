# collection.py

import discord

from discord.ext import commands

import json
import os



class Collection(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    def get_champion(self, name):

        path = (
            f"data/champions/{name.lower()}.json"
        )


        if not os.path.exists(path):

            return None


        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)





    @commands.slash_command(
        name="collection",
        description="Информация о чемпионе"
    )
    async def collection(
        self,
        ctx,
        champion: str
    ):


        data = self.get_champion(
            champion
        )


        if not data:

            await ctx.respond(
                "❌ Чемпион не найден."
            )

            return



        embed = discord.Embed(

            title=
            f"⚔ {data['name']}",

            description=
            data["title"],

            color=0x9B59B6

        )


        embed.add_field(

            name="🌍 Регион",

            value=
            ", ".join(
                data["region"]
            ),

            inline=False
        )


        embed.add_field(

            name="⚔ Роль",

            value=
            ", ".join(
                data["role"]
            ),

            inline=False
        )


        embed.add_field(

            name="📖 История",

            value=
            data["lore"],

            inline=False
        )


        embed.add_field(

            name="💬 Реплики",

            value=
            "\n".join(
                data["quotes"]
            ),

            inline=False
        )


        abilities = "\n".join(

            [
                f"{key}: {value}"

                for key,value

                in data["abilities"].items()
            ]

        )


        embed.add_field(

            name="✨ Способности",

            value=
            abilities,

            inline=False
        )


        await ctx.respond(
            embed=embed
        )





async def setup(bot):

    await bot.add_cog(
        Collection(bot)
    )
