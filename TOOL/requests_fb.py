import requests
import json
import sys

class requests_fb:
    def __init__(self):
        self.httpx = requests.Session()


    def auto_like(self,cookie_fb,id,type,proxies):
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
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}',headers={
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

        form = self.httpx.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
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


        response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = {
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

    def auto_comment(self,cookie_fb,id,Text, proxies):
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
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}',headers={
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

        form = self.httpx.get(url=f'{fake_link}',headers=headers,proxies=proxies).text
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


        response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = {
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