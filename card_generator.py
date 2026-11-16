ROBLOX R15 — COMPLETE ANIMATION SYSTEM REPAIR & REBUILD

MISSION

You are a senior Roblox animation engineer specializing in R15 character animation, combat systems, mining simulators and multiplayer gameplay.

Your mission is to audit, diagnose, repair and rebuild the existing game's animation system.

The current project has a critical problem:

- Mining VFX and effects work.
- Mining damage may be applied.
- Characters do not properly swing their pickaxes.
- Attack animations are missing or malfunctioning.
- Overall character actions lack proper animations.

This is NOT a request to add visual effects to compensate for missing animations.

The character must physically perform the correct actions.

PHASE 1 — PROJECT AUDIT

Inspect the entire Roblox Experience.

Identify:

- All animation-related scripts.
- All Animation objects and AnimationIds.
- Humanoid and Animator configurations.
- Default Animate scripts.
- Existing animation priorities.
- Tool activation scripts.
- Mining and combat controllers.
- Conflicting animation systems.
- Invalid or inaccessible animation assets.
- R6/R15 compatibility problems.

Do not modify anything before documenting the existing architecture.

Create:

- ANIMATION_AUDIT.md
- ANIMATION_IMPLEMENTATION_PLAN.md

PHASE 2 — ANIMATION INFRASTRUCTURE

Implement one centralized animation management architecture.

Requirements:

- One Animator per character Humanoid.
- Centralized animation configuration.
- Animation loading and caching.
- Track lifecycle management.
- Priority management.
- Controlled transitions and blending.
- Cancellation when actions are interrupted.
- Death and respawn handling.
- Tool equip and unequip handling.
- No duplicate animation playback.
- No conflicting controllers.

Preserve and correctly integrate the existing Roblox default movement animation system.

Do not unnecessarily replace the default Animate script.

PHASE 3 — CHARACTER MOVEMENT

Implement and test:

- Idle.
- Walk.
- Run.
- Jump.
- Fall.
- Land.

Ensure smooth transitions between movement states.

PHASE 4 — MINING ANIMATION SYSTEM

Mining is a critical gameplay mechanic.

Implement genuine R15 pickaxe animations:

1. Pickaxe preparation.
2. Character wind-up.
3. Physical pickaxe swing.
4. Impact moment.
5. Recovery.
6. Return to idle.

Requirements:

- Arms and upper body must visibly move.
- Pickaxe must follow the character's hand.
- Grip and attachment positioning must be correct.
- Mining VFX must synchronize with the actual impact frame.
- Sound must synchronize with impact.
- Repeated mining must work without animation overlap.
- Moving, jumping, tool switching and interruptions must be handled correctly.

Never trigger the mining impact effect as a substitute for a real animation.

PHASE 5 — COMBAT ANIMATIONS

Implement:

- Light attack.
- Heavy attack.
- Attack combinations.
- Hit reactions.
- Blocking.
- Dodge.
- Death.

Ensure combat animations have correct priorities and do not break locomotion.

PHASE 6 — ANIMATION ASSET CREATION

Audit whether suitable animation assets already exist.

If assets are missing:

- Identify the missing animation clips.
- Create them using available animation authoring tools.
- Alternatively, import properly authored R15 animations.
- Publish assets under the correct Experience or group ownership.
- Verify every AnimationId in Roblox Studio.

Do not invent AnimationIds or claim an animation works without testing it.

If an animation cannot be created or published with the available tools, document the exact blocker.

PHASE 7 — MULTIPLAYER

Verify:

- Animation visibility for other players.
- Correct Animator replication.
- Server-side validation of gameplay actions.
- No duplicate damage events.
- No animation desynchronization.
- No exploitable client-authoritative damage.

PHASE 8 — PLAYTEST

Use Roblox Studio Play Mode.

Test:

- Mining repeatedly.
- Mining while moving.
- Switching tools during an animation.
- Jumping and landing.
- Combat combinations.
- Taking damage.
- Death and respawn.
- Multiple players performing actions simultaneously.

Capture screenshots or recordings where possible.

PHASE 9 — FINAL REPORT

Create:

- ANIMATION_TEST_REPORT.md
- ANIMATION_ASSET_REGISTER.md
- ANIMATION_KNOWN_ISSUES.md
- ANIMATION_CHANGELOG.md

Every feature must have one status:
PASS / FAIL / BLOCKED / NOT TESTED.

STRICT RULES

- Do not create a new empty project.
- Do not delete existing gameplay systems without justification.
- Do not replace functional mining or combat logic unnecessarily.
- Do not use fake animation effects.
- Do not use placeholder AnimationIds.
- Do not claim success without Play Mode verification.
- Preserve existing maps, assets, tools and gameplay progression.
- Work autonomously using available Roblox Studio MCP tools.
- Verify actual tool availability before relying on them.
- Do not ask the user to manually perform routine implementation steps.

FINAL OBJECTIVE:

A fully functional R15 animation system where mining, combat, movement and tool usage produce genuine, visible character animations synchronized with gameplay.
