import requests
import sys
import json
proxies = {
    "http": "http://sun9420633:N5yEOCUANOQU@proxy-s1.resident-psun.io.vn:20633",
    "https": "http://sun9420633:N5yEOCUANOQU@proxy-s1.resident-psun.io.vn:20633"
}
requests_facebook= requests.Session()
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




cookie = input("Nhập cookie:")

auto_share_page(cookie,977810647878186,"Shop n\\u00e0y uy t\\u00edn, h\\u00e0ng \\u0111\\u1eb9p, x\\u1ecbn ch\\u1ea5t l\\u01b0\\u1ee3ng qu\\u00e1 nha,\\ud83d\\ude18\\ud83d\\ude18\\ud83d\\ude18\"")