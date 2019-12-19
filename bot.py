import datetime

import requests

from Update import Update
from constants import BOT_TOKEN, BOT_SEND_METHOD, BOT_GET_METHOD, Tags
from functions import print_dict, conver_dict_to_string


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"
        print(self.api_url)

    def get_updates(self, offset=None, timeout=5):
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.api_url + BOT_GET_METHOD, params).json()

        result_json = response['result']
        # JsonFile("bot_updates").write(result_json)

        return result_json

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return Update(last_update)

    def send_text_reply(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        send_url = self.api_url + BOT_SEND_METHOD
        print(send_url, "POST")

        return requests.post(send_url, params)

    def send_sticker_reply(self, chat_id, sticker_id):
        pass


greet_bot = BotHandler(BOT_TOKEN)
greetings = ('здравствуй', 'привет', 'ку', 'здорово', 'hi', 'hello')
now = datetime.datetime.now()


def handle_message_request(last: Update, bot: BotHandler):
    if last.chat_type == "group" and "@" not in last.message_text:
        return
    
    if last.message_text:
        reply = get_reply_on_text(last)
        print(last.message_text, reply)

        bot.send_text_reply(
            last.chat_id,
            reply
        )
    elif last.sticker_id:
        reply_text = last.sticker_set_name + "\n" + last.sticker_id

        bot.send_text_reply(
            last.chat_id,
            reply_text
        )
    else:
        bot.send_text_reply(
            last.chat_id,
            conver_dict_to_string(last.get_mess_json()))


def get_reply_on_text(last: Update):
    today = now.day
    hour = now.hour

    if last.message_text.lower() in greetings:
        if today == now.day and 6 <= hour < 12:
            return f'Good morning, {last.author_name[0]}'

        elif today == now.day and 12 <= hour < 17:
            return f'Добрый день, {last.author_name[0]}'

        elif today == now.day and 17 <= hour < 23:
            return f'Good evening, {last.author_name[0]}'
    else:
        return conver_dict_to_string(last.get_mess_json()) + "\n@" + last.author_username
        # return f"Sorry, I don't understand you, {last.author_name[0]}"


def main():
    new_offset = None

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        if last_update.is_empty:
            continue

        print_dict(last_update.get_mess_json())

        handle_message_request(last_update, greet_bot)

        # last_update_id = last_update[Tags.UPDATE_ID]
        new_offset = last_update.id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
