from core import database


async def get_collection_by_region(
        owner_id,
        region
):

    query = """
    SELECT
        cards.id,
        cards.champion,
        cards.skin,
        cards.rarity,
        cards.attack,
        cards.defense,
        cards.health,
        cards.region

    FROM cards

    WHERE owner_id = $1
    AND region = $2;

    """

    async with database.db.acquire() as conn:

        return await conn.fetch(
            query,
            owner_id,
            region
        )
