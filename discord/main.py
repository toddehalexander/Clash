from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import requests
from urllib.parse import quote
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
CLASH_TOKEN: Final[str] = os.getenv('CLASH_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)

headers = {
    'authorization': 'Bearer ' + CLASH_TOKEN,
    'Accept': 'application/json'
}

# Clash of Clans functions
def get_player_info(player_tag):
    player_tag_encoded = quote(player_tag)
    response = requests.get(
        f'https://api.clashofclans.com/v1/players/{player_tag_encoded}', headers=headers)
    if response.status_code == 200:
        player_json = response.json()
        player_info = (f'Player name: {player_json["name"]}\n'
                   f'Player tag: {player_json["tag"]}\n'
                   f'Player trophies: {player_json["trophies"]}\n'
                   f'Player level: {player_json["expLevel"]}\n'
                   f'Best trophies: {player_json["bestTrophies"]}\n'
                   f'\n'
                   f'Clan name: {player_json.get("clan", {}).get("name", "Not in a clan")}\n'
                   f'Clan tag: {player_json.get("clan", {}).get("tag", "Not in a clan")}\n'
                   f'Clan level: {player_json.get("clan", {}).get("clanLevel", "Not in a clan")}\n')

        return player_info
        return player_info
    else:
        return 'Player not found.'

def get_clan_members(clan_tag):
    clan_tag_encoded = quote(clan_tag)
    response = requests.get(
        f'https://api.clashofclans.com/v1/clans/{clan_tag_encoded}/members', headers=headers)
    if response.status_code == 200:
        members_json = response.json()
        return "Clan Members Information:\n" + '\n'.join([f"Name: {member['name']}\nRank: {member['clanRank']}\nTown Hall Level: {member['townHallLevel']}\nRole: {member['role'].capitalize()}\n------------------------" for member in members_json['items']])
    else:
        return 'Clan not found.'

def get_clan_war_league(clan_tag):
    clan_tag_encoded = quote(clan_tag)
    response = requests.get(
        f'https://api.clashofclans.com/v1/clans/{clan_tag_encoded}/currentwar/leaguegroup', headers=headers)
    if response.status_code == 200:
        league_json = response.json()
        result = "Clan War League Information:\n"
        for member in league_json['clans']:
            townhall_levels = defaultdict(int)
            for war_member in member.get('members', []):
                townhall_level = war_member.get('townHallLevel', 'N/A')
                townhall_levels[townhall_level] += 1
            result += f"{member['name']}:\n"
            for townhall_level, count in sorted(townhall_levels.items(), reverse=True):
                if townhall_level != 'N/A':
                    result += f"Townhall {townhall_level}: {count}\n"

            # Sort the townhall_levels dictionary by key before plotting
            townhall_levels = dict(sorted(townhall_levels.items()))

            # Plotting the graph (if required)

        return result
    else:
        return 'Clan not found or no ongoing war.'


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        if user_message.startswith('clan'):
            clan_tag = user_message.split()[1]
            response = get_clan_members(clan_tag)
        elif user_message.startswith('war'):
            clan_tag = user_message.split()[1]
            response = get_clan_war_league(clan_tag)
        elif user_message.startswith('player'):
            player_tag = user_message.split()[1]
            response = get_player_info(player_tag)
        else:
            response = get_response(user_message)

        response = response[:2000]  # Limit the response to 2000 characters
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=DISCORD_TOKEN)


if __name__ == '__main__':
    main()
