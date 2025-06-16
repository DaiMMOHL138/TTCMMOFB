import requests
import cloudscraper
import time
import sys
import json
from bs4 import BeautifulSoup
import os
from random import randint


requests_ttc = cloudscraper.create_scraper()
requests_facebook = requests.Session()

error_comment = 0
error_followandlike = 0
error_rewies = 0


#color
red = '\033[38;2;255;86;48m'
mauvien = '\033[38;2;130;255;209m'
green = '\033[38;2;0;255;0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

title = red + r""" _____  _____  ___ 
/__   \/__   \/ __\
  / /\/  / /\/ /   
 / /    / / / /___ 
 \/     \/  \____/ """
tacgia = f"""{mauvien}=========================
  {red}BY: {green}Groud TTC (AUTO)
  V:1.2 Windows & Termux
{mauvien}========================="""
def title_tool():
    clear_screen()
    print(title)
    print(tacgia)
def delay(main):
    for n in range(main,-1,-1):
        print(f"Vui lòng chờ {n}s     ",end = "\r")
        time.sleep(1)

title_tool()
# Nhập token từ người dùng
accset_token_ttc = input("Accset token(ttc)🐱‍💻:")
proxy = input("proxy (ip:port:user:pass)🌍: ")

proxies = {}

if proxy:
    try:
        ip, port, user, pwd = proxy.split(":")
        proxy_url = f"http://{user}:{pwd}@{ip}:{port}"
        print("Proxy URL:", proxy_url)
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
    except ValueError:
        print("❌ Sai định dạng proxy. Định dạng đúng: ip:port:user:pass")
        sys.exit()

#tạo check_point
check_point = []
name_check_point = []

data = {
    "access_token": f'{accset_token_ttc}'
}

# Header của yêu cầu
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/caidat/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
}
def auto_follow_page(cookie_fb,id):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
    id_ads = id
        

    fake_link = requests_facebook.get(url = f'https://www.facebook.com/{id_ads}',headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    },proxies=proxies).url

    form = requests_facebook.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
    try:
        fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
        jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
        lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
    except KeyboardInterrupt:
                print("exit")
                
                sys.exit()
    except:
        return

    data = {
        "av": f"{id_fb}",
        "__user": f"{id_fb}",
        "fb_dtsg": f"{fb_dtsg}",
        "jazoest": f"{jazoest}",
        "lsd": f"{lsd}",
        "doc_id": "24034012419524524",  # Mã doc dùng cho CometUFIFeedbackReactMutation
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "CometUserFollowMutation",
        '__dyn': '',
        "variables": json.dumps({
            "input": {
                "is_tracking_encrypted": True,
                "subscribe_location":"PROFILE",
                "subscribee_id":f"{id_ads}",
                "tracking": None,
                "actor_id": f"{id_fb}",
                "client_mutation_id": "2",
            },
            "scale":1,
        }),
        "server_timestamps": True
    }


    response = requests_facebook.post(url="https://www.facebook.com/api/graphql/",headers = {
        'accept':'*/*',
        "Accept-Encoding": "gzip",
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'referer':f'{fake_link}',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'X-Fb-Friendly-Name':'useCometUFICreateCommentMutation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'X-Asbd-Id':'359341',
        "X-Fb-Lsd":f"{lsd}",
    },data=data,proxies=proxies)

