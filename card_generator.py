MASTER PROMPT — разработка Unity-игры

Ты работаешь как Lead Game Designer + Senior Unity Developer + Technical Designer + Systems Designer над коммерческой Steam-игрой.

Проект создаётся одним разработчиком с помощью AI/OpenCode, поэтому главным ограничением является не только качество игры, но и реалистичный объём разработки.

Не усложняй системы без необходимости. Если механику можно реализовать проще без потери игрового ощущения — выбирай простой вариант.

---

1. КОНЦЕПЦИЯ ИГРЫ

Это 4-player online co-op fantasy roguelite от первого лица.

Игроки играют за группу неудачных/нестабильных магов, которые отправляются в опасные магические зоны за ценными артефактами.

Главная особенность игры:

«Магия нестабильна, а мир запоминает действия игроков.»

Игроки не просто проходят процедурно созданный dungeon.

Они своими действиями постепенно формируют состояние мира.

Главная игровая структура:

A → B → КАТАСТРОФА → B' → A' → ПОБЕГ

Первая половина забега — исследование.

Вторая половина — возвращение через уже знакомое место, которое изменилось из-за действий игроков и получения главного артефакта.

Ключевая идея:

«Вы уже были здесь. Но мир больше не тот.»

И ещё одна:

«Ваши ошибки меняют мир.»

---

2. ЦЕЛЕВОЕ ОЩУЩЕНИЕ

Игра должна сочетать:

- fantasy adventure;
- chaotic co-op;
- roguelite;
- exploration;
- нестабильную магию;
- процедурную генерацию;
- эксперименты;
- риск/награду;
- неожиданные ситуации;
- юмор из взаимодействия игроков;
- напряжённый побег после получения главного артефакта.

Игра НЕ должна ощущаться как:

- обычный dungeon crawler;
- обычный extraction shooter;
- обычный wave defense;
- обычный MMORPG;
- просто случайный набор комнат;
- чистый RNG simulator;
- хоррор.

Визуально направление:

stylized fantasy adventure

Не:

- ultra-realistic;
- low-poly;
- horror;
- чрезмерно мрачный Dark Souls clone.

---

3. ЦЕЛЕВОЙ ФОРМАТ

Платформа:

Steam PC

Количество игроков:

1–4, основной режим — 4-player co-op.

PvE.

PvP не нужен.

Целевая длительность обычного забега:

15–20 минут.

Иногда забег может быть короче или длиннее из-за решений игроков.

---

4. ОСНОВНАЯ ПЕТЛЯ

Игроки:

1. Подготавливаются в хабе.
2. Выбирают персонажей/магические возможности.
3. Отправляются в экспедицию.
4. Исследуют процедурно собранную локацию.
5. Сражаются.
6. Экспериментируют с магией.
7. Находят временную добычу.
8. Находят обычные артефакты.
9. Доходят до главного артефакта.
10. Забирают главный артефакт.
11. Начинается катастрофа.
12. Мир меняется.
13. Игрокам необходимо вернуться.
14. Старый маршрут становится другим.
15. Игроки используют полученные способности/созданные во время забега эффекты.
16. Начинается финальный побег.
17. Если команда спасается — добыча доставлена в хаб.
18. Если команда полностью погибает — часть/вся временная добыча теряется.
19. В хабе игроки развиваются.
20. Следующий забег генерируется заново.

---

5. СТРУКТУРА ЗАБЕГА

Ориентир:

0–3 минуты

Вход и исследование.

3–8 минут

Бои, эксперименты, секреты, добыча.

8–10 минут

Поиск главного артефакта.

~10 минут

Получение главного артефакта.

10–16 минут

Изменённый мир и возвращение.

16–20 минут

Финальный побег.

Не превращай это в жёсткий таймер, если это ухудшает игру.

---

6. КОМНАТЫ

Ориентир:

12–16 значимых комнат на забег.

Не создавай десятки маленьких бессмысленных комнат.

Типы комнат:

- combat;
- exploration;
- puzzle;
- magic experiment;
- treasure;
- secret;
- elite encounter;
- landmark;
- artifact;
- escape.

Нужны большие запоминающиеся landmark-места.

Например:

- древняя библиотека;
- разрушенный храм;
- огромный мост;
- башня;
- подземный зал;
- магическая лаборатория.

Игрок должен запоминать пространство.

---

7. ПРОЦЕДУРНАЯ ГЕНЕРАЦИЯ

Не использовать полностью случайный dungeon.

Предпочтительный подход:

контролируемый граф + модульные комнаты.

Пример:

START
↓
Combat
↓
Explore
↓
Puzzle / Secret
↓
Combat
↓
Landmark
↓
Artifact
↓
CATASTROPHE
↓
Altered rooms
↓
Escape
↓
EXIT

Но конкретные комнаты выбираются процедурно.

Использовать Seed.

Одна генерация должна быть воспроизводимой.

Необходимо разделить:

Структуру

Какие типы комнат и в каком порядке.

Контент

Какая конкретно комната используется.

Состояние

Normal / Altered / Destroyed / Burning / Corrupted и т.д.

---

8. ГЛАВНАЯ ФИШКА ГЕНЕРАЦИИ

Одна и та же комната должна иметь несколько состояний.

Например:

Forest_01_Normal

Forest_01_Burning

Forest_01_Destroyed

Forest_01_Corrupted

Bridge_01_Normal

Bridge_01_Damaged

Bridge_01_Destroyed

Village_01_Normal

Village_01_Ruined

Village_01_Burning

Это позволит создавать ощущение:

«"Я был здесь раньше."»

Но теперь:

- мост разрушен;
- дверь закрыта;
- появилась трещина;
- появилась новая опасность;
- старый путь исчез;
- появился новый путь.

Не нужно физически симулировать разрушение всего уровня.

Используй заранее подготовленные состояния и переключение объектов/вариантов.

---

9. МАГИЯ

В игре есть несколько магических направлений.

Для прототипа достаточно:

- Fire;
- Ice;
- Lightning;
- Space/Teleport.

