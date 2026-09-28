ЗАДАЧА: СОЗДАТЬ ЕДИНЫЙ ART DIRECTION ДЛЯ ИГРЫ НА UE 5.8

Ты работаешь как Senior Art Director + Environment Artist + Technical Artist для Unreal Engine 5.8.

КОНТЕКСТ ПРОЕКТА

Я создаю PvE Soulslike / Action RPG с кооперативом до 4 игроков.

Основные визуальные ориентиры:

- Elden Ring — композиция мира, руины, масштаб, исследование;
- Dark Souls — читаемость архитектуры, атмосфера, dungeon design;
- Soulframe — более светлая fantasy-эстетика, необычные цветовые акценты;
- Project Titan от Epic Games — основной источник environment assets.

ВАЖНО:

Игра НЕ должна выглядеть как копия Elden Ring, Dark Souls или Soulframe.

Project Titan НЕ должен визуально восприниматься как готовый стиль игры.

Titan используется как основная библиотека environment assets, которую необходимо привести к единому визуальному языку нашей игры.

---

1. ЦЕЛЕВОЙ ART STYLE

Основная формула:

GROUNDed DARK FANTASY
+
STYLIZED REALISM
+
MEDIEVAL / NORTHERN / CELTIC ARCHITECTURAL INFLUENCE
+
SOULSLIKE WORLD COMPOSITION
+
SOULFRAME-LIKE COLOR ACCENTS

Стиль должен находиться между:

- realistic fantasy;
- stylized realism;
- grounded dark fantasy.

НЕ использовать:

- low-poly aesthetic;
- hand-painted aesthetic;
- cartoon style;
- overly colorful fantasy;
- ultra-photorealistic realism;
- horror aesthetic;
- чрезмерно тёмную монохромную Dark Souls-палитру.

Мир должен быть мрачным и загадочным, но не депрессивным и не хоррорным.

Игрок должен ощущать:

"древний красивый fantasy-мир, переживший катастрофу".

---

2. ОСНОВНОЙ ВИЗУАЛЬНЫЙ ПРИНЦИП

Project Titan является ОСНОВОЙ библиотекой окружения.

Не добавляй случайные ассеты только потому, что они выглядят красиво.

Каждый новый ассет должен пройти проверку:

1. Material consistency
2. Scale consistency
3. Detail density
4. Color consistency
5. Silhouette consistency
6. Architectural consistency
7. Lighting compatibility

Если ассет нарушает общий стиль — НЕ использовать его напрямую.

При необходимости:

- изменить material instance;
- изменить tint;
- изменить roughness;
- изменить saturation;
- добавить dirt;
- добавить moss;
- добавить wetness;
- изменить material variation;
- изменить decal coverage;
- изменить освещение;
- заменить ассет.

---

3. ЦВЕТОВАЯ ПАЛИТРА

Основные цвета мира:

- холодный серый камень;
- серо-бежевый;
- тёмно-коричневое дерево;
- приглушённый зелёный;
- холодный серо-синий;
- грязно-бежевые землистые оттенки.

Не использовать чрезмерно насыщенные цвета в окружении.

Яркие цвета должны быть РЕДКИМИ и использоваться преимущественно как акценты.

Акцентные цвета:

- золотой;
- янтарный;
- красный;
- голубой;
- бирюзовый;
- слабый фиолетовый.

Магия должна визуально выделяться на фоне окружения.

---

4. MATERIAL DIRECTION

Нужно создать единую систему материалов.

Если в проекте уже есть подходящие Master Materials — сначала изучи их и переиспользуй существующую систему вместо создания дубликатов.

Если требуется собственная система, создай централизованный material framework.

Предпочтительная структура:

M_Master_Surface

Параметры:

- Base Color
- Normal
- Roughness
- Metallic
- AO
- Dirt
- Moss
- Wetness
- Edge Wear
- Color Variation
- Global Tint
- Macro Variation
- Detail Normal

Создавай Material Instances:

- MI_Stone
- MI_Stone_Dark
- MI_Stone_Moss
- MI_Stone_Wet
- MI_Wood
- MI_Wood_Old
- MI_Metal
- MI_Ruin
- MI_Ground
- MI_Mud

НЕ создавай десятки почти одинаковых материалов.

Используй Material Instances и параметры.

---

5. ENVIRONMENT PRIORITY

Project Titan должен использоваться прежде всего для:

HIGH PRIORITY:

- rocks;
- cliffs;
- terrain;
- trees;
- foliage;
- grass;
- bushes;
- roots;
- stones;
- walls;
- floors;
- stairs;
- bridges;
- ruins;
- modular architecture;
- roads;
- fences;
- environmental props.

MEDIUM PRIORITY:

- houses;
- towers;
- temples;
- gates;
- carts;
- barrels;
- furniture;
- decorative objects.

LOW / SPECIAL USE:

