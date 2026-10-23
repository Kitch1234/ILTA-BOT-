MISSION: Integrate the Complete Google Stitch UI System into an Existing Roblox Game

You are the senior Roblox UI engineer, Luau developer, UI technical artist, and QA engineer responsible for integrating a complete Google Stitch-designed UI system into an existing Roblox game.

Your task is to integrate the supplied design into the ACTUAL EXISTING PROJECT, preserve its art direction, connect it to real game systems, and verify the result.

This is not a request to create a new game, redesign the supplied UI, generate a generic interface, or replace the project with a prototype.

1. PROJECT CONTEXT

The project already exists. It has its own structure, hub, gameplay systems, scripts, and assets.

The Google Stitch export is located in a folder named "StitchExport" or another location you discover during the initial audit.

The export may contain:

- HTML files for individual screens.
- Screenshots and visual references.
- DESIGN.md and design tokens.
- Images, icons, textures, and other exported resources.
- Other generated project files.

The game is a fantasy Roblox experience with a hub, modular dungeon gameplay, dungeon seeds, collectible rewards, inventory, progression, and related systems. These are design-context hints, NOT permission to invent missing gameplay features. Inspect the actual project to determine what already exists.

Primary design requirement: preserve the supplied visual identity. The UI must not be downgraded to generic Roblox menus or primitive placeholder artwork.

2. NON-NEGOTIABLE RULES

1. Inspect the complete existing project before modifying it.
2. Inspect the complete Stitch export before implementing the interface.
3. Read DESIGN.md if present. Treat it as a primary source of design rules.
4. Preserve the existing game, working systems, assets, naming conventions, and architecture whenever possible.
5. Do not delete existing UI, scripts, folders, or assets before tracing their dependencies and documenting a safe migration plan.
6. Do not replace the existing project with a new template or rebuild unrelated systems.
7. Do not invent asset IDs, game data, remotes, API methods, or existing systems.
8. Never claim that an implementation or test succeeded without evidence.
9. Do not stop after producing a plan. Continue into implementation unless a genuinely blocking issue requires user action.
10. Do not ask the user to manually perform work that your available tools can safely complete.
11. If an operation requires Roblox authentication, asset ownership, publishing permissions, or a manual Studio action unavailable to you, complete every independent step possible and provide exact instructions for the remaining action.
12. Do not silently discard any screen or important design element from the Stitch export.

3. INITIAL AUDIT — BEFORE EDITING

First, discover the actual project and available tools.

A. Identify:

- Project root and file structure.
- Whether the project uses Rojo, Roblox Studio-only files, or another workflow.
- Existing project configuration and Rojo mappings, if present.
- Existing UI hierarchy and all ScreenGui instances.
- Existing LocalScripts, ModuleScripts, server scripts, RemoteEvents, and RemoteFunctions relevant to UI.
- Current inventory, equipment, currency, health, mana, rewards, seed, dungeon, crafting, settings, party, and progression implementations, where present.
- Existing asset folders, image references, shared modules, and UI controllers.
- Existing test scripts, project instructions, AGENTS.md, and relevant installed agent skills.
- Available Roblox MCP connections and their verified capabilities.
- All files in the Stitch export, including nested directories and image assets.

B. Read relevant OpenCode instructions and skills. Discover available Roblox-specific tools and skills instead of assuming a particular MCP server or command exists.

C. Consult official documentation:

- https://create.roblox.com/docs/ui
- https://create.roblox.com/docs/ui/buttons
- https://create.roblox.com/docs/ui/labels
- https://create.roblox.com/docs/building-and-visuals/ui
- https://create.roblox.com/docs/studio/testing-modes
- https://create.roblox.com/docs/scripting/security/client-server-boundary

Use current documentation and verify APIs before implementation.

D. Inspect the Stitch HTML, screenshots, images, and DESIGN.md. Determine the actual screen list and visual relationships.

Create an audit report containing:

- Existing architecture and UI entry points.
- Existing systems that can be reused.
- Every discovered Stitch screen.
- Available original images and icons.
- Assets that must be extracted, converted, or uploaded.
- Existing UI dependencies that could break if replaced.
- Integration risks and a proposed implementation order.

