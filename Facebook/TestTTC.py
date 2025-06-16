import cloudscraper
import codecs

data = {
	"access_token": "64c6a72ced2aac7fe4003e9ce2179051"
}

requests_ttc = cloudscraper.create_scraper()

def get_jods_reviews(url = "https://tuongtaccheo.com/kiemtien/danhgiapage/getpost.php"):

        reponse = requests_ttc.get(url=url,headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Priority": "u=0, i",
    "Referer": "https://tuongtaccheo.com/kiemtien/danhgiapage/",
    "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "Sec-CH-UA-Mobile": "?1",
    "cookie":"PHPSESSID=l70dgkq54pt7tkhuu9nq6haks0",
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

a = get_jods_reviews()
print (a)
get_nd = a[0]['nd']
nd = get_nd.split('"')[1].split('"')[0]

text = codecs.decode(nd, 'unicode_escape')
print(a[0]["UID"] + "\n" + text)

# def get_jods_share(url = "https://tuongtaccheo.com/kiemtien/sharecheo/getpost.php"):

#         reponse = requests_ttc.get(url=url,headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Priority": "u=0, i",
#     "Referer": "https://tuongtaccheo.com/kiemtien/danhgiapage/",
#     "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
#     "Sec-CH-UA-Mobile": "?1",
#     "cookie":"_fbp=fb.1.1745041866621.902958007514664312; _gid=GA1.2.1055872792.1748598991; PHPSESSID=fed4jg8bv2qn3m6aeo9f7dgcl0; _gat_gtag_UA_88794877_6=1; _ga_6RNPVXD039=GS2.1.s1749013203$o97$g1$t1749013745$j59$l0$h0; _ga=GA1.1.207914220.1745041866",
#     "Sec-CH-UA-Platform": "\"Android\"",
#     'Connection': 'keep-alive',
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
#     "X-Requested-With":"XMLHttpRequest",
# })
         
#         return reponse.json()

# def get_jods_share_nd(url = "https://tuongtaccheo.com/kiemtien/danhgiapage/getpost.php"):

#         reponse = requests_ttc.get(url=url,headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Priority": "u=0, i",
#     "Referer": "https://tuongtaccheo.com/kiemtien/danhgiapage/",
#     "Sec-CH-UA": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
#     "Sec-CH-UA-Mobile": "?1",
#     "cookie":"_fbp=fb.1.1745041866621.902958007514664312; _gid=GA1.2.1055872792.1748598991; PHPSESSID=3dd7tmbgftupi2qvnli90546r2; _gat_gtag_UA_88794877_6=1; _ga_6RNPVXD039=GS2.1.s1748841571$o92$g1$t1748842353$j43$l0$h0; _ga=GA1.2.207914220.1745041866",
#     "Sec-CH-UA-Platform": "\"Android\"",
#     'Connection': 'keep-alive',
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "same-origin",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
#     "X-Requested-With":"XMLHttpRequest",
# })
         
#         return reponse.json()

# print(get_jods_share())