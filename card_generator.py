TASK: Integrate DialogueKit — Reimagined Mode Only

MISSION

Integrate Kyanid's DialogueKit into the existing Roblox Experience.

Official source:
https://devforum.roblox.com/t/dialoguekit-free-drop-in-npc-dialogue-system/4636187

Use ONLY the Reimagined dialogue mode.

Reimagined features:

- BillboardGui dialogue above NPC's head.
- World-space AnswerPart with interactive answer buttons.
- Hover effects.
- Click and hover sounds.
- No camera switching or forced camera movement.
- Local-only dialogue UI for each player.

Do NOT implement Classic mode.

PHASE 1 — PROJECT AUDIT

Before making changes:

1. Inspect the complete Roblox Experience and active Place.
2. Inspect Workspace, ReplicatedStorage, ServerScriptService, StarterPlayer and StarterGui.
3. Find all existing NPCs, their interaction scripts, ProximityPrompts and dialogue systems.
4. Identify existing NPCs that should receive dialogue.
5. Check whether DialogueKit or a similar system is already installed.
6. Check the current UI architecture and avoid conflicts.
7. Create a backup before modifying anything.

Do not delete, replace or duplicate existing NPC models.

PHASE 2 — SOURCE AND LICENSE VERIFICATION

1. Open the official DialogueKit resource.
2. Obtain the original DialogueV3.rbxl from the author's official download.
3. Inspect its complete hierarchy, scripts, modules and dependencies.
4. Read the installation instructions.
5. Verify the license and compatibility with this Experience.
6. Do not use unverified third-party copies.
7. If commercial use is not authorized, STOP before importing the system and report the licensing blocker. Do not bypass the license.

PHASE 3 — INSTALLATION

Install DialogueKit using the author's documented setup.

Follow the actual source hierarchy and installation instructions.

Required setup for each dialogue NPC:

- Model is inside Workspace.DialogueFolder.
- NPC has a Head.
- NPC has Torso, HumanoidRootPart or PrimaryPart.
- NPC has CollectionService tag: DialogueNPC.
- NPC contains a ModuleScript named DialogueData.

Configure every selected NPC with:

mode = "Reimagined"
options = {}

Do not use Classic settings such as camera distance or FOV.

Do not invent undocumented API calls or modify internal modules unnecessarily.

PHASE 4 — NPC DIALOGUES

Integrate dialogue into existing NPCs where appropriate.

Create configurable dialogue trees using the original DialogueData structure.

Use:

- NPC name and location where supported.
- Multiple dialogue lines.
- Player display name placeholder.
- Multiple answer choices.
- Next-node transitions.
- Goodbye/exit options.
- Server-approved actions for rewards and important game operations.

Do not give currency or items directly from untrusted client code.

Keep dialogue content separate from the dialogue engine.

PHASE 5 — VISUAL AND GAMEPLAY REQUIREMENTS

Reimagined mode must remain the active mode.

Verify:

- BillboardGui appears above the correct NPC.
- AnswerPart is positioned correctly.
- Buttons are readable and clickable.
- Hover effects work.
- Sounds work without excessive repetition.
- Dialogue does not obstruct important gameplay.
- Multiple players can talk to the same NPC independently.
- One player's dialogue does not interfere with another player's dialogue.
- Mobile, PC and gamepad interactions are considered.

Preserve the existing game's visual style.

Do not redesign the entire HUD.

PHASE 6 — TESTING

Run actual Play tests.

Test:

1. Talk to an NPC.
2. Open dialogue.
3. Select each answer.
4. Navigate between dialogue nodes.
5. Exit dialogue.
6. Reopen dialogue.
7. Test with two players simultaneously.
8. Test after NPC respawn if applicable.
9. Test on mobile-sized UI.
10. Check Output for errors and warnings.

Do not report tests as successful unless actually performed.

PHASE 7 — FINAL REPORT

Create:

- DIALOGUEKIT_INSTALLATION.md
- DIALOGUEKIT_NPC_CATALOG.md
- DIALOGUEKIT_TEST_REPORT.md
- DIALOGUEKIT_KNOWN_ISSUES.md

Report:

- What was installed.
- Which NPCs received dialogue.
- Which mode is active.
- Which scripts and objects were changed.
- Test results.
- Remaining issues.
- Any licensing restrictions.

STRICT RULES

- Reimagined mode ONLY.
- No Classic mode.
- No duplicate NPCs.
- No empty placeholder dialogues.
- No unnecessary replacement of existing systems.
- No destructive project-wide changes.
- No unverified Toolbox scripts.
- No fake test results.
- Preserve all existing maps, assets, NPCs and working gameplay.

The final result must be a fully integrated and tested dialogue system, not a prototype or demonstration.


https://create.roblox.com/store/asset/6418221666/Light-Utility-Vehicle?pageNumber=0&pagePosition=2
https://create.roblox.com/store/asset/6433272094/Dune-Buggy?pageNumber=0&pagePosition=3
https://create.roblox.com/store/asset/11641270452/2026-Colt-RIOLU-Standard?pageNumber=0&pagePosition=3

https://create.roblox.com/store/asset/6433323089/Sports-Car?pageNumber=0&pagePosition=5
