# profile.py

import discord

from discord.ext import commands

from database.queries import (
    get_player,
    get_cards,
    get_inventory
)



class Profile(commands.Cog):

    def __init__(self, bot):

        self.bot = bot





    @commands.slash_command(
        name="profile",
        description="Показать профиль игрока"
    )
    async def profile(
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
                "❌ У тебя ещё нет профиля. Используй /start"
            )

            return





        cards = await get_cards(
            pool,
            ctx.author.id
        )


        inventory = await get_inventory(
            pool,
            ctx.author.id
        )





        embed = discord.Embed(

            title=f"⚔ {player['username']}",

            description=
            "Профиль героя ILTA RPG",

            color=0x9B59B6

        )



        embed.add_field(

            name="📊 Уровень",

            value=
            f"{player['level']} уровень",

            inline=True
        )



        embed.add_field(

            name="✨ Опыт",

            value=
            f"{player['experience']} XP",

            inline=True
        )



        embed.add_field(

            name="💰 Золото",

            value=
            f"{player['gold']}",

            inline=True
        )



        embed.add_field(

            name="❤️ Здоровье",

            value=
            f"{player['health']}",

            inline=True
        )



        embed.add_field(

            name="⚔ Атака",

            value=
            f"{player['attack']}",

            inline=True
        )



        embed.add_field(

            name="🛡 Защита",

            value=
            f"{player['defense']}",

            inline=True
        )



        embed.add_field(

            name="🌍 Локация",

            value=
            player["location"],

            inline=True
        )



        embed.add_field(

            name="🎴 Карты",

            value=
            str(len(cards)),

            inline=True
        )



        embed.add_field(

            name="🎒 Предметы",

            value=
            str(len(inventory)),

            inline=True
        )



        embed.set_thumbnail(

            url=
            ctx.author.avatar.url

        )



        await ctx.respond(
            embed=embed
        )





async def setup(bot):

    await bot.add_cog(
        Profile(bot)
      )
