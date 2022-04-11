from os import write
import requests
from bs4 import BeautifulSoup
from time import time, sleep



def get_posts():
    link = 'https://lenta.ru/parts/news'
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2434 Yowser/2.5 Safari/537.36"}
    resp = requests.get(link, headers=headers).text

    # with open('lenta.txt', 'w', encoding='utf-8') as file:
    #     file.write(resp)    


    # with open('lenta.txt', 'r', encoding='utf-8') as file:
    #     resp = file.read()


    soup = BeautifulSoup(resp, 'lxml')
    # print(resp)

    list_news = soup.find_all(class_='parts-page__item')

    final_list = []

    for item in list_news:
        href = item.find('a').get('href')
        if href[0] != '/':
            continue
        try:
            title = item.find('h3').text
        except:
            continue
        final_list.append({'title': title, 'href': 'https://lenta.ru' + href})

    return final_list

    #     print(href)
    #     print(title)

# print(final_list)

# print(get_posts())


def send_message(text: str):
  link='https://discord.com/api/v9/channels/949692477248524388/messages'
  header = {'authorization': TOKEN,
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2434 Yowser/2.5 Safari/537.36"}
  data = {'content':text, 'nonce': str(int(time())), 'tts': False}
  requests.post(link, headers=header, json=data)


# send_message('test')
# print (get_posts()[0])

def loop_news():
    last_news = get_posts()[0]
    while True:
        sleep(20)
        news = get_posts()[0]
        if last_news != news: 
            text = f"```Новая новость!\n{news.get('title', '')}\n{news.get('href', '')}```"
            send_message(text)
            print(text)
            last_news = news

# loop_news()


if __name__ == "__main__":
    with open('config.txt', 'r', encoding='utf-8') as file:
        TOKEN = file.read().strip()
    loop_news()

