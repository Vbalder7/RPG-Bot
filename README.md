
# RPG Bot

We are dedicated to making a discord bot
that is used for any TTRPG (Table Top Role Playing Game),
and since we are all facing these troubling times we might find
ourselves playing these games online. So we
decided to make it Easier.

## Current Version

RPG Bot Is Currently In Version (0.1.3), as of
Friday, January 28, 2022.

## Changelog

### Version (0.1.0)

Minimal functionality. Only able to go online
nothing more. Has Error handling

### Version (0.1.1)

Added some admin commands for shutdown functionality.

### Version (0.1.2)

Added dice rolling capability
we use [d20](https://pypi.org/project/d20/) for our dice rolling.

| Syntax | Name | Description |
|---|---|---|
| k | keep | Keeps all matched values. |
| p | drop | Drops all matched values. |
| rr | re-roll | Rerolls all matched values until none match. (Dice only) |
| ro | re-role once | Rerolls all matched values once. (Dice only) |
| ra | reroll and add | Rerolls up to one matched value once, keeping the original roll. (Dice only) |
| e | explode on | Rolls another die for each matched value. (Dice only) |
| mi | minimum | Sets the minimum value of each die. (Dice only) |
| ma | maximum | Sets the maximum value of each die. (Dice only) |

### Version (0.1.3)

Now it is Possible to generate new character stats using the -randchar command

## Deployment

To deploy this project run

Create a folder in the root directory called `secrets`.
Inside there should be a file named `token` with no file extension
You should place your bot token in this file. If you wish to deploy the bot 24/7 on your own.
I suggest using heroku as the Procfile,requirements.txt, and runtime.txt are provided.
You need only make a private repository on GitHub add all files to the repository, and then build the app with heroku.
once that is done you can go to the resources tab on the heroku dashboard and refresh the page.
then turn on the choice that says bot.py

Or you could just add to server [Add to server](https://discord.com/api/oauth2/authorize?client_id=722335475976634539&permissions=8&scope=bot%20applications.commands)
