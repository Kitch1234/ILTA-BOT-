from core import database



# ==========================
# Добавить карту в слот отряда
# ==========================

async def add_card_slot(
        owner_id,
        deck_id,
        card_id,
        slot
):

    # Проверяем, что колода принадлежит игроку
    check_deck = """
    SELECT id
    FROM decks
    WHERE id = $1
    AND owner_id = $2;
    """


    # Проверяем, что карта принадлежит игроку
    check_card = """
    SELECT id
    FROM cards
    WHERE id = $1
    AND owner_id = $2;
    """



    insert = """
    INSERT INTO deck_slots
    (
        deck_id,
        slot,
        card_id
    )
    VALUES
    (
        $1,
        $2,
        $3
    )

    ON CONFLICT(deck_id, slot)

    DO UPDATE SET

    card_id = EXCLUDED.card_id;
    """



    async with database.db.acquire() as conn:


        deck = await conn.fetchval(
            check_deck,
            deck_id,
            owner_id
        )


        if not deck:

            raise Exception(
                "Эта колода вам не принадлежит"
            )



        card = await conn.fetchval(
            check_card,
            card_id,
            owner_id
        )


        if not card:

            raise Exception(
                "Этой карты нет в вашей коллекции"
            )



        await conn.execute(
            insert,
            deck_id,
            slot,
            card_id
        )



# ==========================
# Получить боевой отряд
# ==========================

async def get_deck_slots(
        deck_id
):


    query = """

    SELECT

        deck_slots.slot,

        cards.id,
        cards.champion,
        cards.skin,
        cards.rarity,
        cards.attack,
        cards.defense,
        cards.health,
        cards.region

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



# ==========================
# Удалить карту из слота
# ==========================

async def remove_card_slot(
        deck_id,
        slot
):


    query = """

    DELETE FROM deck_slots

    WHERE deck_id = $1

    AND slot = $2;

    """



    async with database.db.acquire() as conn:

        await conn.execute(
            query,
            deck_id,
            slot
        )
