import json
import os
import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from DrissionPage import ChromiumPage, WebPage

def get_data():
    page = ChromiumPage('127.0.0.1:9220')

    data_list = []
    try:
        with open('list_all.json', 'r', encoding='utf-8') as f:
            json_str = f.read()
        data_json = '[' + json_str[0:-2] + ']'
        dl_list = json.loads(data_json)
        for dl in dl_list:
            data_list.append(dl['视频链接'])
    except:
        pass

    url = 'https://www.youtube.com/results?search_query=China+Travel'
    # page.get(url)
    # time.sleep(3)

    while True:
        soup = BeautifulSoup(page.html, 'lxml')
        soup_div = soup.select('.text-wrapper.style-scope.ytd-video-renderer')
        print(f"{len(soup_div)}")

        if '无更多结果' in soup.text or len(soup_div) >= 500:
            break

        page.scroll.to_bottom()
        time.sleep(2)

    soup = BeautifulSoup(page.html, 'lxml')
    soup_div = soup.select('.text-wrapper.style-scope.ytd-video-renderer')
    for sd in soup_div:
        # try:
            data = {}
            data['关键词'] = 'china travel'
            data['视频标题'] = sd.select('#title-wrapper')[0].text.replace('\n', '').strip()  # 标题
            data['时间'] = sd.select('.inline-metadata-item.style-scope.ytd-video-meta-block')[1].text  # 时间
            data['视频链接'] = 'https://www.youtube.com' + sd.select('#title-wrapper a')[0]['href']  # 视频链接
            # if data['视频链接'] not in data_list and 'shorts' not in data['视频链接']:
            if data['视频链接'] not in data_list and 'shorts' not in data['视频链接']:
                data_list.append(data['视频链接'])
                print(data)

                with open('list_all.json', 'a', encoding='utf8') as f:
                    f.write(json.dumps(data, ensure_ascii=False) + ',\n')
                with open('list.json', 'a', encoding='utf8') as f:
                    f.write(json.dumps(data, ensure_ascii=False) + ',\n')
        # except:
        #     pass


def get_detail():
    page = ChromiumPage('127.0.0.1:9220')

    with open('list.json', 'r', encoding='utf-8') as f:
        json_data = f.read()
    datajson = json_data[0:-2]
    datajson = '[' + datajson + ']'
    datalist = json.loads(datajson)

    for data in datalist:
        try:
            url = data.get('视频链接')
            print(url)
            page.get(url)
            time.sleep(3)

            page.eles('tag:tp-yt-paper-button')[2].click()
            time.sleep(2)

            soup = BeautifulSoup(page.html, 'lxml')

            data['发布者名称'] = soup.select('#text-container .yt-simple-endpoint.style-scope.yt-formatted-string')[0].text.replace('\n', '').strip()

            data['播放量'] = ''
            soup_info = soup.select('.style-scope.yt-formatted-string.bold')
            for si in soup_info:
                if '次观看' in si.text:
                    data['播放量'] = si.text.replace('次观看', '').replace('\n', '').strip()
                if '年' in si.text and '月' in si.text:
                    data['时间'] = si.text.replace('\n', '').strip()
            if data['播放量'] == '':
                data['播放量'] = soup.select('#view-count')[0]['aria-label'].replace('次观看', '').replace('\n', '').strip()

            data['评论数'] = soup.select('.count-text.style-scope.ytd-comments-header-renderer')[0].text.replace('条评论', '').strip()

            data['视频内容简介'] = soup.select('.style-scope.ytd-text-inline-expander')[0].text.replace('\n', '').strip()

            print(data)
            with open('data.json', 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False) + ',\n')
        except:
            page.ele('#button-shape').click()
            time.sleep(1)
            page.ele('c:.style-scope.ytd-menu-service-item-renderer').click()
            time.sleep(2)

            soup = BeautifulSoup(page.html, 'lxml')
            try:
                data['时间'] = '2024年' + soup.select('.YtwFactoidRendererFactoid')[2].text.strip()[:6]
            except:
                pass

            try:
                data['播放量'] = soup.select('.YtwFactoidRendererFactoid')[1].text.replace('观看次数', '').replace('\n', '').strip()
            except:
                pass

            print(data)
            with open('data.json', 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False) + ',\n')

def save():
    with open('data.json', 'r', encoding='utf-8') as f:
        json_str = f.read()
    data_json = '[' + json_str[0:-2] + ']'
    data_list = json.loads(data_json)

    df = pd.DataFrame(data_list)
    df.to_excel('youtube.xlsx', index=False, encoding='utf-8-sig')


get_data()
get_detail()
save()
