"""
youdotcom.Chat return:
{
    "message": str,
    "time": str,
    "v2Captcha": str,
    "type": str
}

youdotcom.Code return:
{
    "response": [],
    "time": str
}

youdotcom.Search return (check the file "search result - adam and eve"):
{
    ...
    "third_party_search_results": [
        {
            "name": str,
            "url": str,
            ...
            "snippet": str,
            ...
        }
    ],
    ...

}

youdotcom.Write return:
    {
        "response": str,
        "time": str
    }
"""

import telebot
from youdotcom import (Webdriver, Chat, Code, Search, Write)
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()

wl_path = './witelist.txt'

lf_path = './log.txt'


wite_list = []


bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
api_key = os.environ['YOU_TOKEN']


def to_log(level: str, message: str):
    log_file = open(lf_path, 'a')
    log_file.write(f'[{datetime.now()}]  [{level}]  [{message}] \n')
    log_file.close()


def to_log_info(message: str):
    to_log('INFO', message)


def to_log_war(message: str):
    to_log('WARNING', message)


def to_log_err(message: str):
    to_log('ERROR', message)


def load_wite_list(wlf: str):
    f = open(wlf, 'r')
    for line in f:
        wite_list.append(line.replace('\n', ''))
    f.close()


def chek_user_id(user_id):
    if str(user_id) in wite_list:
        return True
    else:
        return False


def you_send_text(q: str) -> str:
    if '/code' in q:
        result: str = ''

        driver = Webdriver().driver
        code = Code.find_code(driver, search=q[len('/code')+1:])

        res_list = code.get('response', [])

        for string in res_list:
            result += f'{string} \n'

        return result
    elif '/search' in q:
        result:str = ''
        search = Search.search_for(message=q[len('/search')+1:])

        res_list = search.get('results', {}).get('mainline', {}).get('third_party_search_results', [])

        for item in res_list:
            result += f"{item['name']} \n {item['snippet']} \n {item['url']} \n\n"

        return  result
    elif '/write' in q:
        result = Write.write(q[len('/write')+1:])
        return  result.get('response', 'something went wrong')
    else:
        result = Chat.send_message(message=q, api_key=api_key)
        return result.get('message', 'something went wrong')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '''
        Hi, Im "YOU Chat", lets get started. 
        Start from any words for use module "Сhat". 
        Start from "/code " for use module "Code".
        Start from "/search " for use module "Search".
        Start from "/write " for use module "Write".
    ''')


@bot.message_handler(content_types=['text'])
def send_text(message):
    user_id = message.from_user.id

    answer = "Sorry, you are denied access"

    if chek_user_id(user_id):
        to_log_info('question')
        to_log_info(message.text)

        answer = you_send_text(message.text)

        to_log_info('answer')
        to_log_info(answer)
    else:
        to_log_war(f'{user_id}: is not in access list')

    bot.send_message(message.chat.id, f'{answer}')


if __name__ == '__main__':
    # print(you_send_text('hellow ai'))
    # print(you_send_text('/code python hello world'))
    # print(you_send_text('/search adam and eve'))
    # print(you_send_text('/write smal letter about galaxy'))

    load_wite_list(wl_path)
    bot.polling()