Не нужно сразу создавать десятки заклинаний.

Основные характеристики:

HP = 100

Mana = 100

Можно иметь Stamina около 100, если она нужна боевой системе.

---

10. НЕСТАБИЛЬНАЯ МАГИЯ

Магия должна иногда вести себя неожиданно.

Но:

«НЕ превращай игру в бессмысленный RNG.»

Игрок должен постепенно понимать закономерности.

Пример Fireball:

Первый раз:

Fireball неожиданно отскакивает.

Второй раз:

игрок замечает закономерность.

Третий раз:

игрок специально стреляет в стену, чтобы получить рикошет.

То есть:

ошибка → наблюдение → понимание → мастерство.

---

11. МУТАЦИИ

Не создавай сразу сложную систему из сотен комбинаций.

Для первого прототипа:

5–10 мутаций.

Примеры:

Ricochet

Заклинание отскакивает.

Split

После столкновения разделяется.

Burn

Оставляет огонь.

Explosion

Взрывается.

Echo

Повторяет заклинание.

Chain

Переходит на другую цель.

Overcharge

Более сильная версия, но выше нестабильность.

Seeking

Немного корректирует направление.

Portal

Может взаимодействовать с порталами.

Unstable

Получает непредсказуемое поведение.

Предложи лучшую структуру мутаций после анализа прототипа.

---

12. ВЗАИМОДЕЙСТВИЕ МАГИИ С МИРОМ

Мир должен реагировать на магию.

Но не нужен настоящий physics simulator.

Используй подготовленные взаимодействия.

Примеры:

Fire → дерево горит.

Ice → вода замерзает.

Lightning → механизм активируется.

Explosion → слабая конструкция разрушается.

Wind → объект отбрасывается.

Teleport → изменение маршрута.

Water + Lightning → электрическая поверхность.

Fire + Water → пар.

Ice + Lightning → электрическая ледяная зона.

Система должна быть data-driven.

---

13. МИР ЗАПОМИНАЕТ ДЕЙСТВИЯ

Не создавай десятки сложных глобальных переменных.

Для первого прототипа используй несколько показателей.

Например:

FireScore

IceScore

LightningScore

SpaceScore

ChaosScore

Они увеличиваются во время забега.

Пример:

обычный Fireball:

FireScore +1

сильный взрыв:

ChaosScore +3

разрушение объекта:

ChaosScore +2

нестабильный артефакт:

ChaosScore +5

---

14. КАТАСТРОФА

Катастрофа начинается после получения главного артефакта.

Главный артефакт должен быть одновременно:

- наградой;
- причиной катастрофы;
- причиной изменения мира.

Не использовать одну и ту же катастрофу всегда.

Определить её на основании поведения игроков.

Например:

FireScore высокий:

Fire Catastrophe

LightningScore высокий:

Storm Catastrophe

SpaceScore высокий:

Spatial Collapse

ChaosScore высокий:

Magical Collapse

Если показатели близкие:

Mixed Catastrophe

---

15. КАТАСТРОФА НЕ ДОЛЖНА БЫТЬ ПОЛНОЙ ФИЗИКОЙ

Не пытайся разрушать весь уровень в реальном времени.

Используй:

RoomState.

Например:

Normal → Burning

Normal → Destroyed

Normal → Corrupted

Normal → Flooded

Normal → Frozen

Normal → Collapsed

Игрок должен видеть убедительный результат.

Техническая реализация должна быть максимально простой и надёжной.

---

16. ФАЗА ПОБЕГА

После получения главного артефакта:

Exploration Mode заканчивается.

Начинается:

Escape Mode.

Команда должна вернуться:

B → B' → A'

Но маршрут уже изменён.

Примеры:

До:

Forest → Bridge → Village

После:

Burning Forest → Destroyed Bridge → Ruined Village

Некоторые маршруты закрываются.

Некоторые новые маршруты появляются.

Некоторые секреты становятся доступны только после катастрофы.

---

17. ПОБЕГ ДОЛЖЕН БЫТЬ ДИНАМИЧЕСКИМ

Не просто:

«"беги 5 минут".»

Мир постепенно становится опаснее.

Например:

0–30 секунд:

- визуальные изменения;
- мелкие разрушения.

30–90:

- новые враги;
- закрытие путей.

90–180:

- большие разрушения;
- опасные зоны;
- изменение маршрута.

Финал:

последний рывок к выходу.

Не обязательно использовать строгий countdown.

Лучше постепенно увеличивать давление.

---

18. АРТЕФАКТЫ

Обычные артефакты:

5–8 за забег.

Главный:

1 за забег.

Артефакты должны не только давать +урон.

Они могут менять правила игры.

Примеры:

Heart of Fire:

+Fire power

+Burn interactions

увеличивает FireScore.

Eye of Space:

создаёт нестабильные порталы.

Ice Idol:

замораживает воду.

Forbidden Artifact:

огромная награда, но резко увеличивает Chaos.

---

19. РИСК / НАГРАДА

Игроки должны иметь возможность рисковать.

Например:

После нахождения ценного артефакта можно:

Уйти

Меньше награды.

Продолжить

Больше артефактов.

Открыть Forbidden Zone

Очень большая награда.

Но:

больше Chaos;

более сложная катастрофа;

сложнее побег.

---

20. СМЕРТЬ

Игрок при потере HP переходит в:

DOWNED

Напарник может поднять его.

Окно:

~30 секунд.

Если никто не поднял:

игрок погибает.

Не нужно мгновенно исключать игрока из игры.

Рассмотри:

- ограниченное количество revive;
- штраф за смерть;
- временное возвращение;
- spectator/ghost режим.

Выбери вариант, который лучше подходит кооперативу.

Если погибла вся команда:

Run Failed.

---

21. ПОТЕРИ

Разделить прогрессию на:

Run Progress

Теряется при провале:

- временное золото;
- временная добыча;
- временные усиления;
- часть найденных ресурсов.

Permanent Progress

Сохраняется:

