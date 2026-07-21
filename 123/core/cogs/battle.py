import discord
from discord.ext import commands
from discord import app_commands

from database import deck_slots
from database import monsters

from game import combat



class Battle(commands.Cog):


    def __init__(self, bot):

        self.bot = bot



    @app_commands.command(
        name="battle",
        description="Начать бой"
    )
    async def battle(
        self,
        interaction: discord.Interaction
    ):


        cards = await deck_slots.get_deck_slots(1)


        if not cards:

            await interaction.response.send_message(
                "❌ У вас нет активного отряда."
            )

            return



        monster = {

            "name": "Лесной волк",
            "health": 200,
            "attack": 30,
            "defense": 5

        }



        card = dict(cards[0])


        result = combat.card_attack(
            card,
            monster
        )



        await interaction.response.send_message(

            f"⚔️ {card['champion']} атакует!\n\n"
            f"🐺 {monster['name']}\n"
            f"Получено урона: {result['damage']}\n"
            f"❤️ HP монстра: {result['monster_hp']}"

        )



async def setup(bot):

    await bot.add_cog(
        Battle(bot)
    )