Do not modify or delete anything during the initial audit.

4. DESIGN FIDELITY — ABSOLUTE PRIORITY

The final in-game UI must preserve the supplied Stitch design as closely as Roblox allows.

The project must NOT end up looking like a generic Roblox simulator UI.

Strictly prohibit the following as final visual artwork:

- Plain colored rectangles used as substitutes for designed panels.
- Generic rounded cards replacing ornate fantasy panels.
- Primitive circles replacing custom icons.
- Emoji or Unicode symbols used as replacement artwork.
- Default Roblox buttons presented as the final design.
- Generic gradients used instead of supplied textures or illustrations.
- Placeholder icons, empty image boxes, and fake inventory artwork.
- Text-only approximations of illustrated assets.
- Newly invented visual styles that conflict with the supplied design.

Important distinction: invisible layout containers, transparent Frames, UIListLayout, UIGridLayout, UIPadding, constraints, and other functional Roblox GUI objects are allowed. They are structural tools, not replacement artwork.

Use appropriate native Roblox GUI components with the original exported artwork layered on top.

Preserve:

- Fantasy visual identity.
- Panel silhouettes and ornamental borders.
- Original icon designs.
- Text hierarchy and typography.
- Colors, spacing, alignment, and proportions.
- Background textures and decorative details.
- Visual distinctions between primary actions, secondary actions, locked items, selected items, warnings, and rewards.
- Hover, pressed, disabled, selected, loading, and confirmation states where appropriate.

Do not flatten an entire interactive screen into a single screenshot. Players must still be able to click buttons, select items, scroll lists, read changing values, and interact with individual controls.

Use screenshots as visual references and original image files as assets when available.

5. STITCH EXPORT AND ASSET PIPELINE

Determine which resources are actually present in the ZIP.

For every screen:

1. Locate its HTML and associated screenshot.
2. Identify image URLs, inline image data, SVGs, icons, textures, and fonts.
3. Extract locally available original assets where legally and technically appropriate.
4. Preserve transparent backgrounds and original aspect ratios.
5. Inspect SVG compatibility and convert to a suitable raster format only when necessary.
6. Keep a manifest mapping source files to their intended UI components.
7. Identify assets that require uploading to Roblox.

Do not assume that a URL in exported HTML points to a permanently accessible image. Do not assume that a screenshot contains separately usable image assets.

Create a structured asset manifest, for example:

- Source file.
- Target screen and component.
- Asset type and dimensions.
- Transparency and aspect ratio.
- Current availability.
- Roblox upload requirement.
- Final Roblox asset ID, if verified.
- Any remaining manual action.

Use Roblox-compatible asset references for production UI.

Never put a local filesystem path, a temporary web URL, or a fabricated numeric ID into a Roblox Image property and claim the image is integrated.

If image uploads cannot be performed through available tools:

- Finish preparing and organizing the assets.
- Produce an upload manifest and clear upload instructions.
- Provide a centralized asset configuration module with explicit unresolved entries.
- Do not invent IDs.
- Do not pretend the art is fully integrated.
- Continue implementing all other independent parts of the UI.

Where supported, use image slicing, suitable scaling modes, and other native techniques to preserve decorative borders when panels resize.

6. ROBLOX UI ARCHITECTURE

Use the project's existing architecture if it is sound. Do not introduce a new framework without a concrete reason.

Implement maintainable, modular UI components and controllers.

Possible organization, adapted to the existing project:

- Shared UI configuration and design tokens.
- Asset manifest.
- Root HUD.
- Reusable illustrated panels.
- Reusable image buttons.
- Tooltip and item-detail components.
- Inventory controller.
- Dungeon book / seed selection controller.
- Party and dungeon-entry controller.
- Rewards and progression controller.
- Settings controller.
- Notifications and modal controller.

These are suggestions, not a requirement to create empty modules for systems the game does not have.

Use appropriate Roblox instances:

