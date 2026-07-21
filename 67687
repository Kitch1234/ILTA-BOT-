from core import database


# Установить активную колоду

async def set_active_deck(
        user_id,
        deck_id
):

    query = """
    UPDATE users
    SET active_deck = $2
    WHERE user_id = $1;
    """


    async with database.db.acquire() as conn:

        await conn.execute(
            query,
            user_id,
            deck_id
        )



# Получить активную колоду

async def get_active_deck(
        user_id
):

    query = """
    SELECT active_deck
    FROM users
    WHERE user_id = $1;
    """


    async with database.db.acquire() as conn:

        return await conn.fetchval(
            query,
            user_id
        )
