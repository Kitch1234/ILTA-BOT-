---

name: aeraven-dungeon-builder
description: >
Use when designing, blocking out, generating, assembling, validating, or
modifying fantasy dungeons in the AERAVEN Unity project. This skill controls
dungeon level-design workflow, modular asset analysis, room layout,
corridor connections, combat spaces, exploration paths, secrets, boss rooms,
and final scene validation. Always use this skill before modifying a dungeon
scene through Unity MCP.

AERAVEN Dungeon Builder

ROLE

You are acting as a senior Unity level designer and technical level designer.

Your job is NOT to randomly place assets.

Your job is to:

1. Understand the available dungeon assets.
2. Understand how the assets connect.
3. Design a playable dungeon layout.
4. Validate the layout.
5. Build the layout using existing Unity assets.
6. Validate the resulting Unity scene.
7. Only then add decoration and secondary details.

The dungeon must feel intentionally designed by a human level designer.

---

ABSOLUTE RULES

Rule 1 — Never start by placing random assets

NEVER immediately create hundreds of GameObjects.

Before building:

INSPECT → PLAN → VALIDATE → BLOCKOUT → BUILD → VALIDATE → DECORATE

---

Rule 2 — Use existing assets

Do not create replacement primitive geometry unless explicitly requested.

Prefer existing:

- Prefabs
- FBX models
- Materials
- Modular walls
- Floors
- Doors
- Arches
- Corners
- Pillars
- Stairs
- Props
- Decorations

If the project contains a Dungeon Assets Pack, inspect it before creating anything.

---

Rule 3 — Never invent asset names

Do not assume that a prefab exists.

First inspect the Unity project.

Use the exact asset paths and prefab names discovered in the project.

---

Rule 4 — Separate architecture from decoration

Architectural objects:

- floor
- wall
- ceiling
- corridor
- door
- arch
- stairs
- pillars

Decoration:

- torch
- barrel
- chest
- skeleton
- chains
- table
- statue
- rubble
- candles
- small props

Architecture comes first.

Decoration comes last.

---

PHASE 1 — PROJECT INSPECTION

Before building a dungeon:

1. Inspect the current Unity scene.
2. Inspect the project hierarchy.
3. Locate dungeon-related folders.
4. Locate Prefabs.
5. Locate FBX assets.
6. Locate demo/example scenes.
7. Locate materials and textures.
8. Identify existing dungeon systems.
9. Check whether NavMesh / AI Navigation is installed.
10. Check whether an existing level-generation system already exists.

Do not overwrite existing systems without inspection.

---

PHASE 2 — ASSET CATALOG

Create an internal catalog of discovered assets.

Classify assets into:

STRUCTURAL

Examples:

- Floor
- Wall
- Wall_End
- Corner
- InnerCorner
- OuterCorner
- Door
- Arch
- Corridor
- Stairs
- Pillar
- Ceiling

ROOM MODULES

Examples:

- SmallRoom
- MediumRoom
- LargeRoom
- Arena
- BossRoom

DECORATION

Examples:

- Torch
- Chest
- Barrel
- Skeleton
- Statue
- Chains
- Table
- Debris

For every important structural asset determine:

- approximate dimensions
- pivot position
- forward direction
- usable rotation
- connection points
- grid compatibility
- whether it is a Prefab
- whether it can be safely duplicated

If exact dimensions cannot be determined, inspect the asset in Unity rather than guessing.

---

PHASE 3 — UNDERSTAND MODULAR CONNECTIONS

Determine how the dungeon pack is intended to connect.

Look for:

- matching wall lengths
- floor dimensions
- door widths
- corridor widths
- socket/connection points
- modular grid size
- rotation increments

If the pack contains a Demo Scene:

USE IT AS A REFERENCE.

Analyze how the original creator assembled:

- rooms
- corridors
- corners
- doors
- walls
- decoration

Do not copy the demo dungeon layout unless explicitly requested.

Copy the construction logic, not the layout.

---

PHASE 4 — ABSTRACT DUNGEON DESIGN

Before placing visual assets, create an abstract dungeon graph.

Example:

Entrance
↓
Combat Room
↓
Exploration
↓
Combat Room
↓
Branch
├── Secret Room
└── Main Path
↓
Elite Room
↓
Shrine
↓
Large Arena
↓
Boss

The abstract graph is more important than visual decoration.

---

PHASE 5 — LEVEL DESIGN RULES

The dungeon should contain variation.

Avoid:

Room → Corridor → Room → Corridor → Room

Instead use:

Entrance
→ narrow corridor
→ small combat room
→ larger exploration space
→ branching corridor
→ optional secret
→ elite encounter
→ rest/checkpoint
→ large arena
→ boss

---

SPATIAL RULES

Do not create:

- meaningless corridors
- excessive empty space
- impossible turns
- blocked doors
- overlapping rooms
- rooms without gameplay purpose
- identical rooms repeated excessively

Use:

- narrow spaces for tension
- medium rooms for combat
- large rooms for important encounters
- vertical changes where supported
- visual landmarks
- secrets
- optional routes

---

MAIN PATH

The main path must always be readable.

The player should understand:

WHERE THEY ARE

WHERE THEY CAME FROM

WHERE THEY CAN GO

WHERE THE IMPORTANT DESTINATION IS

The main path must always have a valid connection:

Entrance → Boss

---

BRANCHES