def auto_like_page(cookie_fb,id):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
    id_ads = id
        

    fake_link = requests_facebook.get(url = f'https://www.facebook.com/{id_ads}',headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    },proxies=proxies).url

    form = requests_facebook.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
    try:
        fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
        jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
        lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
        feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
    except KeyboardInterrupt:
                print("exit")
                
                sys.exit()
    except:
        return

    data = {
        "av": f"{id_fb}",
        "__user": f"{id_fb}",
        "fb_dtsg": f"{fb_dtsg}",
        "jazoest": f"{jazoest}",
        "lsd": f"{lsd}",
        "doc_id": "24452064861060493",  # Mã doc dùng cho CometUFIFeedbackReactMutation
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "CometProfilePlusLikeMutation",
        '__dyn': '',
        "variables": json.dumps({
            "input": {
                "is_tracking_encrypted":False,
                "page_id":f"{id_ads}",
                "source":None,
                "tracking": None,
                "actor_id": f"{id_fb}",
                "client_mutation_id": "2",
            },
            "scale":1,
        }),
        "server_timestamps": True
    }


    response = requests_facebook.post(url="https://www.facebook.com/api/graphql/",headers = {
        'accept':'*/*',
        "Accept-Encoding": "gzip",
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'referer':f'{fake_link}',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'X-Fb-Friendly-Name':'useCometUFICreateCommentMutation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'X-Asbd-Id':'359341',
        "X-Fb-Lsd":f"{lsd}",
    },data=data,proxies=proxies)


def auto_like(cookie_fb,id,type):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
    id_ads = id
    type_id = "1635855486666999"
    if (type == "LOVE"):
        type_id = "1678524932434102"
    elif (type == "CARE"):
        type_id = "613557422527858"
    elif (type == "HAHA"):
        type_id = "115940658764963"
    elif (type == "WOW"):
        type_id = "478547315650144"
    elif (type == "SAD"):
        type_id = "908563459236466"
    elif (type == "ANGRY"):
        type_id = "444813342392137"
        

    fake_link = requests_facebook.get(url = f'https://www.facebook.com/{id_ads}',headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    },proxies=proxies).url

    form = requests_facebook.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
    try:
        fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
        jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
        lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
        feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
    except KeyboardInterrupt:
                print("exit")
                
                sys.exit()
    except:
        return

    data = {
        "av": f"{id_fb}",
        "__user": f"{id_fb}",
        "fb_dtsg": f"{fb_dtsg}",
        "jazoest": f"{jazoest}",
        "lsd": f"{lsd}",
        "doc_id": "29333620026283566",  # Mã doc dùng cho CometUFIFeedbackReactMutation
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "CometUFIFeedbackReactMutation",
        '__dyn': '',
        "variables": json.dumps({
            "input": {
                "feedback_id": f"{feelback}",
                "feedback_reaction_id": f"{type_id}",  # reaction type (VD: Like)
                "feedback_source": "TAHOE",
                "is_tracking_encrypted": True,
                "tracking": [],
                "actor_id": f"{id_fb}",
                "client_mutation_id": "1"
            },
            "useDefaultActor": False,
            "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False
        }),
        "server_timestamps": True
    }


    response = requests_facebook.post(url="https://www.facebook.com/api/graphql/",headers = {
        'accept':'*/*',
        "Accept-Encoding": "gzip",
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'referer':f'{fake_link}',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'x-fb-friendly-name':'CometUFIFeedbackReactMutation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'X-Asbd-Id':'359341',
        "X-Fb-Lsd":f"{lsd}",
    },data=data,proxies=proxies)