- giant fantasy objects;
- Titan-specific objects;
- extremely recognizable fantasy structures;
- unusual giant skeletons;
- highly specific landmarks.

Последние использовать только как уникальные landmarks или специальные места.

Не повторять один и тот же уникальный объект слишком часто.

---

6. АРХИТЕКТУРА

Основной architectural language:

- средневековый;
- древний;
- североевропейский;
- Celtic influence;
- ruined fantasy;
- функциональный.

Избегай ощущения:

"Disney fantasy village".

Архитектура должна выглядеть так, будто она реально существовала в мире:

- здания должны иметь функциональное назначение;
- стены должны логично соединяться;
- лестницы должны вести куда-либо;
- двери должны иметь смысл;
- дороги должны соединять важные точки;
- мосты должны быть логичны;
- здания не должны случайно пересекаться;
- стены не должны появляться без причины.

---

7. WORLD COMPOSITION

Локации должны строиться как Soulslike.

Не создавать огромные пустые пространства только ради масштаба.

Предпочтительно:

- небольшие плотные зоны;
- вертикальность;
- shortcuts;
- landmarks;
- скрытые проходы;
- небольшие секреты;
- руины;
- небольшие арены;
- dungeon entrances;
- vistas;
- альтернативные маршруты.

Игрок должен постоянно видеть интересные направления.

Каждая крупная локация должна иметь:

1. Entrance
2. Main route
3. Secondary route
4. Landmark
5. Shortcut
6. Secret
7. Combat space
8. Exploration space
9. Dungeon / interior
10. Boss / miniboss area

---

8. LIGHTING

Lighting является частью Art Direction.

НЕ пытайся сделать весь мир тёмным.

Обычная outdoor-сцена:

- мягкий daylight;
- холодный ambient;
- читаемые материалы;
- умеренный fog.

Ruins:

- холодное окружение;
- тёплые локальные источники;
- torches;
- fires;
- candles.

Dungeon:

- ограниченный свет;
- сильный контраст;
- локальные источники;
- магические источники.

Magical locations:

- обычное окружение остаётся относительно реалистичным;
- магия создаёт цветовые акценты;
- emissive используется контролируемо.

Не использовать постоянную сильную туманную завесу.

---

9. FOLIAGE

Foliage должен выглядеть естественно.

Не заполняй всё травой.

Создавай:

- foreground;
- midground;
- background;
- vegetation clusters;
- clear paths;
- areas of exposed ground;
- damaged vegetation;
- moss;
- roots;
- fallen trees.

Оставляй пространство для gameplay.

Foliage НЕ должен мешать:

- чтению врагов;
- чтению дороги;
- navigation;
- combat;
- silhouettes.

---

10. VFX

VFX должны стать одним из главных элементов уникальности игры.

Окружение может происходить из Titan.

Но:

- magic;
- souls;
- weapon trails;
- hit effects;
- abilities;
- portals;
- checkpoints;
- magical objects;
- environmental magic

должны иметь собственный визуальный язык.

VFX должны быть более стилизованными, чем окружение.

Но не превращать игру в cartoon.

---

11. CHARACTERS

Characters могут иметь немного более выраженную стилизацию, чем environment.

Цель:

STYLIZED REALISTIC CHARACTERS.

Они должны выглядеть естественно в окружении Titan, но не обязаны быть визуально идентичными environment assets.

Особое внимание:

- silhouette;
- proportions;
- materials;
- armor;
- cloth;
- hair;
- weapons;
- color accents.

Не использовать MetaHuman как основу, если для задачи он не требуется.

---

12. УНИКАЛЬНОСТЬ ИГРЫ

Чтобы игра не выглядела как "Project Titan game", необходимо создать собственные элементы:

- уникальные checkpoints;
- уникальные shrines;
- уникальные souls;
- уникальные magical objects;
- уникальные boss arenas;
- уникальные dungeon entrances;
- уникальные doors;
- уникальные environmental storytelling props;
- собственные VFX;
- собственный UI;
- собственные персонажи;
- собственные weapons;
- собственные interactive objects.

Они должны постепенно формировать узнаваемость игры.

---

13. ПРОПОРЦИЯ ИСПОЛЬЗОВАНИЯ АССЕТОВ

Целевой ориентир:

70–80%:
Project Titan / Epic environment assets

10–20%:
дополнительные совместимые environment assets / Megascans / технические материалы

5–10%:
уникальные ассеты проекта.

Это НЕ строгий математический лимит.

Главный критерий — визуальная целостность.

---

14. PERFORMANCE

Это UE 5.8.

Не жертвуй производительностью ради визуальных эффектов.

При работе с ассетами проверяй:

- Nanite;
- LOD;
- collision;
- material complexity;
- shader complexity;
- texture memory;
- virtual textures;
- foliage density;
- shadow cost;
- VFX cost;
- Niagara particle count;
- draw calls;
- instancing;
- PCG generation cost.

