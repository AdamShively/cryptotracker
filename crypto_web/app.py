import requests
from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)
app.secret_key = "sccxcbasc%av23^avsdv!!wqq##asd44vcb"

cryto_name = ""     #Current cryto coin selected

#Get key from file
try:
    with open('putkeyhere.txt') as f:
        key = f.read()
except Exception as e:
    print(e)

headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': key
}

parameters = {
'start':'1',
'limit':'25',
'convert':'USD'
}

try:
    json = requests.get(url, params=parameters, headers=headers).json()
except Exception as e:
    print(e, "Did you forget to put the key in putkeyhere.txt?")

json = requests.get(url, params=parameters, headers=headers).json()

def get_display():
    """
    get info from api that will be displayed
    :return: dict object storing crypto data
    """
    
    data = {}
    coins = json['data']
    
    for coin in coins:
        if coin and coin['name'].lower() == cryto_name:

            name = coin['name']
            sym = coin['symbol']
            price = coin['quote']['USD']['price']
            price = "{:.2f}".format(price)
            percent = coin['quote']['USD']['percent_change_24h']
            direction = '↑' if percent >= 0 else '↓'
            percent = percent if percent > 0 else percent*-1
            percent = "{:.2f}".format(percent)

            data['name'] = (f'{name}({sym})')
            data['price'] = (f'${price}')
            data['per'] = (f'{direction}{percent}%')
            data['day'] = get_date_time()

            return data

    return {'name':'Unavailable',
            'price':'Unavailable', 
            'per':'Unavailable', 
            'day':'Unavailable'}

def get_date_time():
    """
    gets current day/time and reformats if neccessary
    :return: str containing date/time
    """
    now = dt.datetime.now()
    #date and time format: mm/dd/YYYY H:M:S
    format = "%m/%d/%Y %H:%M:%S"
    date_time = now.strftime(format)
    hour = int(date_time[11:13])

    #Reformat to traditional time format 
    #instead of military time
    if hour > 12:
        hour = hour - 12
        temp = list(date_time)
        temp[11] = str(hour)[0:1]
        temp[12] = str(hour)[1:2]

        return "".join(temp)

    return date_time

@app.route("/")
@app.route("/bitcoin")
def bitcoin():
    """
    displays bitcoin (homepage) data
    :return: None
    """
    global cryto_name
    cryto_name = "bitcoin"
    return render_template("index.html", imgfile='images/btc.png')

@app.route("/ethereum")
def ethereum():
    """
    displays ethereum data
    :return: None
    """
    global cryto_name
    cryto_name = "ethereum"
    return render_template("index.html", imgfile='images/eth.png')

@app.route("/tether")
def tether():
    """
    displays tether data
    :return: None
    """
    global cryto_name
    cryto_name = "tether"
    return render_template("index.html", imgfile='images/usdt.png')

@app.route("/bnb")
def bnb():
    """
    displays bnb data
    :return: None
    """
    global cryto_name
    cryto_name = "bnb"
    return render_template("index.html", imgfile='images/bnb.png')

@app.route("/cardano")
def cardano():
    """
    displays cardano data
    :return: None
    """
    global cryto_name
    cryto_name = "cardano"
    return render_template("index.html", imgfile='images/ada.png')

@app.route("/xrp")
def xrp():
    """
    displays xrp data
    :return: None
    """
    global cryto_name
    cryto_name = "xrp"
    return render_template("index.html", imgfile='images/xrp.png')

@app.route("/solana")
def solana():
    """
    displays solana data
    :return: None
    """
    global cryto_name
    cryto_name = "solana"
    return render_template("index.html", imgfile='images/sol.png')

@app.route("/dogecoin")
def dogecoin():
    """
    displays dogecoin data
    :return: None
    """
    global cryto_name
    cryto_name = "dogecoin"
    return render_template("index.html", imgfile='images/doge.png')

@app.route("/tron")
def tron():
    """
    displays tron data
    :return: None
    """
    global cryto_name
    cryto_name = "tron"
    return render_template("index.html", imgfile='images/trx.png')

@app.route("/litecoin")
def litecoin():
    """
    displays litecoin data
    :return: None
    """
    global cryto_name
    cryto_name = "litecoin"
    return render_template("index.html", imgfile='images/ltc.png')

@app.route("/get_data", methods = ["GET"])
def get_data():
    """
    :return: dict object storing crypto data
    """
    data = get_display()
    return {"data": data}

if __name__ == "__main__":
    
    app.run()
