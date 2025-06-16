import requests

class requests_ttc:
    def __init__(self):

        self.httpx = requests.Session()

    def get_accout(self,access_token,url = "https://tuongtaccheo.com/logintoken.php"):
        data = {
            "access_token": access_token,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = self.httpx.post(url,data=data, headers=headers)

        if response.json()['status'] == "success":
            cookie = response.headers['Set-Cookie']
            main_cookie = cookie.split(';')[0]
            return response.json()['data'],main_cookie
        else:
            main_cookie = ""
            return "Nhập sai access_token hoặc tài khoản không tồn tại",main_cookie
    
    def get_jobs_like_vip(self,cookie,url = "https://tuongtaccheo.com/kiemtien/likepostvipcheo/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_like_re(self,cookie,url = "https://tuongtaccheo.com/kiemtien/likepostvipre/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_camxu_vip(self,cookie,url = "https://tuongtaccheo.com/kiemtien/camxucvipcheo/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_camxu_re(self,cookie,url = "https://tuongtaccheo.com/kiemtien/camxucvipre/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()
    def get_jobs_comment(self,cookie,url = "https://tuongtaccheo.com/kiemtien/cmtcheo/getpost.php"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Cookie": cookie,
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }
        response = self.httpx.get(url, headers=headers)
        return response.json()