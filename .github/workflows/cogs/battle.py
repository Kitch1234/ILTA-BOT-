# battle.py

import discord

from discord.ext import commands

from database.queries import (
    get_player,
    add_experience,
    add_gold,
    add_item
)

from game.combat import start_battle



class Battle(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    @commands.slash_command(
        name="battle",
        description="Начать бой с мобом"
    )
    async def battle(
        self,
        ctx,
        monster: str
    ):


        pool = self.bot.db



        player_db = await get_player(
            pool,
            ctx.author.id
        )



        if not player_db:

            await ctx.respond(
                "❌ Сначала создай персонажа."
            )

            return




        player = {

            "health":
            player_db["health"],

            "attack":
            player_db["attack"],

            "defense":
            player_db["defense"]

        }




        result = start_battle(

            player,

            monster

        )



        if not result["success"]:


            await ctx.respond(
                result["message"]
            )

            return






        embed = discord.Embed(

            title="⚔ Бой",

            color=0xE74C3C

        )



        logs = "\n".join(

            result["log"][-10:]

        )


        embed.add_field(

            name="Ход боя",

            value=logs,

            inline=False

        )




        if result["result"] == "win":


            await add_experience(

                pool,

                ctx.author.id,

                result["experience"]

            )


            await add_gold(

                pool,

                ctx.author.id,

                result["gold"]

            )



            embed.color = 0x2ECC71


            embed.add_field(

                name="Победа!",

                value=(

                    f"✨ +{result['experience']} XP\n"

                    f"💰 +{result['gold']} золота"

                ),

                inline=False

            )



            loot = result.get(
                "loot"
            )


            if loot and loot.get("items"):


                await add_item(

                    pool,

                    ctx.author.id,

                    loot["items"]

                )


                embed.add_field(

                    name="🎁 Добыча",

                    value=
                    loot["items"],

                    inline=False

                )



        else:


            embed.color = 0x000000


            embed.add_field(

                name="Поражение",

                value=
                "Вы были побеждены.",

                inline=False

            )



        await ctx.respond(
            embed=embed
        )





async def setup(bot):

    await bot.add_cog(
        Battle(bot)
    )
