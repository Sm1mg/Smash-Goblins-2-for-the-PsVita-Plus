import discord
import random
from datetime import datetime
from discord.ext import commands


def pront(content, lvl="DEBUG", end="\n") -> None:
    """
    A custom logging method that acts as a wrapper for print().

    Parameters
    ----------
    content : `any`
        The value to print.
    lvl : `str`, optional
        The level to raise the value at.
        Accepted values and their respective colors are as follows:

        LOG : None
        DEBUG : Pink
        OKBLUE : Blue
        OKCYAN : Cyan
        OKGREEN : Green
        WARNING : Yellow
        ERROR : Red
        NONE : Resets ANSI color sequences
    end : `str` = `\\n` (optional)
        The character(s) to end the statement with, passes to print().
    """
    colors = {
        "LOG": "",
        "DEBUG": "\033[1;95m",
        "OKBLUE": "\033[94m",
        "OKCYAN": "\033[96m",
        "OKGREEN": "\033[92m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "NONE": "\033[0m"
    }
    # if type(content) != str and type(content) != int and type(content) != float:
    #    content = sep.join(content)
    print(colors[lvl] + "{" + datetime.now().strftime("%x %X") +
          "} " + lvl + ": " + str(content) + colors["NONE"], end=end)  # sep.join(list())


# Returns a random hex code
def get_random_hex(seed = None) -> int:
    """
    Returns a random hexidecimal color code.
    
    Parameters
    ----------
    seed : `int` | `float` | `str` | `bytes` | `bytearray` (optional)
        The seed to generate the color from.
        None or no argument seeds from current time or from an operating system specific randomness source if available.

    Returns
    -------
    `int`:
        The integer representing the hexidecimal code.
    """
    random.seed(seed)
    return random.randint(0, 16777215)


# Creates a standard Embed object
def get_embed(ctx: commands.Context, title: str=None, description: str=None, *, url: str=None, color: discord.Color|int=None) -> discord.Embed:
    """
    Quick and easy method to create a discord.Embed that allows for easier keeping of a consistent style

    Parameters
    ----------
    ctx : `commands.Context`
        The Context to draw author information from.
    title : `str` (optional)
        The title of the embed. Can only be up to 256 characters.
    description : `str` (optional)
        The description of the embed. Can only be up to 4096 characters.
    url : `str` | `None` (optional)
        The URL of the embed.
    color : `discord.Color` | `int` (optional)
        The color of the embed.

    Returns
    -------
    `discord.Embed`:
        The embed generated by the parameters.
    """
    if color is None:
        color = get_random_hex(ctx.author.id)
    embed = discord.Embed(
        title=title,
        description=description,
        url=url,
        color=color
    )
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.display_avatar.url)
    return embed


# Creates and sends an Embed message
async def send(ctx: commands.Context, title: str=None, description: str=None, *, url: str=None, color: discord.Color|int=None, ephemeral: bool = False) -> None:
    """
    A convenient method to send a get_embed generated by its parameters.

    Parameters
    ----------
    ctx : `commands.Context`
        The Context to draw author information from.
    title : `str` (optional)
        The title of the embed. Can only be up to 256 characters.
    description : `str` (optional)
        The description of the embed. Can only be up to 4096 characters.
    url : `str` | `None` (optional)
        The URL of the embed.
    color : `discord.Color` | `int` (optional)
        The color of the embed.
    ephemeral : `bool` = `False` (optional)
        Whether the message should be ephemeral
    """
    embed = get_embed(ctx, title=title, description=description, url=url, color=color)
    await ctx.reply(embed=embed, ephemeral=ephemeral, mention_author=False)