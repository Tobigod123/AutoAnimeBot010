#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default=3847632, cast=int)
    API_HASH = config("API_HASH", default="1a9708f807ddd06b10337f2091c67657")
    BOT_TOKEN = config("BOT_TOKEN", default="6735110948:AAE3KjdAz52oqW35kXlp0yk-8BFQW6K9g4A")

    # Database Credentials

    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASS = config("REDIS_PASSWORD", default=None)

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=-1002108819224, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default=-1001956463589, cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1002108819224, cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default=-1002108819224, cast=int)
    OWNER = config("OWNER", default=6748415360, cast=int)

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/6c477e9ac15d25f09ff99.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