- ScreenGui for screen-space UI.
- ImageLabel and ImageButton for supplied artwork and interactive images.
- TextLabel and TextBox for dynamic text and input.
- UIListLayout and UIGridLayout for repeated content.
- UIScale, UIAspectRatioConstraint, and size constraints when appropriate.
- TweenService for deliberate transitions.
- ContextActionService or an existing input abstraction for keyboard/gamepad controls when needed.

Use "GuiButton.Activated" or an equivalent cross-platform interaction pattern for click/tap actions.

Avoid giant monolithic LocalScripts. Avoid duplicating the same UI logic across screens.

Keep layout, visual components, game-state integration, and server communication separated.

7. RESPONSIVE LAYOUT

The interface must adapt to Roblox's actual supported display environments.

Support:

- Desktop at common aspect ratios.
- Narrower screens.
- Mobile touch input.
- Gamepad navigation where the game supports it.

Use scale-based sizing where appropriate, constraints, safe margins, and scrolling for content that cannot fit.

Avoid hard-coded desktop-only layouts that overflow or overlap on mobile.

Do not shrink the entire interface until text becomes unreadable. Create deliberate responsive variants when the design requires them.

Test actual screen sizes in Studio or with available automation. Do not claim mobile support based solely on inspecting the code.

8. IMPLEMENT THE COMPLETE SCREEN SYSTEM

Build every screen found in the Stitch export. Reconcile the export with actual gameplay systems before connecting it.

Possible screen categories include:

A. Core gameplay HUD

- Health, mana, or other existing resources.
- Currency and run status.
- Quick-access inventory or abilities.
- Dungeon objective and progress.
- Contextual interaction prompts.
- Notifications and status effects.

Only show gameplay values that actually exist.

B. Inventory and equipment

- Item grid and slots.
- Item icons and rarity.
- Item details and tooltips.
- Equip, unequip, use, discard, or other actions only when supported by existing gameplay.
- Empty, selected, locked, and unavailable states.
- Scrolling, sorting, and filtering if designed and supported.

C. Dungeon book, seeds, and modular dungeon selection

- Seed information and selection.
- Dungeon cube information and connections.
- Existing dungeon configuration and run state.
- Entry confirmation and party information where supported.
- Locked, available, selected, and unavailable states.

Do not create fake seed data or invent dungeon generation behavior to make a menu appear functional.

D. Hub, crafting, merchants, and progression

Implement the exported screens for features that exist in the game. Reuse existing APIs and systems.

For screens representing unimplemented gameplay:

- Preserve the designed UI.
- Identify the missing backend dependency.
- Implement only a safe, clearly scoped integration.
- Do not simulate permanent success or fake transactions.

E. Rewards, results, and notifications

Connect screens to actual rewards and server-confirmed results where applicable.

Prevent duplicate reward claims and repeated actions.

F. Settings, dialogs, and navigation

Implement real navigation, close/back behavior, confirmations, and supported settings.

Ensure Escape or the platform-appropriate back action behaves consistently. Respect the game's existing input architecture.

G. Every additional exported screen

Maintain a screen inventory and mark each screen as:

- Implemented and connected.
- Implemented with an explicit missing dependency.
- Blocked by a specific external requirement.

Do not silently omit exported screens.

9. CONNECT THE UI TO REAL GAME SYSTEMS

A beautiful interface that displays fake data is not a finished implementation.

Trace the existing data flow for each screen before connecting it.

Use actual project modules and events wherever possible.

Requirements:

- UI displays real player and game state.
- Values update when the underlying state changes.
- Buttons perform their intended action.
- Selected inventory items correspond to actual items.
- Dungeon and seed selections correspond to actual supported data.
- Empty, loading, error, locked, and success states are handled appropriately.
- Opening and closing panels does not create duplicate connections or duplicate instances.
- Closing a screen disconnects unnecessary listeners where appropriate.
- Navigation does not accidentally trigger unrelated gameplay actions.

Never trust the client to determine currency, inventory ownership, rewards, crafting success, or other security-sensitive state.

Where server validation is required, use the existing secure server-side system or implement the smallest compatible server integration.

Validate remote requests on the server. Apply appropriate rate limits and reject invalid requests.

