# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.content} は受け付けました' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
        
    #p = r'\[.*\]'  # []に囲まれている任意の文字
    #msg = re.findall(p, message.content)[0]  # パターンに当てはまるものを抽出
    #msg = msg[1:-1]
    #print(msg)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
