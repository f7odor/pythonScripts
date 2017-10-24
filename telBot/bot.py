import requests
import misc
import codecs
from time import sleep
from yobit import get_btc

token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'

global recent_update_id
recent_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()

    recent_object = data['result'][-1]
    current_update_id = recent_object['update_id']

    global recent_update_id
    if recent_update_id != current_update_id:
        recent_update_id = current_update_id
        chat_id = recent_object['message']['chat']['id']
        message_text = recent_object['message']['text']

        message = {'chat_id': chat_id,'text': message_text}

        return message
    return None

def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():

    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
            else:
                continue

        sleep(3)

if __name__ == '__main__':
    main()
