# bot.py
"""
__TOSEARCH__
await keyword
async keyword
@ keyword
raise keyword

__IDEA__
need to give prompt on error


__NOTES__
updates each time I run it from command time
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime

def log(string):
	log = open("logs/runtimelog.txt", "a")
	log.write("[%s] %s\n" % (str(1), string))
	log.close()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

log("open on {TOKEN}")

bot = commands.Bot(command_prefix='ye')

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
	log("Member join {member.name}")
	await member.create_dm()
	await member.dm_channel.send(
		"Hi {member.name}, welcome fatass"
	)

@bot.event
async def on_error(event, *args, **kwargs):
	with open('logs/errlog.txt', 'a') as f:
		if event == 'on_message':
			f.write(f'Unhandled Message: {args[0]}\n')
		else:
			raise
#
# COMMANDS
#
@bot.command(name="fatshame", help="literally bullying")
async def on_message(ctx, arg):
	log("CMD: fatshame")
	await ctx.send(str(ctx.args[1]) + " is fat lmao")

@bot.command(name="1v1", help="[n/a] sends a 1v1")
async def on_message(ctx):
	log("CMD: 1v1")
	await ctx.send(file=discord.File("1v1 me noob.png"))
	await ctx.send("its not working. please don't try again")

@bot.command(name="k", help="please dont use this")
async def on_message(ctx, arg):
	log("CMD: k")
	await ctx.send("read the help menu and piss off")

@bot.command(name="setscore", help="Sets a new score for count")
async def on_message(ctx, arg):
	log("CMD: setscore")
	print(str(ctx.guild))
	file = open("scorecounter/%sscores.txt" % str(ctx.guild), "a")
	file.write(str(arg) + "\n")
	file.close()
	await ctx.send("New Score: " + str(arg) + " Logged")

@bot.command(name="topscore", help="[n/a] Gets the top count score for this server")
async def on_message(ctx):
	log("CMD: setscore")
	print(str(ctx.guild))
	file = open("scorecounter/%sscores.txt" % str(ctx.guild), "r")
	best = 0
	for line in file.readlines():
		best = max(best, int(line))
	file.close()
	await ctx.send("Best Score: " + str(best))

@bot.command(name="topscores", help="Gets the top 10 count score for this server")
async def on_message(ctx, arg=10):
	log("CMD: setscore")
	print(str(ctx.guild))
	file = open("scorecounter/%sscores.txt" % str(ctx.guild), "r")
	bests = []
	for line in file.readlines():
		bests.append(int(line))
	file.close()
	bests.sort()
	await ctx.send("Best %d Scores: " % arg)
	for i in range(1, arg + 1): #need to have if none
		awaitctx.send("%d) %d" % (i, bests[-1 * i - 1]))


@bot.command(name="votekick", help="[n/a] votes for them")
async def on_message(ctx, arg): #needs random chance, needs to get @'s, needs to disconnect someone
#needs to get a @'d person
#guild --> voice channels --> people

#TODO:
#match channel members to args
#make sure that the vc's are being iterated throught
#make sure args are correct, and sent a message if not
	log("CMD: votekick")
	print(str(ctx))
	#print(ctx.guild.voice_channels)
	for vc in ctx.guild.voice_channels:
		print("VC Found: " + str(vc)) #look for different attributes
		print("Members: " + str(vc.members)) #not recognizing members for some reason
		for member in vc.members:
			print("Member display:\t " + str(member.display_name))
			print("Member: \t" + str(member.id))
			print("Arg: \t" + str(ctx.args[1])[3:-1])
			print("Is Node: \t" + str(str(ctx.args[1])[3:-1] == str(member.id)))
			print("Is Author: \t" + str(False))
		#print(vc.members)

	await ctx.send(str(ctx.args[1]) + " was the Imposter")
"""
else:
	person @'d + 1
	send (num / <needed>)
if <people in senders vc> / 2 + 1 < amountL:
	if person in vc
		if *chance*
			is imposter
		is not imposter
		kick
"""


bot.run(TOKEN)