- открытые заклинания;
- персонажи;
- мутации;
- постоянные артефакты;
- улучшения хаба;
- косметика;
- достижения;
- открытые биомы.

Главный принцип:

«Игрок должен потерять награду, но не ощущение прогресса.»

---

22. ПРОГРЕССИЯ

Не делать бесконечный вертикальный power creep.

Не:

+5% damage

+10% damage

+20% damage

Лучше:

Horizontal Progression.

Игрок получает:

- новые заклинания;
- новые мутации;
- новые способы взаимодействия;
- новые артефакты;
- новые персонажи;
- новые биомы;
- новые варианты катастроф;
- новые эксперименты.

Игрок становится сильнее прежде всего потому, что:

«он лучше понимает систему.»

---

23. КООПЕРАЦИЯ

Четыре игрока должны усиливать друг друга.

Примеры:

Fire + Wind → распространение огня.

Water + Lightning → электрическая зона.

Ice + Lightning → замороженная электрическая область.

Teleport + Explosion → взрыв через портал.

Fire + Water → Steam.

Игроки также могут случайно мешать друг другу.

Например:

Игрок 1:

"Я сейчас аккуратно взорву стену."

Игрок 2:

"Не надо."

Игрок 1:

взрыв

Игрок 3:

"ПОЧЕМУ ОНО ПРИЛЕТЕЛО В МЕНЯ?!"

Такие моменты должны естественно создавать клипы для TikTok/YouTube/Twitch.

---

24. ПЕРСОНАЖИ

Не обязательно делать классическую систему классов.

Можно иметь персонажей с различными магическими особенностями.

Например:

Fire-focused

Ice-focused

Space-focused

Lightning-focused

Но игрок не должен быть жёстко привязан к одному типу.

Главное — экспериментирование.

---

25. БОССЫ

Не использовать обычный:

«большой враг + 50000 HP.»

Босс должен заставлять использовать основную механику игры.

Примеры:

Artifact Guardian

Его невозможно нормально убить.

Нужно заставить его разрушить арену.

Spell Mimic

Копирует заклинания игроков.

Corrupted Mage

Использует ошибки игроков против них.

---

26. СЕКРЕТЫ

Некоторые секреты должны существовать в разных состояниях мира.

Normal:

стена целая.

Catastrophe:

стена разрушена → появляется секретная комната.

Или наоборот.

Это должно награждать игроков за то, что они запоминают карту.

---

27. ХАБ

После забега игроки возвращаются в небольшой магический hub.

В нём:

- лаборатория;
- библиотека;
- тренировочная зона;
- хранилище;
- NPC;
- магазин;
- артефактная комната.

Хаб развивается по мере прогресса.

---

28. ЭКОНОМИКА

Не перегружать валютами.

Для первой версии достаточно:

Gold

+ 

Rare Materials

+ 

Artifacts

Не делать 10 разных валют.

---

29. ВИЗУАЛ

Стиль:

Stylized Fantasy Adventure.

Нужно сочетание:

- красивого fantasy;
- читаемых форм;
- выразительной магии;
- умеренно тёмной атмосферы;
- не реализма;
- не low-poly;
- не hand-painted cartoon.

Мир должен хорошо выглядеть на Steam screenshots и видео.

Особенно важны:

- магия;
- катастрофа;
- разрушенные версии локаций;
- артефакты;
- необычные моменты кооператива.

---

30. ЗВУК

Не игнорировать:

- spell sounds;
- impact;
- environment;
- destruction;
- magic ambience;
- footsteps;
- enemy sounds;
- UI;
- music.

Особенно важен звук момента:

главный артефакт → катастрофа.

Он должен быть запоминающимся.

---

31. VFX

VFX — одна из ключевых частей игры.

Особенно:

- Fireball;
- explosions;
- portals;
- lightning;
- ice;
- corruption;
- world collapse;
- destruction;
- artifact activation.

Даже простой gameplay с хорошим VFX должен выглядеть дорого.

---

32. UI

Минимальный HUD:

- HP;
- Mana;
- Stamina;
- выбранное заклинание;
- cooldown;
- состояние игрока;
- состояние команды;
- важный статус артефакта.

Не перегружать экран.

---

33. ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ

Unity.

C#.

Online 4-player co-op.

Архитектура должна быть:

- modular;
- data-driven;
- network-aware;
- scalable;
- testable.

Использовать ScriptableObjects там, где это действительно полезно:

- spells;
- mutations;
- artifacts;
- rooms;
- enemies;
- events;
- loot;
- characters.

Не создавать один огромный GameManager.

---

34. СЕТЕВАЯ АРХИТЕКТУРА

Все важные игровые состояния должны корректно синхронизироваться.

Особенно:

- player position;
- HP;
- mana;
- spells;
- projectiles;
- spell effects;
- enemies;
- pickups;
- artifacts;
- room state;
- catastrophe;
- world changes;
- escape state.

Не делать систему, которая сначала работает только в singleplayer, а потом пытается "прикрутить multiplayer".

Multiplayer учитывать с самого начала.

---

35. MVP

Не пытайся сразу создать всю игру.

Первый прототип должен содержать:

1 биом

8 типов комнат

4 игрока

3 заклинания

5 мутаций

3 типа врагов

3 обычных артефакта

1 главный артефакт

1 катастрофу

Normal / Catastrophe состояния комнат

Escape phase

базовый hub

Этого достаточно, чтобы понять:

«интересно ли играть в основную петлю.»

---

36. ПЕРВЫЙ VERTICAL SLICE

После MVP:

1. Полноценный небольшой биом.
2. 15–20 минут gameplay.
3. Несколько вариантов генерации.
4. Несколько катастроф.
5. Нормальный VFX.
6. Sound design.
7. UI.
8. Полноценный 4-player co-op.
9. Хаб.
10. Прогрессия.

Только после этого увеличивать количество контента.

---

37. ЧЕГО НЕ ДЕЛАТЬ

Не добавлять без необходимости:

