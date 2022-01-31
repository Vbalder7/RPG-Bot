import lightbulb

plugin = lightbulb.Plugin('Help')

@plugin.command
@lightbulb.command('help', 'Help with commands')
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def _help(ctx: lightbulb.Context) -> None:
        pass

def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)