import cloudscraper
import json
import sys

class requests_fb:
    def __init__(self,cookie):
        self.httpx = cloudscraper.create_scraper(
                browser={
                    'browser': 'chrome',
                    'platform': 'windows',
                    'mobile': False
                }
            )
        self.header_get = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "cookie": cookie,
            "referer": "https://www.facebook.com/",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not.A/Brand";v="24"',
            "sec-ch-ua-full-version-list": '"Google Chrome";v="137.0.7151.120", "Chromium";v="137.0.7151.120", "Not.A/Brand";v="24.0.0.0"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-ch-ua-platform-version": "10.0.0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1"
        }

        self.header_post = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": cookie,
            "origin": "https://www.facebook.com",
            "referer": "https://www.facebook.com/",
            "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not.A/Brand";v="24"',
            "sec-ch-ua-full-version-list": '"Google Chrome";v="137.0.7151.120", "Chromium";v="137.0.7151.120", "Not.A/Brand";v="24.0.0.0"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-ch-ua-platform-version": "10.0.0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "pragma": "no-cache"
        }


    def auto_like(self,cookie_fb,id,type,proxies):
        
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
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}',headers = self.header_get,proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',headers=self.header_get,proxies=proxies).text
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

        response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = self.header_post,data=data,proxies=proxies)

    def auto_comment(self,cookie_fb,id,Text, proxies):

        id_fb = cookie_fb.split('c_user=')[1].split(';')[0]
        id_ads = id
            

        fake_link = self.httpx.get(url = f'https://www.facebook.com/{id_ads}', headers=self.header_get,proxies=proxies).url

        form = self.httpx.get(url=f'{fake_link}',headers=self.header_get,proxies=proxies).text
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
        


        response = self.httpx.post(url="https://www.facebook.com/api/graphql/",headers = self.header_post,data=data,proxies=proxies)
    

    