- огромный open world;
- 50 валют;
- сотни заклинаний;
- MMO-системы;
- сложный crafting;
- полноценную физику разрушения;
- огромную сюжетную кампанию;
- PvP;
- десятки классов;
- процедурную генерацию абсолютно всего;
- сложную permanent progression;
- бесконечные случайные модификаторы.

Главный приоритет:

«одна очень сильная игровая петля.»

---

38. ПОРЯДОК РАЗРАБОТКИ

Разрабатывать в таком порядке:

Phase 1 — Movement

Игрок:

- ходит;
- прыгает;
- взаимодействует.

Phase 2 — Combat

- 1 заклинание;
- враг;
- damage;
- HP;
- смерть.

Phase 3 — Multiplayer

- 2–4 игрока;
- синхронизация;
- revive.

Phase 4 — Rooms

- модульные комнаты;
- room graph;
- seed;
- генерация.

Phase 5 — Magic System

- несколько заклинаний;
- interactions;
- mutations.

Phase 6 — Artifacts

- loot;
- обычные артефакты;
- главный артефакт.

Phase 7 — World State

Normal → Catastrophe.

Phase 8 — Escape

B → B' → A'.

Phase 9 — Hub

Progression.

Phase 10 — Polish

- VFX;
- SFX;
- UI;
- animation;
- lighting;
- feedback.

---

39. ТВОЯ ЗАДАЧА КАК AI

Не просто писать код по запросу.

Ты должен выступать как технический партнёр проекта.

Перед реализацией каждой крупной системы:

1. Проверь существующую архитектуру проекта.
2. Найди уже существующие системы.
3. Не создавай дубликаты.
4. Проверь зависимости.
5. Определи, как новая система повлияет на multiplayer.
6. Определи, как она будет расширяться.
7. Предложи минимальную реализацию.
8. Только после этого реализуй.

Когда изменяешь систему:

проверь весь проект на связанные зависимости.

Не ломай существующий функционал.

---

40. ОСОБЕННО ВАЖНО

Если ты видишь возможность сделать механику проще — предложи её.

Если система слишком большая для solo developer — скажи об этом.

Если механика не добавляет веселья — предложи удалить её.

Не пытайся впечатлить количеством кода.

Цель:

«создать небольшую, но очень необычную кооперативную игру, в которой каждый забег создаёт историю.»

---

41. ГЛАВНЫЙ ДИЗАЙН-ПРИНЦИП

Каждый забег должен создавать истории вроде:

«"Мы нашли артефакт."»

«"Потом я случайно поджёг лес."»

«"Потом мост разрушился."»

«"Мы думали, что знаем дорогу обратно."»

«"Но там уже всё было уничтожено."»

«"Мы вспомнили, что оставили портал."»

«"И в последний момент через него спаслись."»

Если gameplay способен регулярно создавать такие истории — игра работает.

Если игрок просто:

«вошёл → убил врагов → забрал предмет → вышел»

то система недостаточно интересная.

---

42. КОНЕЧНАЯ ЦЕЛЬ

Создать игру, где:

Ошибка превращается в механику.

Магия меняет мир.

Первая половина забега создаёт вторую.

Игроки запоминают локацию.

Катастрофа ломает их план.

Побег проверяет, насколько хорошо они адаптировались.

И каждый забег способен породить собственную историю.

---

43. ПЕРЕД НАЧАЛОМ РАЗРАБОТКИ

Не начинай сразу писать тысячи строк кода.

Сначала:

1. Проанализируй весь проект.
2. Определи текущую архитектуру.
3. Составь технический план.
4. Определи MVP.
5. Выдели системы и зависимости.
6. Найди потенциальные проблемы multiplayer.
7. Предложи структуру папок и классов.
8. Предложи порядок реализации.
9. Отдельно укажи, какие решения пока лучше оставить гибкими.
10. После этого начинай реализацию поэтапно.

Каждый этап должен быть проверяемым.

После каждого крупного этапа:

- проверить компиляцию;
- проверить ошибки;
- проверить зависимости;
- проверить multiplayer;
- проверить существующий функционал;
- исправить найденные проблемы.

Не переходить к следующему крупному этапу, пока предыдущий не находится в рабочем состоянии.

КРИТЕРИЙ УСПЕХА

Через несколько итераций должен существовать playable prototype:

4 игрока → процедурная локация → исследование → нестабильная магия → артефакты → главный артефакт → катастрофа → изменённые комнаты → побег → награда → хаб → следующий забег.

Если этот цикл уже интересен без красивых ассетов — фундамент игры правильный.




ДОПОЛНЕНИЕ К MASTER PROMPT

Этот документ является продолжением предыдущего MASTER PROMPT.

Все решения из предыдущего документа сохраняются.

Теперь необходимо дополнить проект системами, которые необходимы для полноценной коммерческой игры.

Не воспринимай этот документ как обязательство реализовать всё сразу.

Сначала спроектируй системы, затем реализуй их поэтапно.

Главный принцип:

«НЕ ДОБАВЛЯТЬ СЛОЖНОСТЬ РАДИ СЛОЖНОСТИ.»

Если система не нужна для основной игровой петли — предложи её убрать или отложить.

---

1. ПОЛНАЯ БОЕВАЯ СИСТЕМА

Необходимо спроектировать полноценный combat framework.

Должны быть:

- damage;
- healing;
- armor/resistance;
- elemental damage;
- status effects;
- knockback;
- stagger;
- interrupt;
- death;
- invulnerability frames;
- cooldown;
- mana cost;
- AoE;
- projectile;
- hitscan, если понадобится;
- collision;
- friendly fire;
- critical effects, если они нужны;
- environmental damage.

Все значения должны быть data-driven.

Не зашивать баланс непосредственно в код.

Например:

SpellData
EnemyData
StatusEffectData
DamageType
MutationData
ArtifactData

---

2. FRIENDLY FIRE

Это важная часть игры.

Рассмотреть возможность:

- полностью отключить friendly fire;
- слабый friendly fire;
- полный friendly fire.

Для основной версии предпочтительно:

ограниченный friendly fire.

Игроки могут мешать друг другу, но случайная ошибка не должна постоянно уничтожать команду.

