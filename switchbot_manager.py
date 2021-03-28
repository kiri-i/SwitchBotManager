#!usr/bin/env python3

import os
from dotenv import load_dotenv
import requests
import pprint
import pathlib

# .envを読み込んで環境変数を設定
load_dotenv()
# 環境変数からAPIキーを取得
API_KEY = os.getenv("SWITCHBOT_APIKEY")

# 共通
base_url = "https://api.switch-bot.com"
headers = {
    "Authorization" : API_KEY
}


def get_devices():
    api_url = "/v1.0/devices"
    url = base_url + api_url
    r = requests.get(url, headers=headers)
    res_dic = r.json()
    return res_dic

def main():
    res_dic = get_devices()
    pprint.pprint(res_dic, indent=2)
    print("完了")

if __name__ == "__main__":
    main()