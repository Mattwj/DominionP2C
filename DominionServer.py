from flask import Flask, jsonify, render_template, send_file
from random import choice
import time

app = Flask(__name__, template_folder='/home/pi/Dominion/')

@app.route("/", methods=['GET'])
def getWebpage():
    return render_template('Dominion.html')

@app.route("/Image/<cardName>", methods=['GET'])
def getImage(cardName = ""):

    return send_file('Images/'+cardName+'.jpg', mimetype='image/jpg')

@app.route("/EstateImage", methods=['GET'])
def getEstateImage():
    return send_file('Images/Estate.jpg', mimetype='image/jpg')

@app.route("/Test", methods=['GET'])
def getInventory():
    return prepareResponse("true")

def prepareResponse(value):
    response = jsonify({'data': str(value)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')