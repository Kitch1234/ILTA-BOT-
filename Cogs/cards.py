# cards.py

import discord

from discord.ext import commands

from database.queries import (
    get_cards
)

from data.champions import (
    get_champion
)



class Cards(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    @commands.slash_command(
        name="cards",
        description="Показать коллекцию карт"
    )
    async def cards(
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
                "🎴 У тебя пока нет карт."
            )

            return



        embed = discord.Embed(

            title="🎴 Коллекция карт",

            color=0x9B59B6

        )


        text = ""


        for card in cards[:20]:

            text += (
                f"⚔ {card['champion']} "
                f"- {card['rarity']}\n"
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





    @commands.slash_command(
        name="card",
        description="Показать карту чемпиона"
    )
    async def card(
        self,
        ctx,
        champion: str
    ):


        data = get_champion(
            champion
        )


        if not data:

            await ctx.respond(
                "❌ Чемпион не найден."
            )

            return



        skin = data["skins"][0]



        image_url = (

            "https://raw.communitydragon.org/"
            "latest/plugins/"
            "rcp-be-lol-game-data/"
            "global/default/assets/characters/"
            +
            skin["image"]

       
