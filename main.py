import discord
from discord.ext import commands
import os
import json
import requests
import aiohttp
from bs4 import BeautifulSoup
from discord import app_commands 
import datetime
import sys




intents = discord.Intents().all()
bot = commands.Bot(command_prefix="/", intents=intents)




os.system('cls')

with open("config.json", 'r') as config:
    configs = json.load(config)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f"Connecté à : {bot.user.name}")
    activity = discord.Activity(
        name="Valorant | v3 Docker 🐳",
        type=discord.ActivityType.playing
    )
    await bot.change_presence(activity=activity)
    
    try:
        synced = await bot.tree.sync()
        print(f"Hello! {bot.user.name}, Le bot est bien connecté à {len(bot.guilds)} serveurs.🤖 Version de discord : {discord.__version__} ")
        print(len((synced)), "commandes synchronisées")
    except:
        print("Syncing failed.")


@bot.tree.command(name="tracker", description="Show statistics of a player 📈")
@commands.guild_only()
async def tracker(interaction: discord.Interaction, username: str, tag: str):
    try:
        await interaction.response.defer()
        Username = "".join(username)
        Tag = "".join(tag)
    
        # Ajoute un %20 dès qu'il y a un espace
        Username = Username.replace(" ", "%20")
    
        overview_url = f'https://tracker.gg/valorant/profile/riot/{Username}%23{Tag}/overview'
        agents_url = f'https://tracker.gg/valorant/profile/riot/{Username}%23{Tag}/agents'
        weapons_url = f'https://tracker.gg/valorant/profile/riot/{Username}%23{Tag}/weapons'

        overview_response = requests.get(overview_url)
        agents_response = requests.get(agents_url)
        weapons_response = requests.get(weapons_url)

        overview = BeautifulSoup(overview_response.content, 'html.parser')
        agent = BeautifulSoup(agents_response.content, 'html.parser')
        weapon = BeautifulSoup(weapons_response.content, 'html.parser')
        # Extraction des données nécessaires
        E = overview.find_all(class_='numbers')  # Overview
        D = overview.find_all(class_='wrapper')  # Overview
        C = agent.find_all(class_='st__item st-content__item-value st__item--sticky st__item--wide agent-row')  # Agent
        A = overview.find_all(class_='stat__value')  # Overview
        B = overview.find_all(class_='value')  # Overview
        F = weapon.find_all(class_='text-18')  # Weapons
        G = overview.find(class_='trn-profile-highlighted-content__icon')['src']#Overview
            
            
        # Extraction des données des pages web
        winrate = B[15].text
        rank = A[0].text
        highest_rank = B[1].text
        best_agent = C[0].text
        headshot = B[14].text
        ace = D[15].text
        ACE = ace[4:6]
        k_d_a = E[11].text
        KDA = k_d_a[9:]
        best_weapon = F[0].text
        kills_bwepaon = F[1].text
        HS_bweapon = F[2].text
        image = G
            


        # Création de l'embed avec les statistiques
        embed = discord.Embed(title="Valorant Statistics", description=f"Stats 📈", color=0xFFFFFF)
        embed.set_author(name=f'{username}#{tag}', icon_url=interaction.user.avatar)

        embed.add_field(name="Rank", value=rank, inline=True)
        embed.set_thumbnail(url=f"{image}")
        embed.add_field(name="Peak Rating", value=highest_rank, inline=True)
        embed.add_field(name="Headshot %", value=headshot, inline=True)
        embed.add_field(name="Win Rate %", value=winrate, inline=True)
        embed.add_field(name="Aces", value=ACE, inline=True)
        embed.add_field(name="KDA", value=KDA, inline=True)
        embed.add_field(name="Best Agent", value=best_agent, inline=True)
        embed.add_field(name="Best Weapon", value=best_weapon, inline=True)
        embed.add_field(name=f"Kills with {best_weapon}", value=kills_bwepaon, inline=True)
        embed.add_field(name=f"HS with {best_weapon}", value=HS_bweapon, inline=True)
        await interaction.followup.send(embed=embed)
    except Exception as e:
        print("Error",e)
        embed=discord.Embed(title="**Error ❌**",description="**User not found,verify and try again**",color=0xFF0000)
        await interaction.followup.send(embed=embed)  
@bot.tree.command(name="stats", description="Afficher l'uptime du bot 📈")
async def uptime(interaction: discord.Interaction):
    delta = datetime.datetime.utcnow() - bot.start_time
    days = delta.days
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    embed = discord.Embed(title="`Bot Uptime`", description=f"`{days} Days {hours} Hours {minutes} min {seconds} s`", color=0xFFFFFF)
    embed.add_field(name="`Discord Version`", value=f'`{discord.__version__}`', inline=False)
    embed.add_field(name="`Bot Version`", value='`1.0.0`', inline=False)
    await interaction.response.send_message(embed=embed)

    





bot.run(configs["token"])



