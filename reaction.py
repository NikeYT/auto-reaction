from pyrogram import Client
from pyrogram import types, filters
from pyrogram.errors.exceptions.bad_request_400 import ReactionInvalid, ReactionEmpty
from random import choice

# Инициализация клиента / Initialize of client
app = Client(
    'my_name',
    api_id='---',
    api_hash='---'
)

@app.on_message(filters=filters.chat("---"))
def call_react(client: Client, message: types.Message):
    smile = '👎' # Смените на ваш нужный / Change to your smile
    try:
        app.send_message(chat_id=message.chat.id, message_id=message.id, emoji=choice(smile))
    except (ReactionInvalid, ReactionEmpty):
        for i in smile:
            try:
                app.send_reaction(chat_id=message.chat.id, message_id=message.id, emoji=i)
                break
            except ReactionInvalid:
                continue

if __name__ == "__main__":
    print('Script started')
    app.run()
