from flask import Flask, jsonify
from random import choice
import time

app = Flask(__name__)









@app.route("/Test", methods=['GET'])
def getInventory():
    return prepareResponse("true")

def prepareResponse(value):
    response = jsonify({'data': str(value)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')