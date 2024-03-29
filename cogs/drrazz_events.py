import discord

from io import BytesIO
from utils import default, lists
from discord.ext import commands

class drrazz_events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    def is_in_guild(guild_id):
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(predicate)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if member.bot:
            return
        if guild.id == lists.drrazz_serverid:
            generalembed = discord.Embed(description=f"Bienvenue {member.mention} sur le serveur de DrraZz_.\nJe te conseil d'aller lire les règle du serveur dans <#818314179508568126>.\nSi tu veux avoir des notification quand <@377944202710876161> va en live sur twitch ou sort une nouvelle vidéo sur youtube va dans <#818474275362963486>.", colour=discord.Colour(0x36393f))
            generalembed.set_author(name="Bienvenue!", icon_url="https://cdn.discordapp.com/emojis/612355003151286278.gif")

            role = guild.get_role(818475324631023656)
            await member.add_roles(role)

            generalchannel = guild.get_channel(818313526720462870)
            rulechannel = guild.get_channel(818314179508568126)
            await generalchannel.send(embed=generalembed)
            await rulechannel.send(f"{member.mention} Merci de lire les règlements!", delete_after=10)

    @commands.command()
    @is_in_guild(818313526720462868)
    async def twitch(self, ctx):
        """ Montre le lien de la chaine twitch de DrraZz_. """
        await ctx.reply("<:twitch:818473720288378980> Voici le lien du twitch de DrraZz_: <https://www.twitch.tv/drrazz_>", mention_author=True)

    @commands.command()
    @is_in_guild(818313526720462868)
    async def youtube(self, ctx):
        """ Montre le lien de la chaine youtube de DrraZz_. """
        await ctx.reply("<:youtube:818473733785649183> Voici le lien de la chaine youtube de DrraZz_: <https://www.youtube.com/channel/UC-bGc-EQVsAshuL4f4TupeQ>", mention_author=True)

def setup(bot):
    bot.add_cog(drrazz_events(bot))
