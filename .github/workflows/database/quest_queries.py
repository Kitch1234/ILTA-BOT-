# quest_queries.py

"""
Запросы для системы квестов ILTA RPG
"""





async def create_quest(

        pool,

        user_id,

        quest_id,

        target

):

    """
    Создать квест игроку
    """

    query = """

    INSERT INTO player_quests

    (
        user_id,
        quest_id,
        target
    )

    VALUES

    ($1,$2,$3)

    ON CONFLICT DO NOTHING;

    """


    async with pool.acquire() as connection:

        await connection.execute(

            query,

            user_id,

            quest_id,

            target

        )







async def get_player_quests(

        pool,

        user_id

):

    """
    Получить задания игрока
    """


    query = """

    SELECT *

    FROM player_quests

    WHERE user_id = $1;

    """


    async with pool.acquire() as connection:


        return await connection.fetch(

            query,

            user_id

        )







async def update_quest_progress(

        pool,

        user_id,

        quest_id,

        amount=1

):

    """
    Добавить прогресс квеста
    """

    query = """

    UPDATE player_quests

    SET progress = progress + $1

    WHERE user_id=$2

    AND quest_id=$3

    AND completed = FALSE;

    """



    async with pool.acquire() as connection:


        await connection.execute(

            query,

            amount,

            user_id,

            quest_id

        )







async def complete_quest(

        pool,

        user_id,

        quest_id

):

    """
    Проверить выполнение
    """

    query = """

    UPDATE player_quests

    SET completed = TRUE

    WHERE user_id=$1

    AND quest_id=$2

    AND progress >= target;

    """



    async with pool.acquire() as connection:


        await connection.execute(

            query,

            user_id,

            quest_id

        )







async def claim_quest_reward(

        pool,

        user_id,

        quest_id

):

    """
    Забрать награду
    """

    query = """

    UPDATE player_quests

    SET claimed = TRUE

    WHERE user_id=$1

    AND quest_id=$2

    AND completed=TRUE;

    """



    async with pool.acquire() as connection:


        await connection.execute(

            query,

            user_id,

            quest_id

        )
