import hfb_firebase as db
import discord
from discord import app_commands
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents = intents)

restaurants = ['Restaurant1', 'Cuisine1', 'Address1']

def format(arr):
    output = ''
    for restaurant, cuisine, address in arr:
        output += '- ' + restaurant + ' - ' + cuisine + ' - ' + address + '\n'
    output += ''
    return output

@bot.event
async def on_ready():
    print("Bot is up and ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name = "add", description = "Add restaurant to the Houston foods database")
async def add(interaction: discord.Interaction, restaurant: str, cuisine: str, address: str):
    line_item = [restaurant, cuisine, address]
    db.write(line_item)
    await interaction.response.send_message(f'Added {restaurant} to the database')

@bot.tree.command(name = "list", description = "List out all restaurants in the Houston foods database")
async def list(interaction: discord.Interaction):
    output = format(restaurants)
    await interaction.response.send_message(output)

bot.run(TOKEN)