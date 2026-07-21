# quest_events.py

"""
Игровые события для системы квестов ILTA RPG
"""


from database.quest_queries import (
    update_quest_progress,
    complete_quest
)





async def trigger_event(

        pool,

        user_id,

        event,

        amount=1

):

    """
    Главный обработчик событий
    """



    events = {


        "monster_kill":

        [

            "kill_monsters"

        ],



        "boss_kill":

        [

            "kill_boss"

        ],



        "open_chest":

        [

            "open_chests"

        ],



        "get_card":

        [

            "collect_cards"

        ],



        "move_region":

        [

            "explorer"

        ]

    }




    quests = events.get(

        event,

        []

    )



    for quest_id in quests:


        await update_quest_progress(

            pool,

            user_id,

            quest_id,

            amount

        )


        await complete_quest(

            pool,

            user_id,

            quest_id

        )






async def monster_killed(

        pool,

        user_id

):

    """
    Событие убийства обычного моба
    """


    await trigger_event(

        pool,

        user_id,

        "monster_kill"

    )







async def boss_killed(

        pool,

        user_id

):

    """
    Событие убийства босса
    """


    await trigger_event(

        pool,

        user_id,

        "boss_kill"

    )







async def chest_opened(

        pool,

        user_id

):

    """
    Событие открытия сундука
    """


    await trigger_event(

        pool,

        user_id,

        "open_chest"

    )







async def card_received(

        pool,

        user_id

):

    """
    Событие получения карты
    """


    await trigger_event(

        pool,

        user_id,

        "get_card"

    )







async def region_discovered(

        pool,

        user_id

):

    """
    Открытие нового региона
    """


    await trigger_event(

        pool,

        user_id,

        "move_region"

    )
