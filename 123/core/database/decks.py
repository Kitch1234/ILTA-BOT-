from core import database


async def create_deck(
        owner_id,
        name
):

    query = """
    INSERT INTO decks
    (
        owner_id,
        name
    )
    VALUES
    (
        $1,
        $2
    )
    RETURNING id;
    """

    async with database.db.acquire() as conn:

        return await conn.fetchval(
            query,
            owner_id,
            name
        )



async def get_player_decks(
        owner_id
):

    query = """
    SELECT *
    FROM decks
    WHERE owner_id = $1;
    """

    async with database.db.acquire() as conn:

        return await conn.fetch(
            query,
            owner_id
        )
