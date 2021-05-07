import discord, os, logging, asyncio
from discord.ext import commands, tasks
import B, ClientConfig,  DatabaseConfig , DatabaseControl

logging.basicConfig(level=logging.INFO)
client = ClientConfig.client

import configparser
config = configparser.ConfigParser()
config["BOT"] = {
  "log_channel":738912143679946783, "support_guild":736422329399246990, "github_project":"https://github.com/JDJGInc/JDBot","invite_url":"https://discord.gg/sHUQCch", "kawaii_guild1":773571474761973840,"kawaii_guild2":806669712410411068,"kawaii_guild3": 69257620740479394,"blooper_verifiers":[708167737381486614,168422909482762240],"special_user":168422909482762240
}

with open('config.ini', 'w') as configfile:
  config.write(configfile)

#B.b()
#client.run(os.environ["classic_token"])