def auto_reviews_page(cookie_fb,id,text):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
    id_ads = id
        

    fake_link = requests_facebook.get(url = f'https://www.facebook.com/{id_ads}/reviews',headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    },proxies=proxies).url

    form = requests_facebook.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
    try:
        fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
        jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
        lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
        feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
    except KeyboardInterrupt:
                print("exit")
                
                sys.exit()
    except:
        return

    data = {
        "av": f"{id_fb}",
        "__user": f"{id_fb}",
        "fb_dtsg": f"{fb_dtsg}",
        "jazoest": f"{jazoest}",
        "lsd": f"{lsd}",
        "doc_id": "29790053613943259",  # bạn nên lấy đúng doc_id từ DevTools
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "ComposerStoryCreateMutation",
        "__dyn": "",  # cần đúng giá trị nếu bắt buộc
        "variables": json.dumps({
            "input": {
                "composer_entry_point": "inline_composer",
                "composer_source_surface": "page_recommendation_tab",
                "source": "WWW",
                "audience": {
                    "privacy": {
                        "allow": [],
                        "base_state": "EVERYONE",
                        "deny": [],
                        "tag_expansion_state": "UNSPECIFIED"
                    }
                },
                "message": {
                    "ranges": [],
                    "text": f"{text}",
                },
                "with_tags_ids": [],  # fix None
                "text_format_preset_id": "0",
                "page_recommendation": {
                    "page_id": f"{id_ads}",
                    "rec_type": "POSITIVE"
                },
                "tracking": [],  # fix None
                "event_share_metadata": {
                    "surface": "newsfeed"
                },
                "actor_id": f"{id_fb}",
                "client_mutation_id": "2"
            },
            "feedLocation": "PAGE_SURFACE_RECOMMENDATIONS",
            "feedbackSource": 0,
            "isProfileReviews": True,
            "renderLocation": "timeline"
        }),
        "server_timestamps": True
    }



    response = requests_facebook.post(url="https://www.facebook.com/api/graphql/",headers = {
        'accept':'*/*',
        "Accept-Encoding": "gzip",
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'referer':f'{fake_link}',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'X-Fb-Friendly-Name':'useCometUFICreateCommentMutation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'X-Asbd-Id':'359341',
        "X-Fb-Lsd":f"{lsd}",
    },data=data,proxies=proxies)

def auto_share_page(cookie_fb,id,text=""):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
    id_ads = id
        

    fake_link = requests_facebook.get(url = f'https://www.facebook.com/{id_ads}',headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    },proxies=proxies).url

    form = requests_facebook.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
    try:
        fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
        jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
        lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
        feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
    except KeyboardInterrupt:
                print("exit")
                
                sys.exit()
    except:
        return

    data = {
        "av": f"{id_fb}",
        "__user": f"{id_fb}",
        "fb_dtsg": f"{fb_dtsg}",
        "jazoest": f"{jazoest}",
        "lsd": f"{lsd}",
        "doc_id": "29790053613943259",  # cần lấy đúng doc_id trong DevTools
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "ComposerStoryCreateMutation",
        "__dyn": "",  # nếu bắt buộc, bạn cần cập nhật giá trị đúng
        "variables": json.dumps({
            "input": {
                "composer_entry_point": "share_modal",
                "composer_source_surface": "feed_story",
                "composer_type": "share",
                "source": "WWW",
                "attachments": [
                    {
                        "link": {
                            "share_scrape_data": json.dumps({
                                "share_type": 22,
                                "share_params": [id_ads]
                            })
                        }
                    }
                ],
                "reshare_original_post": "RESHARE_ORIGINAL_POST",
                "audience": {
                    "privacy": {
                        "allow": [],
                        "base_state": "EVERYONE",
                        "deny": [],
                        "tag_expansion_state": "UNSPECIFIED"
                    }
                },
                "is_tracking_encrypted": True,
                "tracking": [],
                "message": {
                    "ranges": [],
                    "text": f"{text}"
                },
                "actor_id": f"{id_fb}",
                "client_mutation_id": "1"
            },
            "feedLocation": "NEWSFEED",
            "feedbackSource": 1,
            "focusCommentID": None,
            "gridMediaWidth": None,
            "groupID": None,
            "scale": 1,
            "privacySelectorRenderLocation": "COMET_STREAM",
            "checkPhotosToReelsUpsellEligibility": False,
            "renderLocation": "homepage_stream",
            "useDefaultActor": False,
            "inviteShortLinkKey": None,
            "isFeed": True,
            "isFundraiser": False,
            "isFunFactPost": False,
            "isGroup": False,
            "isEvent": False,
            "isTimeline": False,
            "isSocialLearning": False,
            "isPageNewsFeed": False,
            "isProfileReviews": False,
            "isWorkSharedDraft": False,
            "hashtag": None,
            "canUserManageOffers": False,
            "__relay_internal__pv__CometUFIShareActionMigrationrelayprovider": True,
            "__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider": True,
            "__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider": True,
            "__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider": False,
            "__relay_internal__pv__IsWorkUserrelayprovider": False,
            "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False,
            "__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider": True,
            "__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider": 600,
            "__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider": False,
            "__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider": False,
            "__relay_internal__pv__IsMergQAPollsrelayprovider": False,
            "__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider": True,
            "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider": True,
            "__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider": False,
            "__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider": True
        }),
        "server_timestamps": True
    }



    response = requests_facebook.post(url="https://www.facebook.com/api/graphql/",headers = {
        'accept':'*/*',
        "Accept-Encoding": "gzip",
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'referer':f'{fake_link}',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'X-Fb-Friendly-Name':'ComposerStoryCreateMutation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'X-Asbd-Id':'359341',
        "X-Fb-Lsd":f"{lsd}",
    },data=data,proxies=proxies)