Особенно контролировать:

- Explosion;
- Fire;
- Lightning;
- Knockback;
- environmental hazards.

---

3. ВРАГИ

Создать базовую систему Enemy Framework.

Типы:

Basic

Простой враг.

Ranged

Атакует издалека.

Melee

Агрессивно сближается.

Support

Усиливает других.

Elite

Имеет особую механику.

Anomaly

Взаимодействует с нестабильной магией.

Boss

Использует основные механики игры.

---

4. AI ВРАГОВ

AI должен учитывать:

- игроков;
- дистанцию;
- line of sight;
- агро;
- угрозу;
- препятствия;
- состояние комнаты;
- опасные зоны;
- магические эффекты.

Не создавать чрезмерно сложный AI.

Лучше:

простая, стабильная AI-система + хорошо спроектированные behaviours.

---

5. МАСШТАБИРОВАНИЕ НА 1–4 ИГРОКОВ

Одна из обязательных систем.

Игра должна нормально работать при:

1 игроке

2 игроках

3 игроках

4 игроках

Не просто увеличивать HP врагов.

Масштабировать:

- количество врагов;
- типы врагов;
- элитов;
- loot;
- опасность;
- cooldowns некоторых событий;
- количество ресурсов.

Но не делать 4-player режим в 4 раза тяжелее.

---

6. LOOT SYSTEM

Нужна полноценная система добычи.

Категории:

- Gold;
- Materials;
- Artifacts;
- Temporary Buffs;
- Rare Items;
- Main Artifact.

Редкость:

- Common;
- Uncommon;
- Rare;
- Epic;
- Legendary;
- Forbidden.

Но не перегружать игрока редкостями.

Каждый предмет должен иметь понятную ценность.

---

7. LOOT TABLES

Loot должен зависеть от:

- типа комнаты;
- сложности;
- риска;
- элитных врагов;
- секретов;
- текущего этапа забега;
- количества игроков;
- выбранных curse/modifiers.

Loot tables должны быть data-driven.

Не писать:

if(random < 0.05f)

в разных местах проекта.

Создать единую систему:

LootTable
LootEntry
DropChance
Rarity
Weight
Condition

---

8. СУНДУКИ И НАГРАДЫ

Добавить:

- обычные сундуки;
- редкие сундуки;
- секретные сундуки;
- награды за elite;
- награды за puzzle;
- награды за риск.

Сундуки не должны превращаться в одинаковый animation + random item.

Разные типы сундуков должны иметь разные ожидания игрока.

---

9. SPELL FRAMEWORK

Заклинания должны быть отдельной расширяемой системой.

Минимально:

SpellData
SpellBehaviour
SpellProjectile
SpellEffect
SpellCost
SpellCooldown
SpellMutation
SpellInteraction

Новый spell должен добавляться без переписывания основной combat system.

---

10. STATUS EFFECTS

Создать общую систему:

- Burning;
- Frozen;
- Electrified;
- Wet;
- Corrupted;
- Stunned;
- Slowed;
- Teleported;
- Marked.

Эффекты должны иметь:

- duration;
- stack;
- intensity;
- source;
- target;
- VFX;
- SFX.

---

11. MAGIC INTERACTION SYSTEM

Это одна из ключевых систем игры.

Не создавать десятки hardcoded:

if Fire + Water...
if Fire + Ice...

Сделать data-driven interaction framework.

Пример:

Interaction:
Fire + Water
Result:
Steam

Interaction:
Lightning + Water
Result:
ElectrifiedWater

Interaction:
Fire + Wind
Result:
SpreadFire

Система должна позволять добавлять новые взаимодействия через data.

---

12. WORLD REACTION SYSTEM

Объекты мира должны иметь свойства.

Например:

Flammable
Freezable
Conductive
Breakable
Explosive
Teleportable
Magical

Заклинание взаимодействует со свойством.

Например:

Fire → Flammable

Lightning → Conductive

Ice → Freezable

Explosion → Breakable

Это намного лучше, чем делать отдельный код для каждого объекта.

---

13. WORLD STATE SYSTEM

Создать центральную систему состояния мира.

Например:

WorldState
 ├── Normal
 ├── Catastrophe
 └── Escape

А комнаты:

RoomState
 ├── Normal
 ├── Damaged
 ├── Burning
 ├── Frozen
 ├── Corrupted
 └── Destroyed

Катастрофа должна менять состояния комнат.

---

14. CATASTROPHE DIRECTOR

Создать отдельный контроллер:

Catastrophe Director

Он получает:

FireScore
IceScore
LightningScore
SpaceScore
ChaosScore
MainArtifact
RoomHistory

и выбирает подходящую катастрофу.

Он определяет:

- тип катастрофы;
- интенсивность;
- изменённые комнаты;
- новые враги;
- опасные зоны;
- закрытые проходы;
- новые проходы;
- события побега.

Не делать это одним огромным if/else.

---

15. ESCAPE DIRECTOR

Отдельная система:

Escape Director

Она управляет второй половиной забега.

После катастрофы:

- меняет room states;
- открывает/закрывает проходы;
- активирует hazards;
- создаёт pressure;
- запускает события;
- управляет финальным выходом.

Escape должен ощущаться как отдельная фаза игры.

---

16. ROOM HISTORY

Игра должна помнить:

- какие комнаты посетили;
- какие секреты открыли;
- какие объекты разрушили;
- какие магические события произошли;
- какие артефакты были найдены;
- какие состояния должны быть применены после катастрофы.

Но не хранить абсолютно всё.

Сохранять только данные, которые нужны для изменения мира.

---

17. PROCEDURAL GENERATION SYSTEM

Создать отдельный генератор.

Пример:

RunSeed
↓
RoomGraph
↓
RoomSelection
↓
EncounterSelection
↓
LootSelection
↓
SecretPlacement
↓
LandmarkPlacement
↓
MainArtifact

Генерация должна быть:

- reproducible;
- deterministic, где это возможно;
- network-safe;
- testable.

