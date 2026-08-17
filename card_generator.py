ТЗ: Система автоматического получения и управления Discord Emoji для ILTA BOT

ЦЕЛЬ
Создать централизованную систему управления кастомными эмодзи Discord-сервера для ILTA BOT.

Система должна автоматически получать все кастомные эмодзи сервера, сохранять их в PostgreSQL, поддерживать кеширование и позволять всему проекту обращаться к эмодзи по удобному ключу, без ручного прописывания Discord ID в каждом файле.

1. ПОЛУЧЕНИЕ ЭМОДЗИ

При запуске бота необходимо получить полный список кастомных эмодзи каждого доступного Discord-сервера.

Использовать discord.py:

guild.emojis

Для каждого эмодзи получить:

- name
- id
- animated
- url
- guild_id

Пример данных:

name: gold
id: 123456789012345678
animated: false
url: https://cdn.discordapp.com/emojis/123456789012345678.png

2. БАЗА ДАННЫХ

Создать PostgreSQL таблицу:

guild_emojis

Поля:

- id BIGSERIAL PRIMARY KEY
- guild_id BIGINT NOT NULL
- emoji_id BIGINT NOT NULL
- name VARCHAR(100) NOT NULL
- animated BOOLEAN DEFAULT FALSE
- url TEXT
- emoji_key VARCHAR(100)
- created_at TIMESTAMP DEFAULT NOW()
- updated_at TIMESTAMP DEFAULT NOW()

Добавить уникальность:

UNIQUE(guild_id, emoji_id)

emoji_id является реальным Discord ID эмодзи.

emoji_key используется как внутренний ключ ILTA.

Пример:

Discord name:
coin_gold

ILTA key:
gold

Тогда в коде используется:

emoji("gold")

а не:

emoji("coin_gold")

3. СИНХРОНИЗАЦИЯ

Создать отдельный модуль:

core/emoji_manager.py

Создать функцию:

async def sync_guild_emojis(guild)

Алгоритм:

1. Получить guild.emojis.
2. Для каждого эмодзи проверить наличие в PostgreSQL.
3. Если эмодзи отсутствует — добавить.
4. Если эмодзи уже существует — обновить name, animated, url и updated_at.
5. Найти записи в БД, которых больше нет среди guild.emojis.
6. Удалить устаревшие записи.
7. Обновить кеш.

Важно:

Если Discord временно недоступен или произошла ошибка API, НЕ удалять существующие записи из БД.

4. КЕШ

Создать кеш эмодзи.

Пример:

{
    "gold": 123456789012345678,
    "crystal": 123456789012345679,
    "attack": 123456789012345680,
    "defense": 123456789012345681,
    "health": 123456789012345682
}

Кеш должен загружаться после синхронизации.

Приоритет получения:

1. Discord/cache
2. PostgreSQL
3. Если эмодзи не найден — fallback

5. ОСНОВНАЯ ФУНКЦИЯ

Создать единую функцию:

emoji("gold")

Она должна возвращать корректное представление Discord-эмодзи.

Примеры:

emoji("gold")
emoji("crystal")
emoji("attack")
emoji("defense")
emoji("health")
emoji("xp")

Использование:

f"{emoji('gold')} {player.gold}"

f"{emoji('attack')} {player.attack}"

f"{emoji('health')} {player.health}/{player.max_health}"

6. НЕ ХРАНИТЬ ID В КОДЕ

Запрещено создавать отдельные константы:

GOLD_EMOJI_ID = 123456789
CRYSTAL_EMOJI_ID = 987654321
ATTACK_EMOJI_ID = 555555555

ID эмодзи не должны быть разбросаны по проекту.

Все обращения должны проходить через Emoji Manager:

emoji("gold")
emoji("crystal")
emoji("attack")

7. ВНУТРЕННИЕ КЛЮЧИ ILTA

Создать стандартные ключи для игровых систем.

Основные:

gold
crystal
card_shard
xp
reputation

Характеристики:

attack
defense
health
energy

Редкости:

common
rare
epic
legendary
mythic
prestige
ultimate

Системные:

success
error
warning
info
lock
unlock
arrow_left
arrow_right
search
settings

Региональные эмодзи:

demacia
noxus
ionia
piltover
zaun
shurima
targon
freljord
shadow_isles
bilgewater
void
ixtal
bandle_city
etc.

Список должен быть расширяемым.

8. ПОДДЕРЖКА ANIMATED EMOJI

Система должна автоматически определять:

animated = true/false

Необходимо корректно поддерживать как обычные, так и анимированные Discord Emoji.

9. FALLBACK

Если emoji("gold") не найден:

бот НЕ должен падать с ошибкой.

Необходимо вернуть fallback-значение.

Например:

🪙

Или специальный fallback:

❔

Fallback должен быть централизованным и легко изменяемым.

10. ADMINISTRATOR MENU

Добавить управление эмодзи через существующую систему /menu.

Не создавать отдельную обязательную команду, которую администратор должен запоминать.

Путь:

/menu
→ Administration
→ Emoji Manager

Меню:

Emoji Manager

📦 Всего эмодзи: 84

[🔄 Синхронизировать]
[📋 Список эмодзи]
[🔍 Поиск]
[📤 Экспорт]

11. СИНХРОНИЗАЦИЯ ЧЕРЕЗ MENU

При нажатии:

🔄 Синхронизировать

бот:

1. Получает guild.emojis.
2. Сравнивает их с PostgreSQL.
3. Добавляет новые.
4. Обновляет изменённые.
5. Удаляет удалённые.
6. Обновляет кеш.
7. Показывает результат.

