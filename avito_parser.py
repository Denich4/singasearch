import ssl

import cloudscraper
from requests.adapters import HTTPAdapter, PoolManager
from urllib3.util import ssl_
import requests
import certifi

import json

CIPHERS = "TLS_AES_256_GCM_SHA384:TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"

class TlsAdapter(HTTPAdapter):
    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)
        
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)

scraper = cloudscraper.create_scraper(delay=10, browser={'custom': 'ScraperBot/1.0'})
scraper.mount("https://", TlsAdapter(ssl.OP_NO_SSLv3))

url = 'https://www.avito.ru/web/1/profile/items'

headers = {
    'authority': 'www.avito.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'srv_id=7etrx3vhcoPwcDc_.cNW_6bI6EgfXIPIuCWD28oDWVtuib7ijdgKWxEuAf_5g069aq8YL6TyipmThThU=.9Hb_zxG5MZ19t7L2l3cbF26f21vdST0bklsEBbknzrE=.web; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; u=2xzrsp7y.1hwbhq.13hi7jk6ndc00; buyer_laas_location=621540; luri=all; buyer_location_id=621540; _ym_uid=1690297302431837220; _ym_d=1690297302; _gcl_au=1.1.1913198390.1690297302; _ym_isad=2; _ga=GA1.1.1627394497.1690297304; tmr_lvid=e1ef0b6537bfb5d336a44533e8c87088; tmr_lvidTS=1690297304327; uxs_uid=2b895610-2afc-11ee-94bb-635b59dcaff4; adrdel=1; adrcid=ANY1i3OeCiAGj19eApA1lXA; f=5.32e32548b6f3e9784b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8b175a5db148b56e9bcc8809df8ce07f640e3fb81381f359178ba5f931b08c66a59b49948619279110df103df0c26013a2ebf3cb6fd35a0ac91e52da22a560f550df103df0c26013a7b0d53c7afc06d0bba0ac8037e2b74f92da10fb74cac1eab71e7cb57bbcb8e0f71e7cb57bbcb8e0f71e7cb57bbcb8e0f0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686adbf5c86bc0685a4ff42a08f76f4956e8502c730c0109b9fbb88742379a681fe552709b26a275ecd440e28148569569b79099f064490bd264aaffcb3ba7c814b452ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd748ec69374753ddd6b03de19da9ed218fe23de19da9ed218fe2ddb881eef125a8703b2a42e40573ac3c8edd6a0f40cbfd87da3d420d6cca468c; ft="lXh+9XB6Da+f+A03Jx6nMRILS6YV95XEpyuIlTPmZ1P6+eMfHKfBUtIwTF2CVRSTgiS9qEq4zI39C2Yr8L1oB4DwFXnxjTHs1RGOlLcQuA7c0bNfgOYNvgGHTc29VBWh3yWlLb1DikbE22G4WmDQ1mNDxQCmB698vyunxx4tZIT+Z5dxe8FDsGGdDXxtS/wt"; v=1690300709; _ym_visorc=b; sx=H4sIAAAAAAAC%2FwTAUQqDMAwG4Lv8z3uos%2F5ZepwmlYEUxpwBK9593wWSNBeuSl2YqU1qm9VlSWbiinIhUHCuybLnbfz2TxpHrXG899G%2F0ePcuuOBhjJR0%2FwSmZ73%2FQ8AAP%2F%2Frk2RJFsAAAA%3D; dfp_group=65; abp=0; _ga_M29JC28873=GS1.1.1690300859.2.1.1690301314.59.0.0; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyVGh1JTJDJTIwMjUlMjBKdWwlMjAyMDI0JTIwMTYlM0EwOCUzQTM4JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnVmcCU1QyUyMiUzQSU1QyUyMjkxMjI0YWQxNGQzOTY0MmQ3ODc4NWVkMmUwNmE3ZmJkJTVDJTIyJTJDJTVDJTIyYnJvd3NlclZlcnNpb24lNUMlMjIlM0ElNUMlMjIxMTQuMCU1QyUyMiU3RCUyMiU3RA==; tmr_detect=0%7C1690301321734',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def make_request(seller_id, page):
    
    params = {
    'categoryId': 84,
    'locationId': 621540,
    'cd': 0,
    'p' : page,
    'sellerId': seller_id,
    'limit': 12
    }

    r = requests.get("https://www.avito.ru/web/1/profile/items", params=params, headers=headers, verify=False)

    if (r.status_code < 400):
        return r.json()
    else: 
        return json.loads('{"error": 403}')

# json_object = json.dumps(r.json, indent=4)

# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(r.json())

# print(json.loads(r.text))