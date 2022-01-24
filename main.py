import os
import discord 
import requests 
import json
import random
from replit import db
from keep_alive import keep_alive 
from discord.ext import commands 
from datetime import datetime, date
import pytz
import calendar 
from cards import *


client = discord.Client()
my_secret = os.environ['token'] #this codes the server token as to prevent access to the bot and the server from becoming public 

  @client.event
async def on_ready(): #Signal that bitbot is ready
  print('We have logged in as {0.user}'.format(client)) 

@client.event #bitbot will not respond to itself
async def on_message(message):
  if message.author == client.user: 
    return

  msg = message.content
  
  #Below are a series of misc. bot comands. 

  if msg == "ping":
    await message.channel.send("pong!")

  if msg.startswith('$hello'):
    await message.channel.send('Hello! I am BitB0T. How can I help you?')

  if msg.startswith('$thanks'):
    await message.channel.send('No problem! I am happy to help. Beep Boop!')

  if msg.startswith('$introduce'):
    await message.channel.send("Hi! I'm BitBot, a discord bot RPG assistant. Please see the pinned post about me to see what commands I know. I am updated by user @Spookysona#7944. If you have any questions ask my human. I am gappy to meet you all!")

  if msg.startswith('$poop'):
    await message.channel.send(":poop:")

  if msg.startswith('$postcrabs'):
    await message.channel.send(":crab: :crab: :crab:")
  
  if msg.startswith("$flipcoin"):
    coin = ["Heads!", "Tails!"]
    result = random.choice(coin)
    await message.channel.send(result)

  if msg.startswith("$randnum"):
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = random.choice(number)
    await message.channel.send(result)

  if msg.startswith("$goodmorningbitty"): #Bitty will provide the date/time in PST and CST, which is where members of the server are located. 
    tz_PST = pytz.timezone('US/Pacific') 
    datetime_PST = datetime.now(tz_PST)

    tz_CST = pytz.timezone('US/Central')
    datetime_CST = datetime.now(tz_CST)

    today = date.today()
    current_date = today.strftime("%m/%d/%y")

    await message.channel.send("Good morning! Today is " + current_date + ". The current time is " + datetime_PST.strftime("%H:%M:%S") + " PST, or " + datetime_CST.strftime("%H:%M:%S") + " CST. Today is a new day!")

  if msg.startswith("$time"): #same as above
      tz_PST = pytz.timezone('US/Pacific') 
      datetime_PST = datetime.now(tz_PST)

      tz_CST = pytz.timezone('US/Central')
      datetime_CST = datetime.now(tz_CST)

      await message.channel.send("It is " + datetime_PST.strftime("%H:%M:%S") + " PST, or " + datetime_CST.strftime("%H:%M:%S") + " CST.")

  if msg.startswith("$today"): ##This is for days of the week, which correspond to friend inside jokes. 
    my_date = date.today()
    today = calendar.day_name[my_date.weekday()]
    
    if today == "Sunday":
      await message.channel.send("It's finally Sunday! Let's relax.")
    
    if today == "Monday":
      await message.channel.send("It's Miku Monday! https://www.youtube.com/watch?v=widZEAJc0QM")

    if today == "Tuesday":
      tuesday = (0, 1, 2)
      choice = random.choice(tuesday)
      if choice == 0: 
        await message.channel.send("It's Tuesday. Tuck him in! https://64.media.tumblr.com/07906e34aa9970b7dbd25f9e9129ee12/ca781848ad67d447-c5/s540x810/6492839b99ad7680fe9c61b3e2057252e86297f8.jpg")
      if choice == 1: 
        await message.channel.send("It's sweet fat of the hog Tuesday. https://64.media.tumblr.com/631cafa8531ac24a22bd36e4c7e799b9/03dea4e32cc5026d-cb/s540x810/45c9f103a6ece75cfa2d37b5c7cd97f6d48dbe6a.jpg")
      if choice == 2:
         await message.channel.send("Tuesday again? No problem...... :okay_hand: https://cdn.discordapp.com/attachments/760689086263459882/933802753153699870/IMG_4580.png")
    
    if today == "Wednesday":
      wednesday = (0, 1)
      choice = random.choice(tuesday)
      if choice == 0:
        await message.channel.send("It is wednesday my dudes. https://www.youtube.com/watch?v=du-TY1GUFGk")
      if choice == 1:
        await message.channel.send("It's wizard wednesday! https://i.ytimg.com/vi/A_d1p-OJh6w/hqdefault.jpg")
    
    if today == "Thursday":
        await message.channel.send("It's out of touch Thursday! https://www.youtube.com/watch?v=Q8hp2IkI2es ")
    
    if today == "Friday":
      friday = (0, 1)
      choice = random.choice(friday)
      if choice == 0:
        await message.channel.send("It is now Flatworm Friday! https://www.youtube.com/watch?v=LoB6mB9qZn4")
      if choice == 1: 
        await message.channel.send("I's Flat Friday! https://www.youtube.com/watch?v=A5U8ypHq3BU")
    
    if today == "Saturday":
      await message.channel.send("It's saturday! Yay! Let me know if you have a meme you'd like me to post here.")

    else: 
      pass


  if msg.startswith("$2d6") or msg.startswith("$2D6"): #We frequently play a ttrpg that uses two six sided dice for rolls, so that functionality has been added to bitbot
    d6 = [1, 2, 3, 4, 5, 6]
    roll1 = random.choice(d6)
    roll2 = random.choice(d6) 
    result = roll1 + roll2
    await message.channel.send("You rolled " + str(roll1) + " and " + str(roll2) + ". The total is " + str(result) + "!") 
    if result == 12: 
      await message.channel.send("Wow! A natural 12!")
    if result == 2:
      await message.channel.send("Oof, sorry. Maybe use a point of luck?")

  if msg.startswith("$tarot"): #bitbot can pull a random tarot card for a reading from the deck list. located in deck.py
    random_card = random.choice(list(deck.items()))
    card_key = random_card[0]
    card_value = random_card[1]
    
    await message.channel.send("I have drawn a card for you! Your card is: " + str(card_key).capitalize() + ". " + str(card_value) + " :crystal_ball:")
  



keep_alive() #keep the bot running when file is closed 
client.run(my_secret) #use token to access discord bot 


