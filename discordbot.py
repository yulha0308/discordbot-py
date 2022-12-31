from cmath import log
from distutils.sysconfig import PREFIX
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
import os

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

intents=discord.Intents.default()
intents.message_content=True

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    
@bot.command()
async def 고정링크(ctx):
  await ctx.send('https://discord.gg/z9Za2WW6AK%27')
                 
role='멤버'

@bot.command()
async def 서버가입(ctx, member: discord.Member=None):
  global user_role
  user_role=role
  member = member or ctx.message.author
  await member.add_roles(get(ctx.guild.roles, name=user_role))
  await ctx.channel.send("{}님이 정상적으로 서버가입을 마쳤습니다.".format(ctx.author.mention))



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")

    
