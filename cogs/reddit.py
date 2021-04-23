from discord.ext import commands
import discord
import apraw
import os
import random
import aiohttp

class Reddit(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.reddit =  apraw.Reddit(client_id=os.getenv("reddit_client_id"), client_secret=os.getenv("reddit_client_secret"),password= os.getenv("reddit_password"), user_agent="JDBot 1.0", username= os.getenv("reddit_username"))

  @commands.command(brief="Random Meme from Dank Memes with Apraw")
  async def dankmeme(self,ctx):
    subreddit = await self.reddit.subreddit("dankmemes")
    async for submission in subreddit.new():
      print(submission)
    await ctx.send("Command still WIP")

  @commands.command(brief="Random meme from Dank Memes with aiohttp",help="Content returned may not be suitable to younger audiences")
  async def dankmeme2(self,ctx):
    e = await self.client.aiohttp_session.get("https://www.reddit.com/r/dankmemes/.json")
    data = random.choice((await e.json())["data"]["children"])["data"]
    embed = discord.Embed(title=data["title"], color=0x00FF00)
    embed.set_image(url=data["url"])
    embed.set_footer(text=f"Upvote ratio : {data['upvote_ratio']}")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Reddit(client))