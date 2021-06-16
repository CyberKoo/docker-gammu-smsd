#!/usr/bin/env python3
import os
import requests

if __name__ == '__main__':
    numparts = int(os.environ['DECODED_PARTS'])
    text = ''
    # Are there any decoded parts?
    if numparts == 0:
        text = os.environ['SMS_1_TEXT']
    # Get all text parts
    else:
        for i in range(1, numparts + 1):
            varname = 'DECODED_{}_TEXT'.format(i)
            if varname in os.environ:
                text = text + os.environ[varname]

    text = '`接收到 {} 发送的短消息:`\n{}'.format(os.environ['SMS_1_NUMBER'], text)

    API_URL = 'https://api.telegram.org/bot{}/sendMessage'.format(os.environ['BOT_TOKEN'])
    request = {
        'chat_id': os.environ['CHAT_ID'],
        'text': text,
        'parse_mode': 'Markdown'
    }

    if os.environ['PROXY']:
        proxies = {'http': os.environ['PROXY'], 'https': os.environ['PROXY']}
    else:
        proxies = {}

    req = requests.post(API_URL, json=request, proxies=proxies)
    print(req.json())