Один seed должен создавать одинаковый layout.

---

18. GENERATION VALIDATION

После генерации обязательно проверять:

- есть ли путь START → ARTIFACT;
- есть ли путь ARTIFACT → EXIT;
- нет ли soft-lock;
- нет ли недоступных обязательных комнат;
- нет ли слишком длинного маршрута;
- нет ли пустого забега;
- есть ли необходимое количество rewards;
- корректно ли работает escape route.

Если генерация неправильная:

reroll seed / regenerate.

---

19. RUN DIRECTOR

Создать систему, которая управляет забегом целиком.

Пример:

Preparing
↓
Exploration
↓
Artifact Hunt
↓
Artifact Obtained
↓
Catastrophe
↓
Escape
↓
Extraction
↓
Run Complete

Все основные системы должны знать текущую фазу забега.

---

20. РИСКОВЫЕ МОДИФИКАТОРЫ ЗАБЕГА

Добавить систему optional modifiers.

Перед забегом команда может выбрать риск.

Например:

Unstable Magic

Заклинания менее стабильны.

Награда:

+25%

Fragile World

Больше разрушаемых объектов.

Награда:

+20%

Magical Storm

Больше Lightning events.

Награда:

+30%

Forbidden Expedition

Сложнее враги.

Награда:

+50%

Не добавлять много modifiers на старте.

Для MVP достаточно 3–5.

---

21. ПРОГРЕССИЯ

Разделить:

Account Progression

Сохраняется между забегами.

Run Progression

Существует только внутри текущего забега.

Knowledge Progression

Игрок сам учится системе.

Это очень важно.

Knowledge Progression является одной из главных особенностей игры.

---

22. HUB PROGRESSION

Хаб должен иметь реальные функции.

Например:

Library

Новые spells.

Laboratory

Mutations.

Artifact Chamber

Работа с артефактами.

Training Area

Тестирование магии.

Workshop

Дополнительные улучшения.

NPC Area

Персонажи/сюжет.

Не добавлять здания просто ради декора.

---

23. CHARACTERS

Если будут разные персонажи:

Каждый должен иметь:

- identity;
- visual;
- voice/personality;
- passive;
- starting spell/loadout;
- progression.

Но не делать 20 персонажей.

Для первой версии:

4 персонажа.

---

24. LOADOUT

Перед забегом игрок выбирает:

- character;
- starting spell;
- optional modifier;
- cosmetic.

Не давать игроку слишком много выбора в начале.

---

25. DEATH / REVIVE

Полностью спроектировать:

- Downed;
- Revive;
- Revive timer;
- Revive interruption;
- Death;
- Spectator;
- Team wipe.

Дополнительно:

Disconnect during downed

Player reconnect

Player leaves

Host leaves

Все эти случаи должны иметь понятное поведение.

---

26. NETWORKING

Multiplayer должен быть спроектирован с самого начала.

Определить:

- authority;
- ownership;
- server-side validation;
- replication;
- prediction;
- interpolation;
- network spawning;
- network destruction;
- networked room state;
- networked catastrophe;
- networked loot;
- networked enemies.

Не доверять клиенту критические данные:

- Gold;
- Damage;
- Loot;
- Artifact ownership;
- Progression.

---

27. LOBBY

Нужны:

- Create Lobby;
- Join Lobby;
- Invite Friend;
- Ready;
- Character Select;
- Start Run;
- Leave Lobby.

Steam friend invite должен быть предусмотрен архитектурой.

---

28. DISCONNECT / RECONNECT

Продумать:

Если игрок отключился:

- его персонаж остаётся в мире ограниченное время;
- команда может продолжать;
- игрок может reconnect.

Если игрок не вернулся:

- его временная добыча обрабатывается по правилам;
- забег не должен ломаться.

---

29. SAVE SYSTEM

Создать отдельную Save System.

Сохранять:

- unlocked content;
- characters;
- upgrades;
- artifacts;
- cosmetics;
- settings;
- achievements;
- statistics.

Не сохранять состояние текущей комнаты как постоянный прогресс, если это не требуется.

---

30. SAVE SAFETY

Обязательно:

- version number;
- migration;
- backup;
- corruption protection;
- validation.

Пример:

Save Version 1
Save Version 2
Save Version 3

При обновлении игры старые saves должны мигрировать.

---

31. SETTINGS

Обязательно:

Graphics

- resolution;
- fullscreen;
- quality;
- FPS limit;
- VSync;
- shadows;
- effects.

Audio

- master;
- music;
- SFX;
- voice;
- UI.

Controls

- keyboard;
- mouse;
- controller;
- rebinding.

Gameplay

- sensitivity;
- FOV;
- subtitles;
- camera options.

---

32. ACCESSIBILITY

Минимально предусмотреть:

- subtitles;
- subtitle size;
- colorblind-friendly effects;
- screen shake toggle;
- camera shake toggle;
- motion blur toggle;
- FOV;
- mouse sensitivity;
- controller sensitivity;
- key rebinding;
- hold/toggle options.

---

33. ONBOARDING

Игрок не должен читать 20 страниц текста.

Создать короткий tutorial.

Он должен научить:

1. Movement.
2. Spell.
3. Mana.
4. Interaction.
5. Artifact.
6. Catastrophe.
7. Escape.
8. Revive.

Tutorial должен занимать:

5–10 минут максимум.

Можно сделать tutorial отдельным безопасным dungeon.

---

34. UX

Все важные действия должны иметь feedback:

- sound;
- VFX;
- animation;
- UI;
- camera feedback.

Игрок должен понимать:

«почему произошло событие.»

Особенно:

- почему заклинание изменилось;
- почему объект разрушился;
- почему началась катастрофа;
- почему путь закрылся;
- куда бежать.

---

35. AUDIO SYSTEM

Создать audio architecture.

Не вызывать AudioClip напрямую из сотен скриптов.

Использовать:

AudioEvent
AudioManager
Mixer
AudioGroups

Поддержать:

- 3D sound;
- spatial audio;
- ambience;
- combat;
- spells;
- UI;
- music;
- catastrophe music.

