# IDEK

IDEK is a Minecraft simulation discord bot with an additional random command set completely unrelated to Minecraft.

## Requirements

To use the bot, use the  package manager [pip](https://pip.pypa.io/en/stable/) to install required packages by running:

### On macOS/linux: 
```bash
pip3 install discord.py
pip3 install requests
```
### On Windows: 
```bash
pip install discord.py
pip install requests
```
Note: Python 3.x must be installed on your machine.

## Initilazation
Note: If you are using a Windows based machine, download and install git from [here](https://git-scm.com/) to be able to clone this repository.

1. Clone the repository by running the following in in CMD or terminal on windows/ (macOS or linux) respectively:
   ``` bash
   git clone https://github.com/hamza-al/discord-bot.git
   ```

2. Create a file called *users.json* in the **discord-bot** directory
3. Add the following starter code to *users.json*:
   ``` json
   {"users":[]}
   ```
4. Follow the steps [here](https://discordpy.readthedocs.io/en/stable/discord.html) to add the bot to discord.
5. Add the token obtained in step 3 in the *bot.py* file in place of the  ```tokenNew``` variable
6. Right click on the main channel of the server and copy the channel ID
7. Add the ID obtained in step 5 in place of the ```channelIdOld``` variable

### Urban dictionary functions
To make the urban dictionary functionality work, follow the instructions [here](https://dev.to/nhighleysalongenius/comment/epgk) to obtain the api key required, and place than in plac eof the ```urbankey``` variable

### Tenor GIF functions
To make the gif finding functionality work, follow the instructions [here](https://tenor.com/gifapi/documentation#quickstart) to obtain the api key required, and place than in plac eof the ```apikeygif``` variable

## Start up

To run the bot, use the following commands in the **discord-bot** directory:
### On macOS/linux (In Terminal): 
```bash
python3 bot.py
```
### On Windows (in CMD): 
```bash
python bot.py
```
Note: Python 3.x must be installed on your machine.

## Usage:
Once the bot is online: Use the ">help" to get the list of commands supported by the bot. Any command must be preceeded by the ">" symbol.

