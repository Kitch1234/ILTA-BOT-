# main.py

"""
ILTA RPG Discord Bot
"""


import os
import asyncio


import discord

from discord.ext import commands


from dotenv import load_dotenv


from database.database import Database





load_dotenv()



TOKEN = os.getenv(
    "DISCORD_TOKEN"
)





intents = discord.Intents.default()

intents.message_content = True

intents.members = True





class ILTABot(commands.Bot):


    def __init__(self):

        super().__init__(

            command_prefix="!",

            intents=intents

        )


        self.db = None







    async def setup_hook(self):


        # PostgreSQL


        database = Database()


        await database.connect()


        self.db = database.pool



        print(
            "✅ База данных готова"
        )





        # загрузка модулей


        cogs = [

            "profile",

            "map",

            "battle",

            "cards",

            "collection",

            "inventory",

            "quests",

            "quest_manager",

            "shop",

            "auction"

        ]



        for cog in cogs:


            try:


                await self.load_extension(

                    f"cogs.{cog}"

                )


                print(

                    f"✅ Загружен {cog}"

                )



            except Exception as error:


                print(

                    f"❌ Ошибка {cog}:",

                    error

                )







    async def on_ready(self):


        print(

            f"🟢 Бот запущен: "
            f"{self.user}"

        )


        try:


            synced = await self.tree.sync()


            print(

                f"Команд загружено: {len(synced)}"

            )


        except Exception as error:


            print(

                "Ошибка синхронизации:",

                error

            )







bot = ILTABot()





async def main():


    async with bot:


        await bot.start(

            TOKEN

        )







if __name__ == "__main__":


    asyncio.run(

        main()

    )