def auto_comment(cookie_fb,id,Text):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
    id_ads = id
        

    fake_link = requests_facebook.get(url = f'https://www.facebook.com/{id_ads}',headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    },proxies=proxies).url

    form = requests_facebook.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
    try:
        fb_dtsg = form.split('"w":0,"f":"')[1].split('",')[0]
        jazoest = form.split('comet_req=15&jazoest=')[1].split('",')[0]
        lsd     = form.split('["LSD",[],{"token":"')[1].split('"}')[0]
        feelback = form.split('"feedback":{"id":"')[1].split('"')[0]
    except KeyboardInterrupt:
                print("exit")
                
                sys.exit()
    except:
        return

    data = {
        "av": f"{id_fb}",
        "__user": f"{id_fb}",
        "fb_dtsg": f"{fb_dtsg}",
        "jazoest": f"{jazoest}",
        "lsd": f"{lsd}",
        "doc_id": "9761804193899543",  # Mã doc dùng cho CometUFIFeedbackReactMutation
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "useCometUFICreateCommentMutation",
        '__dyn': '',
        "variables": json.dumps({
            "feedLocation":"NEWSFEED","feedbackSource":1,"groupID":None,
            "input": {
                "feedback_id": f"{feelback}",
                "feedback_source": "TAHOE",
                "is_tracking_encrypted": True,
                "tracking": [],
                "actor_id": f"{id_fb}",
                "client_mutation_id": "1",
                "message":{"ranges":[],"text":f"{Text}"}
            },
            "useDefaultActor": False,
            "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider": False
        }),
        "server_timestamps": True
    }


    response = requests_facebook.post(url="https://www.facebook.com/api/graphql/",headers = {
        'accept':'*/*',
        "Accept-Encoding": "gzip",
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Cache-Control': 'no-cache',
        'Cookie': f'{cookie_fb}',
        'Dpr': '1',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'referer':f'{fake_link}',
        'Sec-CH-Prefers-Color-Scheme': 'dark',
        'Sec-CH-UA': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'Sec-CH-UA-Full-Version-List': '"Google Chrome";v="135.0.7049.96", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.96"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Model': '""',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-CH-UA-Platform-Version': '"10.0.0"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'X-Fb-Friendly-Name':'useCometUFICreateCommentMutation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'X-Asbd-Id':'359341',
        "X-Fb-Lsd":f"{lsd}",
    },data=data,proxies=proxies)


a = 1
def get_account_ttc(url="https://tuongtaccheo.com/logintoken.php"):
    global PHPSESSID, name_ttc, coin_ttc,a

    # Gửi yêu cầu POST để lấy thông tin tài khoản
    response = requests_ttc.post(url=url, data=data, headers=headers)

    if response.status_code == 200:
        # Parse JSON để lấy thông tin user và coin
        try:
            name_ttc = response.json()["data"]["user"]
            coin_ttc = response.json()["data"]["sodu"]
            # Lấy PHPSESSID từ cookie
            if a:
                PHPSESSID = response.cookies.get("PHPSESSID")
                a = 0
            return True
        except:
            print(f"Error: {response.text}")
            return False