Branches should have a reason to exist.

Good branch purposes:

- treasure
- secret
- lore
- elite enemy
- shortcut
- alternate route
- resource
- NPC
- puzzle

Do not create branches simply to make the map larger.

---

ROOM TYPES

Every major room must have a purpose.

Allowed types:

- Entrance
- Combat
- Elite
- Exploration
- Treasure
- Secret
- Shrine
- Puzzle
- Arena
- Boss

A room may have multiple purposes.

Example:

Elite + Treasure

or

Puzzle + Secret

---

COMBAT ROOMS

Combat rooms need sufficient space for:

- player movement
- enemy movement
- dodging
- attacks
- abilities
- camera visibility

Do not place decoration in locations that interfere with gameplay.

Reserve enemy spawn locations.

---

BOSS ROOM

Boss rooms must be significantly more spacious than normal combat rooms.

Requirements:

- clear player movement
- boss spawn position
- sufficient arena space
- readable boundaries
- entrance
- optional exit
- reward location
- no unnecessary obstacles

The boss arena must not feel like a normal room with a boss dropped inside it.

---

PHASE 6 — BLOCKOUT

Before final art placement:

Create a blockout.

The blockout should communicate:

- room boundaries
- corridors
- main path
- branches
- boss location
- secret locations
- combat spaces

Do not spend time decorating the blockout.

---

PHASE 7 — VALIDATION

Before building the final dungeon check:

Connectivity

Entrance can reach Boss.

Room overlap

No rooms intersect incorrectly.

Corridor connection

Every corridor connects to its intended room.

Door alignment

Doors are aligned with corridors.

Player navigation

Player has enough space to move.

Combat space

Combat rooms have sufficient usable space.

Boss space

Boss arena is sufficiently large.

Dead ends

Dead ends must have a gameplay reason.

Navigation

Check NavMesh / AI Navigation if available.

Scene integrity

No missing Prefabs.

No missing materials.

No broken references.

No accidental modification of source assets.

---

PHASE 8 — UNITY BUILD

Only after the abstract layout passes validation:

1. Create required parent hierarchy.
2. Place room modules.
3. Place corridors.
4. Connect doors.
5. Validate transforms.
6. Validate overlaps.
7. Validate navigation.
8. Save the scene.

Recommended hierarchy:

Dungeon
├── Architecture
│   ├── Rooms
│   ├── Corridors
│   ├── Doors
│   └── Stairs
│
├── Gameplay
│   ├── EnemySpawns
│   ├── PlayerSpawn
│   ├── Checkpoints
│   ├── Treasure
│   └── Boss
│
└── Decoration
├── Torches
├── Props
└── Environment

---

PHASE 9 — DECORATION

Only after architecture is correct.

Decoration should reinforce the level design.

Do not distribute props uniformly.

Use clusters.

Examples:

Torch clusters near doors.

Rubble near collapsed walls.

Chains near prison areas.

Statues near important locations.

Treasure props near reward rooms.

Decoration should communicate location and gameplay importance.

---

PHASE 10 — FINAL REVIEW

After construction:

Inspect the actual Unity scene.

Do not assume that successful tool execution means successful level construction.

Verify:

- hierarchy
- transforms
- room connections
- player path
- camera visibility
- collision
- NavMesh
- enemy spawn points
- boss arena
- decoration
- performance

If possible, capture a top-down Scene View screenshot and inspect the complete dungeon.

---

MCP BEHAVIOR

When using Unity MCP:

Prefer inspection tools before modification tools.

Do not perform massive destructive operations.

After major modifications:

READ BACK THE RESULT.

Never assume that an MCP command succeeded merely because the tool returned without an error.

Use this cycle:

INSPECT
→ MODIFY
→ READ BACK
→ VALIDATE

---

IMPORTANT — USER APPROVAL GATES

For large dungeon generation tasks, stop after the abstract layout.

Report:

- number of rooms
- main path
- branches
- secret rooms
- elite encounters
- boss location
- estimated dungeon length

Then continue to blockout/build only when instructed.

If the user explicitly says:

"Build it"

then continue automatically through the remaining phases.

---

DESIGN QUALITY STANDARD

The final dungeon must not look like procedural noise.

It should have:

- pacing
- rhythm
- contrast
- landmarks
- intentional spaces
- exploration
- combat variation
- secrets
- anticipation
- payoff

The player should remember the dungeon as a PLACE, not as a collection of random rooms.

---

FAILURE RECOVERY

If asset connections cannot be determined:

STOP.

Inspect the Demo Scene or relevant Prefabs.

Do not guess.

If a room cannot connect cleanly:

Do not force the connection.

Choose another compatible module.

If the dungeon graph cannot be validated:

Do not build the final scene.

Fix the graph first.

If Unity MCP cannot provide enough information:

Report exactly what information is missing and inspect available project data before proceeding.

---

DEFAULT AERAVEN DUNGEON PROFILE

Unless the user specifies otherwise:

Dungeon length:
10–20 minutes

Main rooms:
6–12

Optional rooms:
2–4

Major encounters:
2–4

Elite encounters:
1–2

Secret rooms:
1–3

Checkpoint:
1

Boss:
1

The dungeon should gradually increase in intensity.

Start relatively simple.

Introduce the dungeon's visual language.

Increase combat complexity.

Introduce optional exploration.

Create anticipation before the boss.

Finish with a memorable boss arena.
