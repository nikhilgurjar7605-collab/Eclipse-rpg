# ECLIPSE — Age of the Fallen

A cinematic dark-fantasy RPG built for Telegram.

## Project status

The repository is being prepared for the first playable bot milestone. The current game concept, onboarding flow and class system are documented in `docs/`.

## Start here

- [Game design](docs/GAME_DESIGN.md)
- [Onboarding flow](docs/ONBOARDING_FLOW.md)
- [Characters and classes](docs/CHARACTERS_AND_CLASSES.md)

## Planned first milestone

1. Telegram bot foundation and persistent player registration.
2. New-player intro, skip option and class selection.
3. Editable class preview cards with stats and skills.
4. Character name and gender creation.
5. Tutorial wolf encounter and scripted story defeat.
6. Kingdom recovery and command guide.

## Proposed stack

Python + aiogram 3, PostgreSQL, and environment-based configuration. Confirm deployment and database settings before adding production secrets.

**Security:** Never commit `.env` files, Telegram bot tokens, database passwords or API keys.
