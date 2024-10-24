from avito_parser import make_request
from math import ceil
from sqlalchemy.orm import Session
from db import engine, YuraPrice, SingaPrice
import certifi

page = 0
yura_id = '0793f8fa8904c8f8c986a1f1d341baba'
singa_id = '0306b2a6e58801c9b0e6684a1435a505'


def check_Yura():
    with Session(autoflush=False, bind=engine) as db:    
        page = 1
        total = 0
        while True:
            r = make_request(yura_id, page)
            if (page == 1) : total = ceil(r['totalCount'] / 12)
            
            for i in range(len(r['catalog']['items'])):
                db.add(YuraPrice(name = r['catalog']['items'][i]['title'], price = r['catalog']['items'][i]['priceDetailed']['string'], picture = r['catalog']['items'][i]['images'][0]['catalog'], link = f'https://www.avito.ru{r["catalog"]["items"][i]["urlPath"]}'))
                # print(str(r['catalog']['items'][i]['title']) + ' === ' + r['catalog']['items'][i]['priceDetailed']['string'])

            page += 1
            if (page == (total+1)) : 
                db.commit()
                break


def check_Singa():
    with Session(autoflush=False, bind=engine) as db:    
        page = 1
        total = 0
        while True:
            r = make_request(singa_id, page)
            if (page == 1) : total = ceil(r['totalCount'] / 12)
            
            for i in range(len(r['catalog']['items'])):
                db.add(SingaPrice(name = r['catalog']['items'][i]['title'], price = r['catalog']['items'][i]['priceDetailed']['string'], picture = r['catalog']['items'][i]['images'][0]['catalog'], link = f'https://www.avito.ru{r["catalog"]["items"][i]["urlPath"]}'))
                # print(str(r['catalog']['items'][i]['title']) + ' === ' + r['catalog']['items'][i]['priceDetailed']['string'])

            page += 1
            if (page == (total+1)) : 
                db.commit()
                break

check_Yura()

check_Singa()

# print(certifi.core.where())