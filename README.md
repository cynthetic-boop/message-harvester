# message-harvester
A simple Discord bot written in discord.py to collect messages from a given @ username into a .txt file for data use.

This bot has one simple command, dlchat, where it will output all of the found messages from a specific user and outputs them into a .txt
file title formatted to their id and the server and channel it is from.  The prefix is 'h!' without the quotes.  The output .txt file will
be within the same directory as the bot.py file is in, so I would recommend running it within it's own folder, especially if you plan to
run the command a lot.  Also make sure to run the bot from the command line (Powershell, CMD, Terminal, Bash, etc.) so that you can see
exactly when and where the bot's commands are run.

**INSTALLATION AND USAGE**
- Make sure you have Python 3.8.1 or newer (I haven't tested it on anything else yet)
- Download the .zip file or clone and put all contained files in a separate folder where you will
run the bot.py file
- Open a terminal or other shell window in that directory
- run `pip install -r requirements.txt`, or `pip3 install -r requirements.txt` if you have
multiple versions of python
- Make a file named just `.env` with the token in it formatted `TOKEN=<your_bot_token_here>` in the same directory as the rest of the bot's files.  
If you don't know how to get a bot token, search up how to make a discord bot.  **REMEMBER NOT TO SHARE YOUR DISCORD BOT TOKEN WITH ANYONE OR UPLOAD WITH ANY CODE**
- run the command `python bot.py` or `python3 bot.py`, same reason as above
- In the server and channel you want to download messages from, call the command
`h!dlchat <@username>`
- The output will be saved to a .txt file with a long name describing the location and
user ID that the messages are from

**BEWARE OF PULLING OFTEN, ESPECIALLY FROM LARGE OR OLD SERVERS(EVEN RELATIVELY SMALL ONES), IT MAY CAUSE RATELIMITING**
Seriously, it may ratelimit you very hard.  This is a primitive bot, so no checks are put into place for this, you need to be aware.
(I will test this soon if I am able get the courage to do it on my older servers.)

Things I may add in the future:
- Specify what channel you want to download from
- Removing links and images from the file (images dont go in, but they add extra lines)
- Multiple users downloading (would very likely be ratelimited)
- Improve consistency of the bot's outputs, and make it a litte more human readable
- Better options for formatting the output to your liking
- More verbose outputs in the terminal, optional changes
- Is CLI possible? (I don't think it is)