Не создавай unnecessarily expensive materials.

Не добавляй дополнительные texture samples без необходимости.

Не используй уникальные материалы там, где достаточно Material Instance.

---

15. PCG

Если используется PCG:

PCG должен использоваться для:

- foliage;
- rocks;
- small props;
- debris;
- vegetation;
- environmental variation.

Но:

НЕ использовать PCG для всего мира без контроля.

Главные landmarks, здания, дороги, важные gameplay areas и dungeon entrances должны контролироваться вручную.

PCG должен создавать естественную вариативность, а не хаос.

---

16. VISUAL BENCHMARK

Создай одну небольшую тестовую локацию размером примерно на 10–15 минут прохождения.

Структура:

HUB / ENTRANCE
↓
FOREST
↓
RUINS
↓
SMALL DUNGEON
↓
MINI-BOSS

Эта локация является VISUAL BENCHMARK проекта.

Не создавай остальные крупные зоны, пока этот benchmark не выглядит целостно.

---

17. ПОСЛЕДОВАТЕЛЬНОСТЬ РАБОТЫ

Перед изменениями:

1. Просканируй проект.
2. Найди Project Titan assets.
3. Определи существующие Material Master / Material Instances.
4. Найди существующие PCG systems.
5. Найди foliage systems.
6. Найди lighting setup.
7. Найди post-process setup.
8. Найди существующие environment blueprints.
9. Определи, что уже работает.
10. НЕ создавай дубликаты существующих систем.

После анализа составь краткий отчёт:

- какие Titan assets используются;
- какие материалы уже существуют;
- какие системы можно переиспользовать;
- какие системы требуют изменений;
- какие ассеты конфликтуют со стилем;
- какие ассеты лучше исключить.

---

18. ПРАВИЛО "НЕ ЛОМАТЬ ПРОЕКТ"

Перед изменением существующей системы:

- сначала изучи зависимости;
- проверь references;
- не удаляй рабочие assets;
- не переименовывай assets без необходимости;
- не создавай дубликаты;
- не меняй gameplay systems ради визуала;
- не меняй project settings без необходимости;
- делай изменения минимально инвазивными.

Если существующая система уже решает задачу — используй её.

---

19. КРИТЕРИЙ КАЧЕСТВА

После каждой крупной итерации оценивай сцену по следующим параметрам:

ART DIRECTION
0–10

MATERIAL CONSISTENCY
0–10

COLOR CONSISTENCY
0–10

ARCHITECTURAL CONSISTENCY
0–10

ENVIRONMENT DENSITY
0–10

LIGHTING
0–10

READABILITY
0–10

SOULSLIKE ATMOSPHERE
0–10

PERFORMANCE
0–10

ASSET CONSISTENCY
0–10

Если какой-либо показатель ниже 8/10 — найди причину и исправь её.

ВАЖНО:

Не оценивай сцену субъективно по принципу "красиво".

Объясняй конкретно:

- какой объект выбивается;
- какой материал конфликтует;
- какой цвет слишком насыщенный;
- где слишком много foliage;
- где нарушен масштаб;
- где нарушена композиция;
- где освещение ломает читаемость.

---

20. ГЛАВНЫЙ ПРИНЦИП

НЕ ПЫТАЙСЯ СДЕЛАТЬ "КАК PROJECT TITAN".

Сделай:

"МИР, СОБРАННЫЙ В ОСНОВНОМ ИЗ PROJECT TITAN, НО ВЫГЛЯДЯЩИЙ КАК СОБСТВЕННАЯ ИГРА."

Project Titan — это библиотека.

Art Direction принадлежит нашей игре.

Если между красивым ассетом и единым стилем существует конфликт:

ЕДИНЫЙ СТИЛЬ ВСЕГДА ВАЖНЕЕ.

---

ФИНАЛЬНАЯ ЗАДАЧА

Сначала НЕ начинай массово менять ассеты.

Сначала:

1. Проанализируй весь доступный Project Titan content в проекте.
2. Проанализируй существующее окружение.
3. Определи текущие визуальные проблемы.
4. Создай Art Direction document внутри проекта.
5. Создай visual benchmark scene.
6. Настрой материалы.
7. Настрой lighting.
8. Настрой foliage.
9. Настрой environment composition.
10. Проверь производительность.
11. Только после этого начинай переносить этот визуальный стандарт на остальные локации.

В конце каждого этапа сообщай:

- что найдено;
- что изменено;
- почему это изменено;
- какие assets используются;
- какие assets исключены;
- какие проблемы остались;
- что делать следующим этапом.

НЕ ДЕЛАЙ РЕЗКИХ И НЕОБРАТИМЫХ ИЗМЕНЕНИЙ БЕЗ ПРОВЕРКИ ЗАВИСИМОСТЕЙ.
