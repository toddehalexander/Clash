import requests
from urllib.parse import quote
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import os

with open('C:\\Users\\Todd\\Desktop\\API\\clash_api.txt', 'r') as file:
    token = file.read().strip()

headers = {
    'authorization': 'Bearer ' + token,
    'Accept': 'application/json'
}

def get_user(player_tag):
    # URL encode the player tag
    player_tag_encoded = quote(player_tag)
    # this will get an account from the Clash of Clans API
    response = requests.get(
        f'https://api.clashofclans.com/v1/players/{player_tag_encoded}', headers=headers)
    if response.status_code == 200:
        user_json = response.json()
        print('Player name: ' + user_json['name'])
        print('Player tag: ' + user_json['tag'])
        print('Player trophies: ' + str(user_json['trophies']))
        print('Player level: ' + str(user_json['expLevel']))
        print('Best trophies: ' + str(user_json['bestTrophies']))
        
        if 'clan' in user_json:
            clan_info = user_json['clan']
            print('Clan name: ' + clan_info['name'])
            print('Clan tag: ' + clan_info['tag'])
            print('Clan level: ' + str(clan_info['clanLevel']))
    else:
        print('Player not found.')

def get_clan_members(clan_tag):
    clan_tag_encoded = quote(clan_tag)
    response = requests.get(
        f'https://api.clashofclans.com/v1/clans/{clan_tag_encoded}/members', headers=headers)
    if response.status_code == 200:
        members_json = response.json()
        print("Clan Members Information:")
        for member in members_json['items']:
            print(f"Name: {member['name']}")
            print(f"Rank: {member['clanRank']}")
            print(f"Town Hall Level: {member['townHallLevel']}")
            print(f"Role: {member['role'].capitalize()}")
            print("------------------------")
    else:
        print('Clan not found.')

def get_clan_war_league(clan_tag):
    clan_tag_encoded = quote(clan_tag)
    response = requests.get(
        f'https://api.clashofclans.com/v1/clans/{clan_tag_encoded}/currentwar/leaguegroup', headers=headers)
    if response.status_code == 200:
        league_json = response.json()
        print("Clan War League Information:")
        for member in league_json['clans']:
            townhall_levels = defaultdict(int)
            for war_member in member.get('members', []):
                townhall_level = war_member.get('townHallLevel', 'N/A')
                townhall_levels[townhall_level] += 1
            print(f"{member['name']}:")
            for townhall_level, count in sorted(townhall_levels.items(), reverse=True):
                if townhall_level != 'N/A':
                    print(f"Townhall {townhall_level}: {count}")

            # Sort the townhall_levels dictionary by key before plotting
            townhall_levels = dict(sorted(townhall_levels.items()))

            # Plotting the graph
            labels = list(townhall_levels.keys())
            values = list(townhall_levels.values())
            indexes = np.arange(len(labels))
            plt.bar(indexes, values)
            plt.xticks(indexes, labels)
            plt.title(f"Townhall Levels in {member['name']}")
            plt.xlabel('Townhall Level')
            plt.ylabel('Count')

            # Save the plot as an image in a folder
            if not os.path.exists('clan_graphs'):
                os.makedirs('clan_graphs')
            plt.savefig(f'clan_graphs/{member["name"]}.png')
            plt.close()
    else:
        print('Clan not found or no ongoing war.')

def main():
    while True:
        print("1. Get user information")
        print("2. Get clan's information")
        print("3. Get clan war league information")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            player_tag = input("Enter player tag: ")
            get_user(player_tag)
        elif choice == '2':
            clan_tag = input("Enter clan tag: ")
            get_clan_members(clan_tag)
        elif choice == '3':
            clan_tag = input("Enter clan tag: ")
            get_clan_war_league(clan_tag)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()