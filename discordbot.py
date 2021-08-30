# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODgxNzA5Mzk5MDE2NjIwMDkz.YSwx3g.ggHgy3Fo6hAAl2B_XF9lVq6aaNk'

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

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '#8888':
        await reply(message) # 返信する非同期関数を実行

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)