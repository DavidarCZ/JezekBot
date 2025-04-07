import discord
import requests
import json
import unicodedata
import random
from dotenv import load_dotenv
import os

# Constants
KEYWORDS = ['hedgehog','jezek', 'jezka', 'jezku', 'jezkovi', 'jezkovi', 'jezkem', 'jezci', 'jezku', 'jezkum', 'jezky', 'jezci', 'jezkove', 'jezcich', 'jezkach']
REACTION_EMOJI = '🦔'

# Helper Functions
def remove_diacritics(input_str):
      return ''.join(
        c for c in unicodedata.normalize('NFD', input_str)
        if unicodedata.category(c) != 'Mn'
      )

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_hedgehog():
  hedgehog_pictures = [
        "https://tenor.com/view/hedgehoglove-hedgehog-arici-gif-21931845",
        "https://tenor.com/view/%D1%91%D0%B6-gif-26077268",
        "https://tenor.com/view/hedgehog-gif-26256018",
        "https://tenor.com/view/briankik-turn-around-hedgehog-mrbond-gif-24320492",
        "https://tenor.com/view/hedgehog-to-toward-near-gif-19383771",
        "https://tenor.com/view/hedgehog-gif-10403085565855781900",
        "https://tenor.com/view/hedgehog-hat-magic-funny-gif-3399172",
        "https://tenor.com/view/edgehog-microsoft-edge-hedgehog-hedgehogs-sleep-gif-2500255623108511840",
        "https://tenor.com/view/hedgehog-floating-bath-time-gif-9915686",
        "https://tenor.com/view/cute-love-pet-lover-gif-24924793",
        "https://tenor.com/view/hedgehog-is-hedgehog-body-nog-hedgehog-shower-hedgehog-clean-gif-18183894163039785990"
    ]
  return random.choice(hedgehog_pictures)

def get_fact():
  facts = [
        "Hedgehogs can run up to 6 feet per second!",
        "Hedgehogs have around 5,000 to 7,000 quills.",
        "Hedgehogs are nocturnal animals and sleep during the day.",
        "A group of hedgehogs is called a prickle.",
        "Hedgehogs can hibernate in cold climates.",
        "Hedgehogs use their sense of smell to find food.",
        "Hedgehogs curl into a ball to protect themselves from predators.",
        "There are 17 different species of hedgehogs.",
        "Hedgehogs communicate through grunts, snuffles, and squeals.",
        "Hedgehogs have been around for over 15 million years!"
    ]
  return random.choice(facts)

# Main logic
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  
  async def on_message(self, message):
    if message.author == self.user:
      return

    # React to keywords
    normalized_content = remove_diacritics(message.content.lower())
    if any(word in normalized_content for word in KEYWORDS):
        await message.add_reaction(REACTION_EMOJI)
    
    # Commands
    if message.content.startswith('~hello'):
      await message.channel.send('Hello Hedgehog!🦔')
      
    if message.content.startswith('~meme'):
      meme_url = get_meme()
      await message.channel.send(meme_url)
      
    if message.content.startswith('~gif'):
      hedgehog_url = get_hedgehog()
      await message.channel.send(hedgehog_url)
      
    if message.content.startswith('~fact'):
      await message.channel.send(get_fact())
      
    if message.content.startswith('~help'):
      help_message = (
        "Commands:\n"
        "~hello - Greets you'\n"
        "~meme - Sends a random meme\n"
        "~help - Displays this help message\n"
        "~gif - Sends a random hedgehog gif\n"
        "~fact - Sends a random hedgehog fact\n"
        "React to messages containing 'jezek' or 'hedgehog' with a hedgehog emoji (🦔)\n"
      )
      await message.channel.send(help_message)

# Run the Bot
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_BOT_TOKEN'))