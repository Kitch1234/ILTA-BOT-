import discord
from discord.ext import commands
from discord import app_commands

from database import deck_slots
from database import player
from database import monsters

from game import combat


class BattleView(discord.ui.View):

    def __init__(
            self,
            cards,
            monster
    ):

        super().__init__(
            timeout=60
        )

        self.cards = cards
        self.monster = monster



        for card in cards:

            button = discord.ui.Button(

                label=card["champion"],

                style=discord.ButtonStyle.primary

            )


            button.callback = self.create_callback(
                card
            )


            self.add_item(button)



    def create_callback(
            self,
            card
    ):


        async def callback(
                interaction: discord.Interaction
        ):


            result = combat.card_attack(
                card,
                self.monster
            )


            text = (

                f"⚔️ **{card['champion']} атакует!**\n\n"

                f"💥 Урон: {result['damage']}\n"

                f"❤️ HP монстра: {max(self.monster['health'],0)}"

            )


            if result["critical"]:

                text += "\n🔥 Критический удар!"



            if combat.is_dead(
                self.monster
            ):

                text += (
                    "\n\n🎉 Победа!"
                )

                self.stop()



            await interaction.response.send_message(
                text
            )


        return callback





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


        deck_id = await player.get_active_deck(
            interaction.user.id
        )


        if not deck_id:

            await interaction.response.send_message(

                "❌ Сначала выберите отряд:\n"
                "/deck_select"

            )

            return



        cards = await deck_slots.get_deck_slots(
            deck_id
        )


        if len(cards) < 3:

            await interaction.response.send_message(

                "❌ В отряде должно быть 3 карты."

            )

            return



        monster = {

            "name": "Лесной волк",

            "health": 200,

            "attack": 30,

            "defense": 5

        }



        await interaction.response.send_message(

            f"⚔️ **Бой начался!**\n\n"

            f"🐺 {monster['name']}\n"

            f"❤️ HP: {monster['health']}\n\n"

            "Выберите карту для атаки:",

            view=BattleView(
                cards,
                monster
            )

        )



async def setup(bot):

    await bot.add_cog(
        Battle(bot)
    )