running = get_account_ttc()

if running:
    # Cập nhật header với PHPSESSID lấy từ cookie
    headers.update({
        "Cookie": f"PHPSESSID={PHPSESSID}"
    })

    def get_account_facebook(url="https://tuongtaccheo.com/cauhinh/facebook.php"):
        # Gửi yêu cầu GET với headers chứa cookie đã cập nhật
        response = requests_ttc.get(url=url, headers=headers)
        return response.text

    # Gọi hàm lấy thông tin Facebook
    html_text = get_account_facebook()

    soup = BeautifulSoup(html_text, 'html.parser')

    # Duyệt qua tất cả các thẻ li trong danh sách nick
    items = soup.select("ul#dsnick li")

    for item in items:
        try:
            user_id = item.find('input', {'type': 'checkbox'})['value']
            name = item.find('a', {'href': f'https://www.facebook.com/{user_id}'}).text

            check_point.append(user_id)
            name_check_point.append(name)

        except Exception as e:
            pass

    
    def datnick(index,url="https://tuongtaccheo.com/cauhinh/datnick.php"):

        payload = {
            "iddat[]": check_point[index],
            "loai": "fb",
            "access_token": f'{accset_token_ttc}'
        }

        respone = requests_ttc.post(url=url,data=payload)



    def get_jods_like(url = "https://tuongtaccheo.com/kiemtien/likepostvipcheo/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/likepostvipcheo/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
         
        return reponse.json()
    def get_jods_follow_page(url = "https://tuongtaccheo.com/kiemtien/subcheo/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/subcheo/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
         
        return reponse.json()
    def get_jods_like_page(url = "https://tuongtaccheo.com/kiemtien/likepagecheo/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/subcheo/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
    def get_jods_reviews(url = "https://tuongtaccheo.com/kiemtien/danhgiapage/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/danhgiapage/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
         
        return reponse.json()
    def get_jods_camxu(url = "https://tuongtaccheo.com/kiemtien/camxucvipcheo/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/camxucvipcheo/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
         
        return reponse.json()
    
    def get_jods_comment(url = "https://tuongtaccheo.com/kiemtien/cmtcheo/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/camxucvipcheo/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
         
        return reponse.json()
    def get_jods_camxure(url = "https://tuongtaccheo.com/kiemtien/camxucvipre/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/camxucvipcheo/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
         
        return reponse.json()
    
    def get_jods_likere(url = "https://tuongtaccheo.com/kiemtien/likepostvipre/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/camxucvipcheo/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Sec-CH-UA-Platform": "\"Android\"",
    'Connection': 'keep-alive',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
})
         
        return reponse.json()
    
    def nhantien(idpost,type,re):
        global error,tong_jobs
        if type == "":
            type_jobs = "like"
            if re:
                url = "https://tuongtaccheo.com/kiemtien/likepostvipre/nhantien.php"
            else: url = "https://tuongtaccheo.com/kiemtien/likepostvipcheo/nhantien.php"
            ads = "LIKE"
            payload = {
                "id": f'{idpost}',
            }
        elif type == "cm":
            url = "https://tuongtaccheo.com/kiemtien/cmtcheo/nhantien.php"
            type_jobs = "cm"
            ads = "COMMENT"
            payload = {
                "id": f'{idpost}',
            }
        elif type == "follow":
            url = 'https://tuongtaccheo.com/kiemtien/subcheo/nhantien.php'
            type_jobs = "follow"
            ads = "FOLLOW"
            payload = {
                "id": f'{idpost}',
            }
        elif type == "likepage":
            url = "https://tuongtaccheo.com/kiemtien/likepagecheo/nhantien.php"
            type_jobs = "likepage"
            ads = "LIKEPAGE"
            payload = {
                "id": f'{idpost}',
            }
        else:
            if re:
                url = "https://tuongtaccheo.com/kiemtien/camxucvipre/nhantien.php"
            else: url = "https://tuongtaccheo.com/kiemtien/camxucvipcheo/nhantien.php"
            type_jobs = "like"
            ads = "CAMXUC"
            payload = {
                "id": f'{idpost}',
                "loaicx": type,
            }

        response = requests_ttc.post(url=url,headers={
    "Cookie": f"PHPSESSID={PHPSESSID}",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
},data=payload)
        if type_jobs == "like":
            if response.json() == {"mess": "Thành công, bạn đã được cộng 1100 xu"}:
                get_account_ttc()
                tong_jobs += 1
                print(f"{green}{tong_jobs}|{red}{name_ttc}{green}|{mauvien}{coin_ttc}{green}|+1100|{red}{ads}✔")
                return True
            elif response.json() == {"mess": "Thành công, bạn đã được cộng 600 xu"}:
                get_account_ttc()
                tong_jobs += 1
                print(f"{green}{tong_jobs}|{red}{name_ttc}{green}|{mauvien}{coin_ttc}{green}|+600|{red}{ads}✔")
                return True
            else:
                return False
        if type_jobs == "follow":
            if response.json() == {"mess": "Thành công, bạn đã được cộng 700 xu"}:
                get_account_ttc()
                error_followandlike = 0
                tong_jobs += 1
                print(f"{green}{tong_jobs}|{red}{name_ttc}{green}|{mauvien}{coin_ttc}{green}|+700|{red}{ads}✔")
                return True
            else:
                error_followandlike += 1
                return False
        
        if type_jobs == "likepage":
            if response.json() == {"mess": "Thành công, bạn đã được cộng 1300 xu"}:
                get_account_ttc()
                error_followandlike = 0
                tong_jobs += 1
                print(f"{green}{tong_jobs}|{red}{name_ttc}{green}|{mauvien}{coin_ttc}{green}|+1300|{red}{ads}✔")
                return True
            else:
                error_followandlike += 1
                return False

        if type_jobs == "cm":
            if response.json() == {"error":"Bạn chưa comment đúng nội dung"}:
                error += 1
                return False
            else:
                get_account_ttc()
                tong_jobs += 1
                print(f"{green}{tong_jobs}|{red}{name_ttc}{green}|{mauvien}{coin_ttc}{green}|+1400|{red}{ads}✔")
                error = 0
                return True

    def su_ly(cookie_fb):
        global jobs_save
        global jobs_sleep,delay_min,delay_max,time_sleep_min,time_sleep_max
        if type_job_1 == "1":
            data = get_jods_like()
            max = len(data)
        
            for n in range(0,max):
                try:
                    idpost = data[n]["idpost"]
                    link = data[n]["link"]
                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]

                    auto_like(cookie_fb,idfb,type='LIKE')
                    check_jobs_access = nhantien(idpost=idpost,type="",re=False)
                    delay(randint(delay_min,delay_max))
                    if check_jobs_access:
                        if jobs_save < (jobs_sleep - 1):
                            jobs_save += 1
                        else:
                            jobs_save = 0
                            delay(randint(time_sleep_min,time_sleep_max))
                except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
                except:
                    delay(int(data["countdown"]+3))
                    pass
            data = get_jods_camxu()
            max = len(data)
    
            for n in range(0,max):
                try:
                    idpost = data[n]["idpost"]
                    link = data[n]["link"]
                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                    type = data[n]["loaicx"]

                    auto_like(cookie_fb,idfb,type)
                    check_jobs_access = nhantien(idpost=idpost,type=type,re = False)
                    delay(randint(delay_min,delay_max))
                    if check_jobs_access:
                        if jobs_save < (jobs_sleep - 1):
                            jobs_save += 1
                        else:
                            jobs_save = 0
                            delay(randint(time_sleep_min,time_sleep_max))

                     

                except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
                except:
                    delay(int(data["countdown"]+3))
                    pass

            data = get_jods_likere()
            max = len(data)
    
            for n in range(0,max):
                try:
                    idpost = data[n]["idpost"]
                    link = data[n]["link"]
                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]

                    auto_like(cookie_fb,idfb,type='LIKE')
                    check_jobs_access = nhantien(idpost=idpost,type="",re=True)
                    delay(randint(delay_min,delay_max))
                    if check_jobs_access:
                        if jobs_save < (jobs_sleep - 1):
                            jobs_save += 1
                        else:
                            jobs_save = 0
                            delay(randint(time_sleep_min,time_sleep_max))

                     

                except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
                except:
                    delay(int(data["countdown"]+3))
                    pass
            data = get_jods_camxure()
            max = len(data)
    
            for n in range(0,max):
                try:
                    idpost = data[n]["idpost"]
                    link = data[n]["link"]
                    idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                    type = data[n]["loaicx"]

                    auto_like(cookie_fb,idfb,type)
                    check_jobs_access = nhantien(idpost=idpost,type=type,re = True)
                    delay(randint(delay_min,delay_max))
                    if check_jobs_access:
                        if jobs_save < (jobs_sleep - 1):
                            jobs_save += 1
                        else:
                            jobs_save = 0
                            delay(randint(time_sleep_min,time_sleep_max))



                except KeyboardInterrupt:
                    print("exit")
                    
                    sys.exit()
                except:
                    delay(int(data["countdown"]+3))
                    pass
        if type_job_2 == "1":
            
                data = get_jods_comment()
                max = len(data)
        
                for n in range(0,max):
                    try:
                        if error_comment >= 5:
                            pass
                        else:
                            idpost = data[n]["idpost"]
                            link = data[n]["link"]
                            idfb = link.split('https://www.facebook.com/')[1].split('"')[0]
                            type = data[n]["nd"]
                            text = type.split('"')[1].split('"')[0]

                            auto_comment(cookie_fb,idfb,text)
                            check_jobs_access = nhantien(idpost=idpost,type="cm",re=False)
                            delay(randint(delay_min,delay_max))
                            if check_jobs_access:
                                if jobs_save < (jobs_sleep - 1):
                                    jobs_save += 1
                                else:
                                    jobs_save = 0
                                    delay(randint(time_sleep_min,time_sleep_max))
                    except KeyboardInterrupt:
                        print("exit")
                        
                        sys.exit()
                    except:
                        delay(int(data["countdown"]+3))
                        pass
            


    while True:

        title_tool()
        for n,name in enumerate(name_check_point):
            print(f'{mauvien}[{red}{n}{mauvien}] {green}{name}')

        index = int(input(f"{mauvien}Nhập tài khoản muốn chạy👀:"))
        cookie_fb = input("Nhập cookie Facebook🐱‍💻:")
        clear_screen()
        title_tool()
        type_job_1 = input("Lam like vs cam xuc:(Yes[1]:No[0])👍❤:")
        type_job_2 = input("Lam comment(Yes[1]:No[0])💬:")
        delay_min = 10
        delay_max = 30
        jobs_sleep = 5
        time_sleep_min = 120
        time_sleep_max = 300

        if delay_min > delay_max:
            print("Error: Vui long nhap lai delay.")
            sys.exit()
        elif time_sleep_min > time_sleep_max:
            print("Error: vui long nhap lai delay.")
            sys.exit()


        datnick(index=index)

        tong_jobs = 0
        jobs_save = 0


        while True:
            try:
                su_ly(cookie_fb=cookie_fb)
            except KeyboardInterrupt:
                print("exit")
                
                sys.exit()

            except:
                pass
            
