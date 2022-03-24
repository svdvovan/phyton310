import requests
from requests.exceptions import HTTPError

api_token = '5141126163:AAHsGi3Li68H3HjQvYypCB5zZhmWHbyi6hk'


def sendMessageTelegram(status, txt):
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
        chat_id='-1001755258893',
        text=f"Сайт {status}: " + txt
    ))


for url in ['https://jira.boxberry.ru', 'https://fitlife62.ru']:
    try:
        if(count):
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            sendMessageTelegram(status, url)
    # except HTTPError as http_err:
    #     # print(f'HTTP error occurred: {http_err}')  # Python 3.6
    #     sendMessageTelegram(url)
    #     print("1")

    except Exception as err:
        status = "недоступен"
        # print(f'Other error occurred: {err}')  # Python 3.6
        sendMessageTelegram(status, url)
        count = False

    else:
        # print('Success!')
        status = "доступен"
        # sendMessageTelegram(status, url)
        count = True


