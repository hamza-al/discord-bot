# IDEK

IDEK is a Minecraft simulation discord bot with an additional random command set completely unrelated to Minecraft.

## Requirements

To use the bot, use the  package manager [pip](https://pip.pypa.io/en/stable/) to install required packages by running:

### On macOS/linux: 
```bash
pip3 install requirements.txt
```
### On Windows: 
```bash
pip install requirements.txt
```
Note: Python 3.x must be installed on your machine.

## Initilazation

1. Create a file called *users.json* in the **discord-bot** directory
2. Add the following starter code to *users.json*:
   ``` json
   {"users":[]}
   ```
3. Follow the steps [here](https://discordpy.readthedocs.io/en/stable/discord.html) to add the bot to discord.
4. Add the token obtained in step 3 in thr *bot.py* file in place of the  ```tokenNew``` variable
5. Right click on the main channel of the server and copy the channel ID
6. Add the ID obtained in step 5 in place of the ```channelIdOld``` variable

## Usage

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


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)