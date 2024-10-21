from flask import Flask, render_template, request 
from db import engine, YuraPrice, SingaPrice
from sqlalchemy.orm import Session

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
        tableSingaData=tableSingaData 
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')