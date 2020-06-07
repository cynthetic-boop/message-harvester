# message-harvester
A simple Discord bot written in discord.py to collect messages from a given @ username into a .txt file for data use.

This bot has one simple command, dlchat, where it will output all of the found messages from a specific user and outputs them into a .txt
file title formatted to their id and the sevrer and channel it is from.  The prefix is 'h!' without the quotes.  The output .txt file will
be within the same directory as the bot.py file is in, so I would recommend running it within it's own folder, especially if you plan to 
run the command a lot.  Also make sure to run the bot from the command line (Powershell, CMD, Terminal, Bash, etc.) so that you can see
exactly when and where the bot's commands are run.

**BEWARE OF PULLING FROM LARGE OR OLD SERVERS(EVEN RELATIVELY SMALL ONES), IT MAY CAUSE RATELIMITING** 
Seriously, it may ratelimit you very hard.  This is a primitive bot, so no checks are put into place for this, you need to be aware.
(I will test this soon if I am able get the courage to do it on my older servers.)

Things I may add in the future:
- Multiple users downloading (would very likely be ratelimited)
- Better options for formatting the output to your liking
- More verbose outputs in the terminal, optional changes
- Is CLI possible? (I don't think it is)
