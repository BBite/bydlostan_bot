# from environs import Env
#
# env = Env()
# env.read_env()
#
# BOT_TOKEN = env.str("BOT_TOKEN")
# ADMINS = env.list("ADMINS")
# IP = env.str("ip")

import os
BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMINS = os.environ["ADMINS"]