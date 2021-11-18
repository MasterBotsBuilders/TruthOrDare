from __future__ import division
import discord
import os
import random
import json
import requests
from replit import db
from keep_alive import keep_alive

client = discord.Client()

truths = [
  "Who is your favorite person in this server? Why?",
  "You got lucky and get to skip this one :smiling_imp:",
  "If you had 1 million dollars, what would be the first thing you'd do?",
  "What are your honest opinions on everyone in the server?",
  "When was the last time you lied?",
  "When was the last time you cried?",
  "What's your biggest fear?",
  "What's your biggest dream for the future?",
  "What's the worst thing you've ever done?",
  "Do you have a hidden talent?",
  "Have you ever cheated in an exam?",
  "Have you ever broken the law? :smiling_imp:",
  "What's your biggest insecurity?",
  "What's the biggest mistake you've ever made?",
  "What's one thing you hate people knowing about you?",
  "What's the worst thing someone's done to you?",
  "What's the best thing anyone's done for you?",
  "What's your worst habit?",
  "What's the worst thing you've ever said to anyone?",
  "What's the strangest dream you've had?",
  "Have you ever been caught red handed?",
  "When was the latest you stayed up?",
  "What's your biggest regret?",
  "What's the biggest misconception about you?",
  "Have you ever said something you regret about someone playing?",
  "What's one thing you wish more people knew about you?",
  "What's the most trouble you've been in?",
  "What's the worst thing you've lied about?",
  "What's one thing you wished you lied about?",
  "What's the best advice you've ever been given?",
  "What's the most money you've ever spent? (To the non-spoiled people here) ",
  "What's something you do that you know isn't good for you?",
  "Who do you dislike most in this server?",
  "Who's your best friend?",
  "When's your birthday?",
  "What's the most absurd rumor you've ever heard?",
  "Who in this server would you swap lives with?"
]
dares = [
  "Show everyone your worst photo",
  "You Lucky Ducky! You Get To Skip This Dare! :smiley:",
  "Show everyone the last 5 people you texted",
  "Let the group decide your pfp for a day",
  "Let the group decide your name for a day",
  "Do 20 Push-ups",
  "Do 20 sit-ups",
  "Show us your screen time report",
  "Eat an ice cube",
  "Yell out the first word that comes to your mind when i say your mom",
  "Keep your eyes and ears closed until its your turn again",
  "Send a selfie of you with a fruit, looking at it in an evil manner",
  "Pretend to be your best friend for a minute",
  "Say 2 brutally honest things about everyone in the group.",
  "Try and make the group laugh as quickly as possible, and if they don't, lecture them on having fun",
  "Tell everyone an embarassing story from your childhood.",
  "Tell everyone a story, made up or real, and have them guess if its real or not. If they win, change your nickname to their choice. If you win, make everyone else change their nickname to your choice.",
  "Tell the group two truths and a lie, and if they guess the lie have them decide your nickname. If they lose, then have the entire group change their nickname.",
  "Say an insult for everyone else playing",
]


if "responding" not in db.keys():
  db["responding"] = True

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if db["responding"]:
    options = truths
    if "truths" in db.keys():
      options = options + db["truths"]
  
  if db["responding"]:
    options2 = dares
    if "dares" in db.keys():
      options2 = options2 + db["dares"]
  
  if msg.startswith("~t"):
    await message.channel.send(random.choice(options))
  
  if msg.startswith("~d"):
    await message.channel.send(random.choice(options2))

  if msg.startswith("~help"):
    await message.channel.send("These are the following two commands. *~t*- shows a truth. *~d*-shows a dare.")

keep_alive()  

client.run(os.getenv("TOKEN"))
