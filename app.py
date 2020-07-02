from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('nYqDJxzAk7tkYs12gZMuzXL90+UR85f5o38LhXFCBtdIoMYjm8Sy4Q/YsQUcwGRVk9oBOYA3kIo2j+B8NGRNCRP1KFP4Xkn7bRKKOlC5jcFcpg/zeeSnodXbFTni1mqyOj24P9OjoOyIpIx0gnDzJgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('87d7aa31df62e10ee26d09a4db780ab9')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "你好"
    if msg in ['Hi','hi']:
        r = "嗨"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r))


if __name__ == "__main__":
    app.run()