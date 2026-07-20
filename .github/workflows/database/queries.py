# queries.py

"""
Запросы к базе данных ILTA RPG
"""


async def create_player(pool, user_id, username):
    """
    Создание нового игрока
    """

    query = """

    INSERT INTO players
    (
        id,
        username
    )

    VALUES
    ($1, $2)

    ON CONFLICT (id)
    DO NOTHING;

    """

    async with pool.acquire() as connection:

        await connection.execute(
            query,
            user_id,
            username
        )





async def get_player(pool, user_id):
    """
    Получить профиль игрока
    """

    query = """

    SELECT *

    FROM players

    WHERE id = $1;

    """


    async with pool.acquire() as connection:

        return await connection.fetchrow(
            query,
            user_id
        )






async def update_location(
        pool,
        user_id,
        location
):
    """
    Изменить регион игрока
    """


    query = """

    UPDATE players

    SET location = $1

    WHERE id = $2;

    """


    async with pool.acquire() as connection:

        await connection.execute(
            query,
            location,
            user_id
        )






async def add_experience(
        pool,
        user_id,
        amount
):
    """
    Добавить опыт
    """


    query = """

    UPDATE players

    SET experience = experience + $1

    WHERE id = $2;

    """


    async with pool.acquire() as connection:

        await connection.execute(
            query,
            amount,
            user_id
        )






async def add_gold(
        pool,
        user_id,
        amount
):
    """
    Добавить золото
    """


    query = """

    UPDATE players

    SET gold = gold + $1

    WHERE id = $2;

    """


    async with pool.acquire() as connection:

        await connection.execute(
            query,
            amount,
            user_id
        )







async def add_card(
        pool,
        user_id,
        champion,
        skin,
        rarity
):
    """
    Добавить карту игроку
    """


    query = """

    INSERT INTO cards
    (
        owner_id,
        champion,
        skin,
        rarity
    )

    VALUES
    ($1,$2,$3,$4);

    """


    async with pool.acquire() as connection:

        await connection.execute(
            query,
            user_id,
            champion,
            skin,
            rarity
        )







async def get_cards(
        pool,
        user_id
):
    """
    Получить коллекцию карт
    """


    query = """

    SELECT *

    FROM cards

    WHERE owner_id = $1;

    """


    async with pool.acquire() as connection:

        return await connection.fetch(
            query,
            user_id
        )







async def add_item(
        pool,
        user_id,
        item
):
    """
    Добавить предмет
    """


    query = """

    INSERT INTO inventory
    (
        owner_id,
        item
    )

    VALUES
    ($1,$2);

    """


    async with pool.acquire() as connection:

        await connection.execute(
            query,
            user_id,
            item
        )







async def get_inventory(
        pool,
        user_id
):
    """
    Получить инвентарь
    """


    query = """

    SELECT *

    FROM inventory

    WHERE owner_id = $1;

    """


    async with pool.acquire() as connection:

        return await connection.fetch(
            query,
            user_id
        )
