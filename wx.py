#!/usr/bin/env python3
# coding: utf-8

from wxpy import *

import time
import datetime

import  requests
# 扫码登陆
bot = Bot()
# 初始化图灵机器人 (API key 申请: http://tuling123.com)
tuling = Tuling(api_key='06f7d22826fa40e89e9782967384789e')

# CITY_NAME = ''  // 城市名称
# Date_String = ''   // 日期
# weatherInfo = ''  // 天气描述
# weatherInfoNight = '' //晚上天气描述
# temperatureMax = ''   // 最高温度
# temperatureMin = '' // 最低气温
# wind_dir       = ''    // 风向
# wind_sc         = '' //风力
# bodytemperature = '' // 体感温度
# sunRaise = ''   // 日出时间
# sunDown = ''  // 日落时间
# vis   = '' // 能见度
# pop   = '' // 降水概率
#
# temperature = '' //当前温度

XIAOKEZI = '小可💕'
CHING = 'Ching'
KONG  = 'Mr.K'
CHI   = '大河奔流'
DENG  = 'Melody💭'


nameMap = {XIAOKEZI:'北京', CHING:'贵阳',KONG:'北京',CHI:'天津',DENG:'大连'}

def getWeather(location):
    url = 'https://free-api.heweather.com/s6/weather?location='+location+'&key=4303dea218f6422ebf378e6ac0eba9ff'
    r = requests.request('get', url)
    text = r.json()
    data = text['HeWeather6'][0]
    CITY_NAME = data['basic']['location']

    today =  data['daily_forecast'][0]
    Date_String = today['date']
    weatherInfo = today['cond_txt_d']
    weatherInfoNight = today['cond_txt_n']
    temperatureMax = today['tmp_max']
    temperatureMin = today['tmp_min']
    wind_dir = today['wind_dir']
    wind_sc = today['wind_sc']
    sunRaise = today['sr']
    sunDown = today['ss']
    vis = today['vis']
    pop = today['pop']

    now = data['now']
    temperature = now['tmp']
    bodytemperature = now['fl']


    message = CITY_NAME + '\n日期:'+ Date_String +  '\n当前温度:'+ temperature +'°C'+'\n体感温度:'+bodytemperature+ '°C' +'\n日间天气:'+weatherInfo+'\n夜间天气:'+weatherInfoNight+'\n最高气温:'+temperatureMax+'°C' +'\n最低气温:'+temperatureMin+'°C' +'\n风向:'+wind_dir+'\n风力:'+wind_sc+'\n日出时间:'+sunRaise+'\n日落时间:'+sunDown+'\n能见度:'+vis+'\n降雨概率:'+pop+'%'

    return message




def sendMessge(username):
    my_friend = bot.friends().search(username, )[0]
    my_friend.send(getWeather(nameMap[username]))


def execute_task():
    print('........')
    sendMessge(XIAOKEZI)
    # sendMessge(CHING)
    # sendMessge(KONG)
    # sendMessge(CHI)
    # sendMessge(DENG)
    time.sleep(60)


def dotask(h = 0 , m = 0 , s = 0):
    while True:

        # 判断是否达到设定时间，例如0:00

        while True:

            now = datetime.datetime.now()

            # 到达设定时间，结束内循环

            if now.hour == h and now.minute == m and now.second == s:
                break
            time.sleep(1)

        # 做正事，一天做一次

        execute_task()


if __name__ == '__main__':
    dotask(7,0,0)