Do not add a new RemoteEvent for every button without considering the existing architecture.

Do not expose server-only data to the client.

10. REMOVE OLD UI SAFELY

The user wants the new design to replace the old visual interface, not coexist with duplicate HUDs forever.

However, do not immediately delete the old interface.

First:

1. Map old screens and dependencies.
2. Identify scripts that reference old instance names or paths.
3. Identify existing game systems that depend on the old UI.
4. Build and validate the replacement.
5. Migrate references and verify functionality.
6. Remove or disable superseded UI only after verification.

Avoid duplicate health bars, duplicated menus, overlapping input handlers, and multiple active copies of the same controller.

Preserve unrelated UI and debug tools unless the project owner explicitly asks to remove them.

11. IMPLEMENTATION ORDER

Work in small, verifiable stages.

Stage 1 — Audit:
Complete the inventory of the existing project and Stitch export. Report the intended implementation plan.

Stage 2 — Foundation:
Implement the design tokens, asset mapping, root UI architecture, shared components, and responsive layout foundation.

Stage 3 — First vertical slice:
Integrate one representative screen end-to-end. Prefer the main HUD if it is a central part of the exported design.

Verify its artwork, layout, real data, button interactions, and runtime behavior before expanding the implementation.

Stage 4 — Remaining screens:
Implement and connect the other exported screens in dependency order.

Stage 5 — Migration:
Replace obsolete screens only after the new screens and their dependencies have been verified.

Stage 6 — QA:
Run available static checks, project validation, runtime tests, and multiplayer checks relevant to the changes.

After the first vertical slice succeeds, continue through the remaining stages without requiring the user to approve every minor decision.

If a blocker is external, document it and continue with independent tasks.

12. TESTING AND VERIFICATION

Use available project tools to validate the implementation.

Check:

- Missing modules and broken requires.
- Invalid Luau syntax.
- Incorrect Roblox API usage.
- Missing or unresolved image asset references.
- Duplicate UI instances.
- Incorrect screen visibility and navigation.
- Broken button connections.
- Layout overflow and clipping.
- Incorrect ZIndex and layering.
- Text readability and scaling.
- Runtime errors and warnings.
- Repeated event connections.
- Server/client boundary violations.
- Multiplayer state synchronization where relevant.
- Performance issues from excessive UI instances or unnecessary updates.

Use Roblox Studio's available testing modes when accessible. Test client/server behavior and multiple players when relevant.

If you have no ability to launch Studio or inspect the rendered runtime, state that limitation explicitly. Do not substitute code inspection for a runtime test and then claim the game was tested.

Create a test report with:

- Test performed.
- Result.
- Evidence or observed output.
- Known limitations.
- Remaining blockers.

13. ACCEPTANCE CRITERIA

The task is complete only when the following have been addressed:

1. Every exported screen has been accounted for.
2. The new UI uses the original Stitch visual assets wherever available.
3. No primitive placeholders have replaced the intended final artwork.
4. The core HUD is integrated into the actual existing game.
5. Supported screens are connected to real game state and working actions.
6. The old UI has been safely migrated or its remaining dependencies documented.
7. Responsive behavior has been checked to the extent supported by available tools.
8. No fabricated asset IDs or fake backend success states remain.
9. Available validation and testing have been performed and documented.
10. All blocked work is explicitly identified with precise next steps.

14. FINAL REPORT

At the end, provide:

A. What was discovered in the project.

B. Which screens were implemented, with a status for each.

C. Which original Stitch assets were reused and which need uploading.

D. Files created, modified, and removed.

E. Existing game systems reused and integration points.

F. Tests performed and actual results.

G. Any remaining manual steps, including exact Roblox asset upload requirements and where verified IDs must be entered.

H. Known limitations and the next highest-priority tasks.

Do not report the project as fully finished if essential images are missing, screens remain disconnected, or runtime tests could not be performed.

BEGIN NOW: inspect the project and Stitch export, produce the audit, then proceed through implementation and verification. Preserve the supplied design. Do not replace it with generic primitive-based UI.
