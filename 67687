from core import database


# Получить карты игрока

async def get_player_cards(owner_id):

    query = """
    SELECT *
    FROM cards
    WHERE owner_id = $1;
    """

    async with database.db.acquire() as conn:

        return await conn.fetch(
            query,
            owner_id
        )



# Получить одну карту

async def get_card(card_id):

    query = """
    SELECT *
    FROM cards
    WHERE id = $1;
    """

    async with database.db.acquire() as conn:

        return await conn.fetchrow(
            query,
            card_id
        )



# Добавить карту игроку

async def add_card(
        owner_id,
        champion,
        skin,
        rarity,
        attack,
        defense,
        health
):

    query = """
    INSERT INTO cards
    (
        owner_id,
        champion,
        skin,
        rarity,
        attack,
        defense,
        health
    )
    VALUES
    (
        $1,$2,$3,$4,$5,$6,$7
    );
    """


    async with database.db.acquire() as conn:

        await conn.execute(
            query,
            owner_id,
            champion,
            skin,
            rarity,
            attack,
            defense,
            health
        )
