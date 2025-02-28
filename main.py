import os
import discord
from discrod.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_perfix='!', intents=discord.intents.all())








@bot.event
async def on_ready():
    print("Bot online!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)") 


# แจ้งคนเข้า-ออกเซิฟเวอร์

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1304623235647930379)  # ID ห้อง
    text = f"Wellcom to the server, {member.mention}!"
    await channel.send(text) # ส่งข้อความไปที่ห้องนั้น
    await channel.send(embed = emmbed)
    await member.send(text) # ส่งข้อความไปที่แชทส่วนตัวของ member

    emmbed = discord.emmbed(title = 'Wellcom to the server!' , description = text , color = 0x66FFFF)
   


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1304623235647930379)  # ID ห้อง
    text = f"{member_name} has left the server!"
    await channel.send(text) # ส่งข้อความไปที่ห้องนั้น
    



# คำสั่งแชทบอท
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello It's me") # ส่งกลับไปที่ห้องนั้น

    elif mes == 'hi bot':
        await message.channel.send("Hello, " + str(message.author.name))

await bot.process_commands(message)
# ทำคำสั่ง event แล้วค่อยไปทำ bot commands ต่อ





# \\\\\\\\\\\\\ Commands \\\\\\\\\\\\\
# กำหนดคำสั่งบอท

@bot.command()
async def hallo(ctx):
    await cxt.send(f"hallo {ctx.author.name}!")


@bot.command()
async def text(ctx, arg):
    await ctx.send(arg)
    await bot.process_commands(ctx)


# slash commands
@bot.tree.command(name='hellobot', Description='Replies with Hello')
async def hellocommand(interaction):
    await.interaction.response.send_message("hello It's me BOT DISCORD")


@bot.tree.command(name='name')
@app_commands.describe(name = "What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hello {name}")




# Embeds

@bot.tree.command(name='help', Description='bot command')
async def helpcommand(interaction):
    emmbed = discord.Embed(title='help Me! - Bot Commands' ,
    description='Bot commands',
    color=0x66FFFF,
    timestamp= discord.utils.utcnow())


  # ใส่ข้อมูล
emmbed.app_field(name='/hello1', value='Hello command', inline=True)
emmbed.app_field(name='/hello2', value='Hello command', inline=True)
emmbed.app_field(name='/hello3', value='Hello command', inline=False)

emmbed.set_auther(name='Author', url='https://www.youtube.com/@pond_na/channels', icon_url='https://media.discordapp.net/attachments/1337053105010769953/1343788810806235207/4b7afdb7e3f6e4852b54e9bb74e9a098_1.jpg?ex=67be8c5a&is=67bd3ada&hm=cbb40265c0157987779f8561fcfbca7509f8e57a3e4913138ce061a81eb5f5db&=&format=webp&width=468&height=468' )

# ใส่รูปเล็ก-ใหญ่ 
emmbed.set_thumbnal(url='https://media.discordapp.net/attachments/1337053105010769953/1343790059328901130/IMB_SzvuP4.gif?ex=67be8d84&is=67bd3c04&hm=5fe60ca3dc5987d4f774f31197b6744923df36c79038887afbf595582e380331&=')
emmbed.set_image(url='https://media.discordapp.net/attachments/1337053105010769953/1343790059681353778/IMG_5123.gif?ex=67be8d84&is=67bd3c04&hm=0d2dd5f6b3afcb722e3776fd360fbcd973f95d52df1cf446a6af3a130d5bd89f&')


# Footer เนื้อหาส่วนท้าย
emmbed.set_footer(text='Footer',icon_url='https://media.discordapp.net/attachments/1337053105010769953/1343790059328901130/IMB_SzvuP4.gif?ex=67be8d84&is=67bd3c04&hm=5fe60ca3dc5987d4f774f31197b6744923df36c79038887afbf595582e380331&=')


await interaction.response.send_message(embed = emmbed)


server_on()

bot.run(os.getenv('TOKEN'))