Пример:

Emoji synchronization completed.

Added: 5
Updated: 2
Removed: 1
Total: 84

12. ПРОСМОТР ЭМОДЗИ

Кнопка:

📋 Список эмодзи

Должна показывать список с пагинацией.

Пример:

🧩 ILTA Emojis

🪙 gold
ID: 123456789012345678

💎 crystal
ID: 123456789012345679

⚔️ attack
ID: 123456789012345680

🛡️ defense
ID: 123456789012345681

❤️ health
ID: 123456789012345682

Кнопки:

[◀️] [1/5] [▶️]

13. ПОИСК

Добавить кнопку:

🔍 Поиск

Администратор вводит:

gold

Бот показывает:

🪙 gold

ID: 123456789012345678
Animated: false
URL: ...

14. ЭКСПОРТ

Добавить:

📤 Экспорт

Бот должен формировать файл:

emojis.json

Формат:

{
    "gold": {
        "id": "123456789012345678",
        "name": "gold",
        "animated": false
    },
    "crystal": {
        "id": "123456789012345679",
        "name": "crystal",
        "animated": false
    },
    "attack": {
        "id": "123456789012345680",
        "name": "attack",
        "animated": true
    }
}

Также желательно поддержать CSV:

emojis.csv

15. АВТОМАТИЧЕСКАЯ СИНХРОНИЗАЦИЯ

Синхронизация должна выполняться:

- при запуске бота;
- после подключения guild;
- вручную через Emoji Manager;
- периодически через background task.

Рекомендуемый интервал:

30 минут.

Необходимо использовать discord.ext.tasks для фоновой синхронизации.

16. ОБРАБОТКА УДАЛЕНИЯ

Если Discord Emoji был удалён:

Discord:
gold → удалён

После синхронизации:

PostgreSQL:
gold → удалить

Cache:
gold → удалить

При этом другие эмодзи не должны затрагиваться.

17. ОБРАБОТКА ПЕРЕИМЕНОВАНИЯ

Если эмодзи:

old_name

стал:

new_name

необходимо обновить name в БД.

При этом emoji_id остаётся прежним.

18. MULTI-GUILD

Система должна поддерживать несколько Discord-серверов.

Все записи должны быть связаны с:

guild_id

Пример:

Guild A:
gold → 111111111

Guild B:
gold → 222222222

Один и тот же emoji_key может существовать на разных серверах с разными Discord ID.

19. ИСПОЛЬЗОВАНИЕ В ILTA

Emoji Manager должен быть доступен из всех игровых Cog.

Например:

profile.py
shop.py
battle.py
cards.py
pack.py
quest.py
inventory.py
daily.py
collection.py

Примеры:

Профиль:

⚔️ Attack: 100
🛡️ Defense: 80
❤️ Health: 500

Баланс:

🪙 Gold: 10,500
💎 Crystals: 250
🔷 Card Shards: 75

Карточка:

⚔️ 120
🛡️ 80
❤️ 500

Награда:

🎁 Rewards

🪙 ×500
💎 ×10
🔷 ×25

20. АРХИТЕКТУРА

Рекомендуемая структура:

ILTA-BOT/

core/
    database.py
    emoji_manager.py

database/
    emojis.py

cogs/
    menu.py
    profile.py
    shop.py
    battle.py
    cards.py
    pack.py
    quest.py
    inventory.py

assets/

main.py

core/emoji_manager.py

Отвечает за:

- кеш;
- получение Discord Emoji;
- поиск;
- синхронизацию;
- fallback;
- предоставление API emoji().

database/emojis.py

Отвечает за:

- INSERT;
- UPDATE;
- DELETE;
- SELECT;
- работу с PostgreSQL.

cogs/menu.py

Отвечает только за интерфейс администратора.

21. ТРЕБОВАНИЯ К КОДУ

Использовать async/await.

Использовать существующий asyncpg pool проекта.

Не создавать отдельное соединение с PostgreSQL для каждого запроса.

Не дублировать логику работы с Emoji в Cog.

Не обращаться напрямую к таблице guild_emojis из игровых Cog.

Все игровые системы должны обращаться только через Emoji Manager.

22. ЛОГИРОВАНИЕ

При запуске:

[EMOJI] Starting synchronization...

После завершения:

[EMOJI] Guild: ILTA
[EMOJI] Added: 5
[EMOJI] Updated: 2
[EMOJI] Removed: 1
[EMOJI] Total: 84

При ошибке:

[EMOJI] Synchronization failed: <error>

Ошибки не должны останавливать работу бота.

23. БЕЗОПАСНОСТЬ

Управление Emoji Manager доступно только администраторам сервера или пользователям с соответствующим Discord permission.

Обычные пользователи не должны иметь доступа к:

- синхронизации;
- экспорту;
- удалению;
- изменению emoji_key.

24. РЕЗУЛЬТАТ

После реализации система должна работать следующим образом:

Discord Server
        ↓
guild.emojis
        ↓
Emoji Manager
        ↓
PostgreSQL
        ↓
Cache
        ↓
Все игровые системы ILTA

В любом месте проекта можно использовать:

emoji("gold")
emoji("crystal")
emoji("attack")
emoji("defense")
emoji("health")
emoji("xp")

Без ручного указания Discord ID.

Главная задача системы — сделать Emoji полностью централизованными, автоматически синхронизируемыми и доступными всему ILTA BOT через простые ключи.
:::
