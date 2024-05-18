# Clash of Bots Documentation 🛡️⚔️🤖🎮  
  
### Introduction
This Python script provides functionalities to interact with the Clash of Clans API. It allows users to retrieve information about players, clans, and clan war leagues.

### Features
- Retrieve player information including name, tag, trophies, level, best trophies, clan name, clan tag, and clan level.
- Get information about clan members including their name, rank, town hall level, and role.
- Access clan war league information including town hall levels distribution within the clan.

## Discord Screenshot
![discord screenshot](/example_screenshots/Discord_QzIRlL3heM.png)
## Python Script Screenshot
![python script](/example_screenshots/Code_NQvyIqdSCJ.png)
## Matplotlib Graph
![matplotlib graph](/clan_graphs/COYG.png)





## Python Script Documentation

### Prerequisites
- Python 3.x installed on your system.
- Install the required Python packages using pip: ```pip install requests python-dotenv matplotlib discord.py```

### Usage
1. **Player Information**
 - Enter choice `1`.
 - Provide the player tag when prompted.

2. **Clan Information**
 - Enter choice `2`.
 - Provide the clan tag when prompted.

3. **Clan War League Information**
 - Enter choice `3`.
 - Provide the clan tag when prompted.

4. **Exit**
 - Enter choice `4`.

### Environmental Variables
Ensure to set the following environmental variables:
- `CLASH_TOKEN`: Your Clash of Clans API token.
- `DISCORD_TOKEN`: Your Discord bot token (if you're using the Discord bot).

### Running the Script
1. Navigate to the directory containing the Python script.
2. Run the script using the following command:

## Discord Bot Documentation

### Introduction
This Discord bot extends the functionality of the Clash of Clans Python script to provide real-time interaction within Discord servers.

### Features
- Responds to user queries in Discord channels.
- Supports commands for retrieving player information, clan information, and clan war league details.
- Restricts the bot's response to a maximum of 2000 characters to prevent message overflow.

### Prerequisites
- Python 3.x installed on your system.
- Discord account for creating and deploying bots.
- Install the required Python packages using pip: ```pip install discord.py requests python-dotenv matplotlib```

### Setup
1. **Create a Discord Bot**
 - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
 - Navigate to the "Bot" tab and click on "Add Bot" to create a bot user.
 - Copy the bot token to use later.

2. **Environmental Variables**
 - Set the following environmental variables:
   - `DISCORD_TOKEN`: Your Discord bot token.
   - `CLASH_TOKEN`: Your Clash of Clans API token.

3. **Run the Bot**
 - Run the Discord bot script using the following command:
   ```python discord_bot.py```

### Bot Commands
- `?clan [CLAN_TAG]`: Retrieves information about the specified clan.
- `?war [CLAN_TAG]`: Retrieves clan war league information for the specified clan.
- `?player [PLAYER_TAG]`: Retrieves information about the specified player.

### Usage
1. Invite the bot to your Discord server using the generated bot invite link.
2. Use the specified commands in any text channel to interact with the bot.

---

Feel free to customize and extend the functionality of the provided scripts to suit your needs! 🚀