---

36. MUSIC SYSTEM

Музыка должна меняться между фазами:

Exploration

Спокойная fantasy.

Danger

Повышение напряжения.

Artifact

Особая музыкальная тема.

Catastrophe

Резкое изменение.

Escape

Динамичная музыка.

Extraction

Разрядка.

---

37. VFX SYSTEM

Создать reusable VFX architecture.

VFX должны быть:

- pooled;
- network-aware;
- scalable;
- configurable.

Не создавать новый уникальный код для каждого эффекта.

---

38. OBJECT POOLING

Использовать pooling там, где это действительно необходимо:

- projectiles;
- VFX;
- common enemies;
- damage effects;
- pickups.

Не создавать/уничтожать сотни объектов каждый кадр.

---

39. PERFORMANCE

Цель:

стабильный FPS во время хаоса.

Особенно проверить:

- 4 players;
- dozens of enemies;
- spell spam;
- VFX;
- destruction;
- network traffic.

Избегать:

- FindObjectOfType в Update;
- excessive Instantiate/Destroy;
- лишних allocations;
- огромного количества Update;
- неконтролируемых particle systems.

---

40. LOADING

Продумать:

- main menu;
- hub;
- dungeon;
- loading;
- return to hub.

Не загружать всю игру одновременно, если это не требуется.

---

41. CAMERA

First-person camera должна иметь:

- FOV;
- sensitivity;
- head movement;
- recoil;
- spell feedback;
- damage feedback;
- camera shake.

Все эффекты должны иметь возможность отключаться.

---

42. ANIMATION

Даже для first-person игры нужны:

- hands;
- spell casting;
- interaction;
- revive;
- pickup;
- damage;
- death;
- enemy animations.

Сделать animation system расширяемой.

---

43. UI ARCHITECTURE

Разделить:

MainMenu
Lobby
HUD
Inventory
ArtifactScreen
Map
Settings
Pause
Results
Hub
Shop
Progression

Не создавать один огромный UI Manager.

---

44. RUN RESULTS

После успешного забега показать:

- найденные артефакты;
- золото;
- rare loot;
- deaths;
- revives;
- spells used;
- catastrophe type;
- chaos level;
- time;
- secrets;
- bonus rewards.

Это также может создавать хорошие моменты для друзей.

---

45. STATISTICS

Хранить интересные статистические данные:

- total runs;
- successful runs;
- deaths;
- revives;
- artifacts;
- damage;
- spells;
- catastrophe types;
- secrets;
- friendly fire incidents;
- biggest explosion;
- longest escape.

Не обязательно всё выводить игроку сразу.

---

46. ACHIEVEMENTS

Steam achievements должны быть основаны на интересных ситуациях.

Например:

"Это было специально"

Успешно использовать рикошетное заклинание для убийства врага.

"БЕГИ!"

Успешно завершить escape после высокой Chaos.

"Мы почти умерли"

Спастись с минимальным HP.

"Никогда больше"

Пережить Forbidden Expedition.

Achievements должны стимулировать экспериментирование.

---

47. STEAM

Предусмотреть:

- Steam authentication;
- Steam friends;
- invites;
- achievements;
- Steam Cloud;
- rich presence;
- overlay;
- controller support;
- Steam Deck compatibility.

Не писать Steam integration непосредственно в gameplay classes.

Использовать abstraction layer.

---

48. LOCALIZATION

Минимально подготовить:

- English;
- Russian.

Но архитектура должна позволять добавлять другие языки.

Никакого текста непосредственно в коде.

Использовать localization keys.

---

49. CONTENT PIPELINE

Очень важный раздел.

Добавление нового контента должно быть максимально простым.

Например:

Новый Spell

Create SpellData
→ configure
→ add VFX
→ add SFX
→ add mutations
→ add interactions
→ add localization
→ test multiplayer.

Новый Artifact

Create ArtifactData
→ effects
→ rarity
→ loot table
→ VFX
→ SFX
→ catastrophe influence
→ localization
→ test.

Новая Room

Create Room
→ define tags
→ define exits
→ define encounters
→ define loot
→ define Normal state
→ define Catastrophe state
→ validation.

Новый Enemy

EnemyData
→ AI
→ attacks
→ resistances
→ loot
→ VFX
→ SFX
→ scaling.

---

50. DEBUG TOOLS

Для разработки обязательно создать debug tools.

Например:

- teleport to room;
- spawn enemy;
- spawn artifact;
- give spell;
- set Chaos;
- set FireScore;
- trigger catastrophe;
- force room state;
- regenerate seed;
- kill player;
- revive player;
- simulate 4 players.

Debug menu может существовать только в development builds.

Это значительно ускорит разработку.

---

51. AUTOMATED TESTS

Создать тесты для критических систем:

- room generation;
- path validation;
- loot;
- damage;
- spell interactions;
- mutations;
- catastrophe selection;
- save/load;
- multiplayer state;
- escape route.

Особенно:

«генерация не должна создавать soft-lock.»

---

52. QA

Перед каждым milestone проверять:

Gameplay

- movement;
- combat;
- spells;
- loot;
- artifacts;
- catastrophe;
- escape.

Multiplayer

- 1 player;
- 2 players;
- 3 players;
- 4 players;
- disconnect;
- reconnect;
- player death;
- team wipe.

Generation

- 100+ seeds;
- no soft-lock;
- reachable artifact;
- reachable exit.

Performance

- low-end PC;
- 4 players;
- many enemies;
- many VFX.

---

53. BUG REPORTING

Добавить систему development logging.

Каждая критическая система должна иметь понятные logs.

Например:

[RUN]
Seed: 284913

[ARTIFACT]
Main Artifact: HeartOfFire

[CATASTROPHE]
Type: Fire
Chaos: 68

[ESCAPE]
Route generated successfully

Это сильно упростит debugging.

---

54. CRASH / TELEMETRY

Для production предусмотреть:

- crash reporting;
- error logging;
- performance data;
- network errors.

Не собирать ненужные персональные данные.

