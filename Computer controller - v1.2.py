import discord
import os
import webbrowser

client = discord.Client()

token = "Secure"

@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("지민님의 명령을 기다리는 중")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if message.content == "!!컴퓨터 종료":
        await message.channel.send("정상 인식")
        os.system("shutdown -s -t 0")

    if message.content == "!!네이버":
        await message.channel.send("정상 인식")
        webbrowser.open("https://naver.com")

    if message.content == "!!유튜브":
        await message.channel.send("정상 인식")
        webbrowser.open("https://youtube.com")

    if message.content == "!!구글":
        await message.channel.send("정상 인식")
        webbrowser.open("https://google.com")

    if message.content == "!!컴퓨터 재부팅":
        await message.channel.send("정상 인식")
        os.system("shutdown -r -f -t 0")
        
        

client.run(token)
