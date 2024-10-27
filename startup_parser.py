from avito_parser import make_request
from math import ceil
from sqlalchemy.orm import Session
from db import engine, YuraPrice, SingaPrice
from time_util import get_now
import time
import random

last_update = { "yura": get_now(), "singa": get_now()}
yura_id = '0793f8fa8904c8f8c986a1f1d341baba'
singa_id = '0306b2a6e58801c9b0e6684a1435a505'

def update_date(seller, is_error = False):
    global last_update
    if not is_error:
        last_update[seller] = get_now()
    else: print('ошибка')

def get_date():
    global last_update
    return last_update

def check_uni(seller_id):
    if (seller_id == yura_id): # ПЕРЕДЕЛАТЬ А ТО ЭТО КРИНЖ
        TempTable = YuraPrice
        seller = "yura"
    elif (seller_id == singa_id):
        TempTable = SingaPrice
        seller = "singa"
        
    with Session(autoflush=False, bind=engine) as db:    
        page = 1
        total = 0
        did_delete = False
        while True:
            r = make_request(seller_id, page)
            
            if ('error' in r):
                break
            
            if (not did_delete): 
                db.query(TempTable).delete()
                db.commit()
                update_date(seller=seller)
                did_delete = True
            
            if (page == 1) : total = ceil(r['totalCount'] / 12)
            
            for i in range(len(r['catalog']['items'])):
                db.add(TempTable(name = r['catalog']['items'][i]['title'], price = r['catalog']['items'][i]['priceDetailed']['string'], picture = r['catalog']['items'][i]['images'][0]['catalog'], link = f'https://www.avito.ru{r["catalog"]["items"][i]["urlPath"]}'))
                
            page += 1
            if (page == (total+1)) : 
                db.commit()
                break
            
            time.sleep(random.random() + 0.5)

def check_Yura():
    check_uni(yura_id)

def check_Singa():
    check_uni(singa_id)

check_Yura()
time.sleep(random.random() + 0.5)
check_Singa()

# print(certifi.core.where())
