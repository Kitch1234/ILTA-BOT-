# ILTA-BOT

Генератор карточек в стиле **Legends of Runeterra** из чемпионов и скинов **League of Legends**.

## Возможности
- Автоматическое определение редкости скина (Common, Epic, Legendary, Ultimate, Prestige, Mythic и т.д.)
- Скачивание артов из официального DataDragon
- Использование рамок из CommunityDragon
- Легко интегрируется в Discord-бота
- Магазин карточек (в разработке)

  
## Установка
```bash
ILTA-BOT/
│
├── main.py
├── requirements.txt
├── .env
├── README.md
│
├── .github/
│   └── workflows/
│       └── python.yml
│
│
├── cogs/                         # Discord команды
│   │
│   ├── profile.py                # Профиль игрока
│   ├── map.py                    # Карта мира
│   ├── movement.py               # Перемещение
│   ├── battle.py                 # Бои
│   ├── cards.py                  # Карты чемпионов
│   ├── collection.py             # Коллекция
│   ├── inventory.py              # Инвентарь
│   ├── quests.py                 # Квесты
│   ├── quest_manager.py          # Управление квестами
│   ├── shop.py                   # Магазин
│   ├── auction.py                # Аукцион
│   ├── crafting.py               # Крафт
│   ├── achievements.py           # Достижения
│   └── leaderboard.py            # Рейтинг игроков
│
│
├── game/                         # Игровая логика
│   │
│   ├── combat.py                 # Боевая система
│   ├── world.py                  # Мир и регионы
│   ├── movement.py               # Хождение по карте
│   ├── leveling.py               # Опыт и уровни
│   ├── rewards.py                # Награды
│   ├── loot.py                   # Выпадение предметов
│   ├── monsters.py               # Мобы
│   ├── abilities.py              # Способности
│   ├── cards.py                  # Логика карт
│   ├── economy.py                # Экономика
│   └── quest_events.py           # События квестов
│
│
├── database/                     # PostgreSQL
│   │
│   ├── database.py               # Подключение БД
│   ├── schema.sql                # Все таблицы
│   ├── queries.py                # Игроки
│   ├── auction_queries.py        # Аукцион
│   ├── quest_queries.py          # Квесты
│   ├── card_queries.py           # Карты
│   └── inventory_queries.py      # Инвентарь
│
│
├── data/                         # Данные игры
│   │
│   ├── champions.json            # Чемпионы
│   ├── skins.json                # Скины
│   ├── skins_rarity.json         # Редкость
│   ├── abilities.json            # Способности
│   ├── card_types.json           # Типы карт
│   ├── items.json                # Предметы
│   ├── loot.json                 # Лут
│   ├── monsters.json             # Мобы
│   ├── quests.json               # Квесты
│   ├── shop.json                 # Магазин
│   ├── regions.json              # Регионы
│   └── world_map.json             # Карта мира
│
│
├── generators/                   # Генерация контента
│   │
│   ├── card_generator.py         # Создание карт
│   ├── skin_generator.py         # Скины
│   ├── champion_lore_generator.py# Лор
│   ├── loot_generator.py         # Лут
│   └── generate_all_cards.py     # Массовая генерация
│
│
├── assets/                       # Изображения
│   │
│   ├── champions/
│   │   ├── aatrox.jpg
│   │   └── ...
│   │
│   ├── skins/
│   │   └── ...
│   │
│   ├── cards/
│   │   └── ...
│   │
│   ├── frames/
│   │   ├── common.png
│   │   ├── epic.png
│   │   ├── legendary.png
│   │   └── mythic.png
│   │
│   └── icons/
│
│
├── utils/                        # Вспомогательное
│   │
│   ├── embeds.py                 # Discord Embed
│   ├── loaders.py                # Загрузка JSON
│   ├── constants.py              # Константы
│   └── logger.py                 # Логи
│
│
└── tests/
    └── test_database.py

pip install -r requirements.txt
