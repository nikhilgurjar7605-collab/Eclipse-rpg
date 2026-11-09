# ECLIPSE — Age of the Fallen

A Telegram-native cinematic RPG with PvE, PvP, exploration, character progression and a persistent shared world.

## Product direction

- **Platform:** Telegram bot only.
- **Genre:** Dark-fantasy RPG.
- **Combat:** PvE and PvP; tactical turn-based combat is the proposed baseline.
- **Presentation:** Cinematic story messages, character artwork, concise stat cards and inline keyboards.
- **Interaction rule:** Use commands to enter major systems; use inline keyboards for choices and navigation. Where possible, edit the existing media/message instead of sending a new message.

## New-player onboarding

1. `/start` checks whether the Telegram user already has a character.
2. New players receive an atmospheric welcome and an **Enter the Story** button.
3. **Skip Intro** bypasses story text and opens class selection.
4. Class selection displays five class buttons: Knight, Assassin, Mage, Ranger and Paladin.
5. Selecting a class edits the same message to show its artwork, short lore, Level 1 stats, starting active skill, passive trait and Confirm/Back buttons.
6. Confirm locks the class. Back returns to the five-class list.
7. Character creation collects character name and gender; appearance can be changed later.
8. A short opening sequence introduces the player's first route encounter.
9. The player fights a tutorial wolf. The tutorial reward is limited to XP, gold, wolf fangs and wolf hide/leather; do not add unrelated drops.
10. A much stronger scripted enemy defeats the player as part of the opening narrative, leading to the kingdom's recovery phase.
11. After recovery, show a concise command guide (for example `/profile`, `/inventory`, `/quests`, `/explore`, `/map`) and let the player enter normal play.

## Core systems

- Character profile and detailed stats
- Inventory with 20–30 starting slots (recommended default: 25)
- Equipment, skills and class progression
- Quests and story chapters
- Guild directory, applications and player-created guilds (phase-gated)
- Normal exploration with random enemies, NPC encounters and events
- Random dungeon appearances
- NPC interactions and trading
- World map with discoverable regions
- PvE bosses, parties and raids
- PvP arena, duels and seasonal rankings
- Economy, crafting and rewards

## Command-first navigation

Initial command set:
- `/start`
- `/profile`
- `/stats`
- `/inventory`
- `/quests`
- `/guild`
- `/explore`
- `/map`
- `/skills`
- `/equipment`

Inline buttons support selection and in-message navigation; they do not replace the command entry points.

## Design principles

1. Keep Telegram messages readable on mobile.
2. Avoid dumping every attribute into the first profile view.
3. Make class identity meaningful without making one class strictly superior.
4. Validate all rewards, cooldowns, trades and combat outcomes on the server.
5. Persist onboarding progress so users can resume after leaving the bot.
6. Separate scripted tutorial encounters from repeatable exploration.
7. Never grant the scripted defeat as a normal player death penalty.

## Proposed technical direction

Python + aiogram 3 is the proposed bot framework. Use PostgreSQL (for example Supabase-hosted PostgreSQL) for persistent player/game data. Keep secrets in environment variables and never commit bot tokens or database credentials.

The implementation stack and deployment target should be confirmed before production integration.
