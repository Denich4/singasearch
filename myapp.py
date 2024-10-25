from flask import Flask, render_template, request 
from db import engine, YuraPrice, SingaPrice
from sqlalchemy.orm import Session
from startup_parser import last_update
from flask_apscheduler import APScheduler
from startup_parser import check_Yura, check_Singa

scheduler = APScheduler()

@scheduler.task("cron", id="do_job_1", hour='10,14,19')
def job1():
    check_Singa()
    check_Yura()


app = Flask(__name__)

@app.route('/')
def home():
    
    tableYuriyData = []
    tableSingaData = []
        
    with Session(autoflush=False, bind=engine) as db:
        prices = db.query(YuraPrice).all()
        for p in prices:
            tableYuriyData.append({'name': f'{p.name}', 'price': f'{p.price}', 'picture': f'{p.picture}', 'link': f'{p.link}'})

    with Session(autoflush=False, bind=engine) as db:
        prices = db.query(SingaPrice).all()
        for p in prices:
            tableSingaData.append({'name': f'{p.name}', 'price': f'{p.price}', 'picture': f'{p.picture}', 'link': f'{p.link}'})

    return render_template(
        'index.html',
        tableYuriyData=tableYuriyData,
        tableSingaData=tableSingaData,
        date=last_update
    )

if __name__ == '__main__':
    scheduler.api_enabled = True
    scheduler.init_app(app)   
    scheduler.start()
    app.run(host='0.0.0.0')