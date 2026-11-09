# ECLIPSE onboarding and tutorial flow

## State machine

```text
NEW_PLAYER
  -> WELCOME
  -> INTRO (or SKIP)
  -> CLASS_LIST
  -> CLASS_PREVIEW
  -> CLASS_CONFIRMED
  -> NAME_INPUT
  -> GENDER_SELECTION
  -> CHARACTER_CONFIRMATION
  -> OPENING_STORY
  -> WOLF_ENCOUNTER
  -> SCRIPTED_DEFEAT
  -> KINGDOM_RECOVERY
  -> TUTORIAL_COMPLETE
  -> NORMAL_GAME
```

## Interaction details

### Welcome
Send a cinematic welcome with:
- Enter the Story
- Skip Intro

Skip Intro must go directly to class selection, not to the main menu.

### Class list and preview
Show five class buttons. When a class is selected:
- Edit the same Telegram message/caption.
- Replace the artwork and class details.
- Show base stats, starting active skill and passive ability.
- Show **Back** and **Confirm**.

Back returns to the class list. Confirm stores the class and proceeds to character creation.

### Character creation
Collect:
- Character name
- Gender
- Optional basic appearance choice

Appearance should be editable later. Do not make the initial setup too long.

### Tutorial story
After confirmation, narrate the opening journey and introduce a named wolf enemy. Start a short tutorial fight that teaches the basic battle actions.

On victory, award only the defined tutorial rewards:
- XP
- Gold
- Wolf fangs
- Wolf hide/leather

Do not add a health potion or unrelated loot unless the game design is deliberately revised.

### Scripted defeat and recovery
After the wolf encounter, introduce a clearly stronger story enemy. This is a narrative set-piece that the player is expected to lose. Keep it separate from normal death rules and do not delete equipment or permanently punish the player.

The player wakes in the kingdom and enters the recovery phase. Then provide a short command guide and unlock normal gameplay.

## Reliability requirements

- Save the onboarding state after every completed step.
- Repeated callbacks must not create duplicate characters or duplicate rewards.
- Validate callback ownership against the Telegram user ID.
- Add an expiry/retry path for name input and abandoned onboarding.
- Use idempotent reward transactions.
