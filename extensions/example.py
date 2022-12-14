# from random import randint
# from random import choice
# from ssl import Options
# from typing import Optional
# from art import text2art

import hikari
import lightbulb
import random

plugin = lightbulb.Plugin('Example')


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event):
    pass


@plugin.command
@lightbulb.command("about", "About Me")
@lightbulb.implements(lightbulb.SlashCommand)
async def about(ctx):
    linkembed = (
        hikari.Embed(title="About Me, the PM", description="मैं चुटिया हूं|")
        .add_field("वादे", "मैं कभी नहीं निभाता।")
        .add_field("वोट", "राम जी की कृपा से मिल जाते हैं।")
        .add_field("प्रधान मंत्री", "इसलिये हूं क्युकी सामने वाला मुझसे भी बड़ा चुटिया है।")
        .add_field("मैहंगाई", "बढ़ूंगा और अपने दोस्तों की मदद करुंगा।")
        .add_field("जनता", "मर जाए, मुझे क्या।")
        .set_thumbnail("https://i.imgur.com/BPfttKL.png")
        .set_footer("भारत माता की जय। जय हिन्द।")
    )
    await ctx.respond(linkembed)


@plugin.command
@lightbulb.command("namaste", "namaskar")
@lightbulb.implements(lightbulb.SlashCommand)
async def namaste(ctx):
    await ctx.respond(f'नमस्कार मित्रों।')


milestones = ["राममंदिर किसके वजह से बन रहा है भई?", "जम्मू-कश्मीर को भारत का अंग किसने बनाया, मैंने नहीं क्या?",
              "भारत को पाकिस्तान से भी  नीचे हंगर इंडेक्स में किसने लाया?",
              "फ्रॉम डेमोक्रेसी टू डिक्टेटरशिप :sunglasses:"]


@plugin.command
@lightbulb.command("works", "achievements")
@lightbulb.implements(lightbulb.SlashCommand)
async def ms(ctx):
    await ctx.respond(f'{random.choice(milestones)}')


@plugin.command
@lightbulb.command("friends", "my friends")
@lightbulb.implements(lightbulb.SlashCommand)
async def friends(ctx):
    await ctx.respond(
        f'अडानी, अम्बानी, बिड़ला, एवं ऐसे कई अरबपति मेरे प्रिय मित्र हैं। फिर भी जनता को "मित्रों" बोल के पोपट बनाता रहता हूँ। ')


@plugin.command
@lightbulb.command("glt", "glt")
@lightbulb.implements(lightbulb.SlashCommand)
async def glt(ctx):
    await ctx.respond(f'ज्ञान प्रकाश गलत बोल रहा है। :joy3d:')


@plugin.command
@lightbulb.command("bak", "bak")
@lightbulb.implements(lightbulb.SlashCommand)
async def bak(ctx):
    await ctx.respond(f'पोमोडोरो में बकवास मत करो प्लीज।')


@plugin.listener(hikari.MessageCreateEvent)
async def event1(event):
    if not event.content == "":
        if not event.author.is_bot:
            if "modi" in event.content.lower() and (
                    "jumla" in event.content.lower() or "जुमला" in event.content.lower() or "jumle" in event.content.lower()):
                await event.message.respond(f"घर पे CBI, ED भिजवा दूंगा तुम्हारे <@{event.author.id}>।")
                await event.message.respond(
                    f"https://tenor.com/view/6crore-followers-for-prime-minister-narendra-modi-trending-narendra-modi-modi-pm-gif-18494788")
            elif "modi" in event.content.lower() and (
                    "mahangai" in event.content.lower() or "mehangai" in event.content.lower() or "berozgaari" in event.content.lower() or "तानाशाह" in event.content.lower() or "महंगाई" in event.content.lower() or "बेरोज़गारी" in event.content.lower() or "tanashah" in event.content.lower() or "dictator" in event.content.lower()):
                await event.message.respond(f'https://tenor.com/view/sajjan-modi-gif-18209517', reply=True)
