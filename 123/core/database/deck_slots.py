from core import database



# ==========================
# Добавить карту в слот
# ==========================

async def add_card_slot(
        owner_id,
        deck_id,
        card_id,
        slot
):

    query = """

    INSERT INTO deck_slots
    (
        deck_id,
        slot,
        card_id
    )

    SELECT
        $2,
        $4,
        $3

    FROM cards

    WHERE cards.id = $3
    AND cards.owner_id = $1;

    """


    async with database.db.acquire() as conn:

        await conn.execute(
            query,
            owner_id,
            deck_id,
            card_id,
            slot
        )



# ==========================
# Получить отряд
# ==========================

async def get_deck_slots(
        deck_id
):

    query = """

    SELECT

        deck_slots.slot,

        cards.id,
        cards.champion,
        cards.rarity,
        cards.attack,
        cards.health

    FROM deck_slots


    JOIN cards

    ON cards.id = deck_slots.card_id


    WHERE deck_slots.deck_id = $1

    ORDER BY deck_slots.slot;

    """


    async with database.db.acquire() as conn:

        return await conn.fetch(
            query,
            deck_id
        )
