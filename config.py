class Config:
    # ─── BOT SETTINGS ─────────────────────────────────────────────────────
    BOT_TOKEN = "8835991666:AAHnQXcikJcSw_vWK4xg2jM27kjVHxLkWxI"        # Get from @BotFather
    BOT_NAME  = "FILE STORE"          # Your bot's display name

    # ─── ADMIN SETTINGS ───────────────────────────────────────────────────
    ADMIN_IDS = [
        "7938671247",    # Your Telegram User ID (as string)
    ]

    # ─── OWNER CONTACT ────────────────────────────────────────────────────
    OWNER_USERNAME = "THE_DEVLOPER_KING"         # Without the @ symbol

    # ─── COIN SETTINGS ────────────────────────────────────────────────────
    REFERRAL_COINS     = 1   # Coins referrer earns per successful referral
    NEW_USER_REF_COINS = 2   # Bonus coins new user gets when joining via referral

    # ─── FORCE SUBSCRIBE CHANNELS ─────────────────────────────────────────
    # Users must join ALL channels below before using the bot
    FORCE_CHANNELS = [
        {"name": "ARAFAT SOURCE",  "username": "ARAFAT_SOURCE"},
        {"name": "ARAFAT CODEX7",  "username": "ARAFAT_CODEX7"},
        {"name": "ARAFAT FLEX",    "username": "ARAFAT_FLEX"},
    ]
