import discord
import random

from utils import default
from discord.ext import commands
from discord.ext.commands import errors
from utils import permissions, default


class Ecorte(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    def is_in_guild(guild_id):
        async def predicate(ctx):
            return ctx.guild and ctx.guild.id == guild_id
        return commands.check(predicate)

    @commands.command(aliases=['rb'])
    @commands.cooldown(1, 300, commands.BucketType.guild)
    @commands.has_any_role(818207098877116417)
    @is_in_guild(324284116021542922)
    async def rainbow(self, ctx):
        """ Change la couleur du rôle rainbow. """
        role = ctx.guild.get_role(818207098877116417)
        r = discord.Colour.random()
        await role.edit(color=r)
        embed = discord.Embed(
            description=f"Tu viens de changer la couleur du rôle <@&818207098877116417> pour {r}. \nTu peut rechanger la couleur du rôle <@&818207098877116417> dans 5 minutes.", color=r)
        embed.set_author(
            name="Rôle Rainbow", icon_url="https://media.discordapp.net/attachments/811959848921071636/822598144968884314/baa392758f065fa770e3a9063f91d33a.png")
        await ctx.reply(embed=embed, mention_author=False)

    @rainbow.error
    async def rainbow_error(self, ctx, err):
        if isinstance(err, errors.MissingAnyRole):
            await ctx.reply(f"> :x: Tu doit avoir le rôle **Rainbow**.\n > Pour avoir le rôle tu doit soit avoir le rôle **Addicte**, **No-EXP** ou **Nitro Booster**.\n > Si tu a un de ces rôles va dans <#439155130924007444> et tape **-role rainbow**.")

    @commands.command(aliases=['v'])
    @permissions.has_permissions(manage_messages=True)
    @is_in_guild(324284116021542922)
    async def verify(self, ctx, user: discord.Member):
        """ Verify someone. (Mod only) """
        staffrole = ctx.guild.get_role(797650029278920714)
        if staffrole in ctx.author.roles:
            userrole = ctx.guild.get_role(614126210422800404)
            await user.add_roles(userrole, reason=f"Manually got verified by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.reply("> :white_check_mark: Done!", mention_author=False)

    @commands.command(aliases=['uv'])
    @permissions.has_permissions(manage_messages=True)
    @is_in_guild(324284116021542922)
    async def unverify(self, ctx, user: discord.Member):
        """ Un-Verify someone. (Mod only) """
        staffrole = ctx.guild.get_role(797650029278920714)
        if staffrole in ctx.author.roles:
            userrole = ctx.guild.get_role(614126210422800404)
            await user.remove_roles(userrole, reason=f"Manually got un-verified by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.reply("> :white_check_mark: Done!", mention_author=False)

    @commands.command()
    @is_in_guild(324284116021542922)
    async def noexp(self, ctx):
        """ Se give le rôle No-EXP. """
        membrerole = ctx.guild.get_role(823227863284449352)
        noexprole = ctx.guild.get_role(823229487974055957)
        if ctx.channel.id != 439155130924007444:
            await ctx.reply("> :x: Mauvais channel. Va dans <#439155130924007444>.", mention_author=False)
        else:
            if membrerole in ctx.author.roles:
                await ctx.author.add_roles(noexprole)
                await ctx.author.remove_roles(membrerole)
                await ctx.reply("> :white_check_mark: Done!", mention_author=False)
            else:
                await ctx.reply("> :x: Tu doit avoir le rôle **Membres**.")

    @commands.command(aliases=['ap'])
    @permissions.has_permissions(manage_messages=True)
    @is_in_guild(324284116021542922)
    async def approve(self, ctx, member: discord.Member):
        """ Approuver un membres. (Mod only)"""
        staffrole = ctx.guild.get_role(797650029278920714)
        if staffrole in ctx.author.roles:
            approvedrole = ctx.guild.get_role(823691168982237185)
            await member.add_roles(approvedrole, reason=f"Manually got approved by {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.reply("> :white_check_mark: Done!", mention_author=False)


def setup(bot):
    bot.add_cog(Ecorte(bot))
