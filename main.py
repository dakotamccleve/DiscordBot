import discord


client = discord.Client()


@client.event
async def on_message(message):
    if message.channel.id == 453039886501543946:  # Noodles & Ramen Channel ID for MokkuSylvan stuff 453039886501543946
        if message.content.find("Sylvan Dragon") != -1 or message.content.find("Mokkurkalfi") != -1:
            target_channel = client.get_channel(827958096974053446)  # Avalon-Raiders channel 827958096974053446
            await target_channel.send("<@&827958166150709248> " + "<@&832704792681250846> " + message.content)


client.run("ODMzODQzNzk3ODkyNzkyMzIx.YH4QQg.j7CmVW2E4n8zel68RjL4l1Zm8hM", bot=False)
