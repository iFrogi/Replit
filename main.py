import discord
import os
client = discord.Client()

@client.event
def onmessage(m):
  m.channel.send(m.content + "- A unwise man once said")

client.run(os.environ.get("TOKEN"))