---

55. LEGAL / ASSETS

Для каждого внешнего ассета хранить:

- source;
- license;
- commercial-use permission;
- author;
- version;
- modification rights.

Нельзя использовать ассеты, если лицензия не позволяет коммерческое использование.

То же самое:

- music;
- sound effects;
- fonts;
- VFX;
- textures;
- animations;
- code libraries.

---

56. BUILD PIPELINE

Должны существовать отдельные builds:

Development
Testing
Demo
Release

Перед Steam build:

- clean build;
- validate scenes;
- validate assets;
- validate localization;
- validate save;
- validate Steam integration;
- validate multiplayer.

---

57. CONTENT VALIDATION

Создать editor tools, которые находят:

- missing references;
- missing VFX;
- missing SFX;
- invalid room exits;
- invalid loot tables;
- missing localization;
- duplicate IDs;
- invalid ScriptableObjects.

---

58. ПОДГОТОВКА К РАСШИРЕНИЮ

Архитектура должна позволять после релиза добавлять:

- новые биомы;
- новые комнаты;
- новые spells;
- новые mutations;
- новые artifacts;
- новые enemies;
- новые catastrophes;
- новых персонажей.

Без переписывания core systems.

---

59. НЕ ДОБАВЛЯТЬ ПОКА

До рабочего MVP НЕ делать:

- огромный crafting;
- guilds;
- PvP;
- open world;
- 100+ персонажей;
- battle pass;
- daily quests;
- сложную социальную систему;
- огромную сюжетную кампанию;
- MMO features.

Сначала доказать, что основная петля работает.

---

60. ФИНАЛЬНАЯ ПРОВЕРКА ПРОЕКТА

Перед релизом игра должна отвечать:

Можно ли начать игру за несколько кликов?

Можно ли легко пригласить друзей?

Понимает ли игрок магию?

Понимает ли игрок, почему мир изменился?

Есть ли смысл исследовать?

Есть ли риск?

Есть ли награда?

Отличаются ли забеги?

Есть ли причины переигрывать?

Есть ли интересные моменты для друзей?

Может ли игрок рассказать историю о своём забеге?

Не ломается ли игра при 4 игроках?

Можно ли добавить новый контент без переписывания архитектуры?

---

61. PRODUCTION MILESTONES

Разрабатывать проект по этапам:

M0 — Technical Foundation

- Unity project;
- architecture;
- networking;
- input;
- player;
- save;
- debug tools.

M1 — Combat Prototype

- player;
- 3 spells;
- enemies;
- damage;
- mana;
- death;
- revive.

M2 — Multiplayer Prototype

- 4 players;
- synchronization;
- lobby;
- disconnect;
- reconnect.

M3 — Procedural Prototype

- room graph;
- seed;
- 8 room types;
- validation.

M4 — Core Gameplay

- loot;
- artifacts;
- main artifact;
- world state;
- catastrophe;
- escape.

M5 — Vertical Slice

- complete 15–20 minute run;
- VFX;
- SFX;
- UI;
- animation;
- hub;
- progression.

M6 — Content Production

- additional rooms;
- enemies;
- spells;
- artifacts;
- mutations;
- catastrophes;
- biomes.

M7 — Alpha

Полный gameplay loop без критических системных проблем.

M8 — Beta

Баланс + QA + multiplayer testing + optimization.

M9 — Release Candidate

Steam integration + localization + saves + achievements + performance + bug fixing.

M10 — Release

Steam launch.

---

62. ПРАВИЛО ДЛЯ OPENCODE

Перед написанием кода:

СНАЧАЛА ПРОВЕРЬ ПРОЕКТ.

Не предполагай, что нужной системы нет.

Ищи:

- existing classes;
- existing managers;
- ScriptableObjects;
- scenes;
- prefabs;
- packages;
- networking code;
- input system;
- UI;
- save system.

Если уже существует подходящая система:

расширяй её, а не создавай вторую.

---

63. ПРАВИЛО РЕАЛИЗАЦИИ

Для каждой задачи сначала ответь себе:

1. Что уже существует?
2. Что нужно изменить?
3. Какие системы затронуты?
4. Какие network implications?
5. Какие save implications?
6. Какие dependencies?
7. Как протестировать?
8. Как откатить изменение, если оно сломает проект?

Только после этого изменяй код.

---

64. ГЛАВНОЕ ОГРАНИЧЕНИЕ

Не превращай проект в технический эксперимент.

Игроку не важно, насколько сложна архитектура.

Ему важно:

«"Было весело."»

Поэтому при выборе между:

сложной системой + 5% дополнительного качества

и

простой системой + быстрым production

выбирай простую систему.

---

65. ФИНАЛЬНЫЙ КРИТЕРИЙ ГОТОВОЙ ИГРЫ

Готовый проект должен позволять игроку:

Запустить игру

↓

Создать/найти lobby

↓

Пригласить 1–3 друзей

↓

Выбрать персонажа

↓

Начать экспедицию

↓

Исследовать процедурную локацию

↓

Сражаться

↓

Экспериментировать с магией

↓

Находить артефакты

↓

Изменять состояние мира

↓

Получить главный артефакт

↓

Запустить катастрофу

↓

Увидеть изменившийся мир

↓

Убежать

↓

Выжить или погибнуть

↓

Получить/потерять добычу

↓

Вернуться в хаб

↓

Развить персонажа/системы

↓

Начать следующий забег.

И весь этот цикл должен работать стабильно в 1–4 player online co-op.

---

ГЛАВНАЯ ЗАДАЧА AI

Не пытайся реализовать весь проект одним огромным изменением.

Работай итеративно.

Каждая итерация должна оставлять проект в рабочем состоянии.

После каждой крупной системы:

1. Compile.
2. Run.
3. Test.
4. Check errors.
5. Check multiplayer.
6. Check dependencies.
7. Check performance.
8. Fix regressions.
9. Только после этого переходить дальше.

Главная цель:

«Не написать много кода, а постепенно довести игру до состояния полноценного коммерческого продукта.»
