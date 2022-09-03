import discord
import os

client = discord.Client()

token = "Secure"


@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("당신이 욕을 쓰는 것을 막기 - 문의, 건의 : ljm22w@naver.com")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    if "시발" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "지랄" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅅㅂ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "개새끼" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅅㅂㅅㄲ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "야발" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "fuck" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅄ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅂㅅ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "병신" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "애미" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "좆" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅈ같네" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "미친놈" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "미친년" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "시12발" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "시1발" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "뒤질" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "뒤진" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "지1랄" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "지12랄" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "지3랄" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "십발" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "섹스" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "섻스" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "보지" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    if "자지" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "헤으응" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "하앗" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "썅" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "뒤져" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅈ같은" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅈ까" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅂ신" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "느금마" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "뒤짐" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㄴㄱㅁ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "쉬불" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "시바" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "븅신" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅅ발" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅈ되네" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "시뱔" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅅ뱔" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "병ㅅ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        

    if "ㅅㅅ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    if "ㅈㄲ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    link = "xvideos.com" "xxx.com" "levea.xyz" "pornhub.com"" hitomi.la" "tema79.com"
    
    if "xvideos.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "xxx.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "levea.xyz" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "pornhub.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "hitomi.la" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "tema79.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "xhamster.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "e-hentai.org" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "danbooru.donmai.us" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "gelbooru.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "luscious.net" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "nhentai.net" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "nhentai.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "rule34.paheal.net" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "sankakucomplex.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "thumbzilla.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "tsumino.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "zone-archive.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "hellven.net" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "hs002.chatovod.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "uriminzokkiri.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "rodong.rep.kp" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "dprktoday.com" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "kcna.kp" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "XVIDEOS.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "XXX.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "LEVEA.XYZ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "PORNHUB.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "HITOMI.LA" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "TEMA79.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "XHAMSTER.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "E-HENTAI.ORG" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "DANBOORU.DONMAI.US" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "GELBOORU.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "LUSCIOUS.NET" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "NHENTAI.NET" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "NHENTAI.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "RULE34.PAHEAL.NET" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "SANKAKUCOMPLEX.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "THUMBZILLA.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "TSUMINO.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "ZONE-ARCHIVE.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "HELLVEN.NET" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "HS002.CHATOVOD.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "URIMINZOKKIRI.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "RODONG.REP.KP" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "DPRKTODAY.COM" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "KCNA.KP" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("유해사이트가 감지되어 삭제되었습니다.")
        print('link 감지, 정상 삭제 완료')
        
    if "FUCK" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    if "시 발" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    if "새끼야" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    if "빙신" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    if "병 신" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        
    if "ㅈ ㄲ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')
        

    if "ㅗ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅅ1ㅂ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

    if "ㅈㄹ" in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send("욕이 감지되어 삭제되었습니다.")
        print('욕 감지, 정상 삭제 완료')

        
    if message.content == "?!명령어":
        await message.channel.send("명령어는 아래와 같습니다.")
        await message.channel.send("?!구동현황 : 현재 봇 구동현황 메세지 출력")
        await message.channel.send("?!명령어 : 명령어 안내")
        await message.channel.send("?!만든이 : 만든 사람이 누군지 안내")
        await message.channel.send("?!버전 : 현재 무슨 버전인지 안내")
        await message.channel.send("?!건의 : 문의, 건의를 할 수 있는 이메일을 알려드립니다.")
        await message.channel.send("?!디스코드 : 노퍽봇의 공식 디스코드 서버 주소를 안내드립니다. ")
        await message.channel.send("?!깃허브: 개발자의 깃허브를 안내드립니다.")
        await message.channel.send("?!도움주신분: 노퍽봇 개발에 도움 주신분들의 명단을 안내드립니다.")
        print('명령어 안내 메세지 출력')

    if message.content == "?!구동현황":
        await message.channel.send("정상적으로 구동중입니다.")
        print('구동 현황 메세지 출력')

    if message.content == "?!만든이":
        await message.channel.send("제작: 6L5TPR (이지민)")
        print('만든이 메세지 출력')

    if message.content == "?!버전":
        await message.channel.send("현재 버전은 V1.7으로, 2022년 8월 10일에 업데이트 되었습니다.")
        print('버전 메세지 출력')
        
    if message.content == "?!건의":
        await message.channel.send("ljm22w@naver.com")
        print('건의 메시지 출력')

    if message.content == "?!디스코드":
        await message.channel.send("https://discord.gg/jbkAthkF6R")
        print('디스코드 메시지 출력')

    if message.content == "?!깃허브":
        await message.channel.send("개발자 깃허브: https://github.com/ljm22w")
        print('깃허브 메세지 출력')

    if message.content == "?!도움주신분":
        await message.channel.send("피드백 해주신 분: 6L5TNG 쿵쿵왕, 배승빈")
        print('도움주신 분 메시지 출력')




client.run(token)
