from CardEffectsLogic import isAttackCard
from flask import Flask, jsonify, render_template, send_file
from Board import Board
import subprocess

app = Flask(__name__, template_folder='/home/pi/Dominion/')

@app.route("/GitPull", methods=['GET'])
def PerformGitPull():
    shellscript = subprocess.Popen(["/home/pi/Dominion/gitPull.sh"], stdin=subprocess.PIPE)
    shellscript.stdin.close()
    return prepareResponse("done")

@app.route("/", methods=['GET'])
def getWebpage():
    return render_template('Dominion.html')

@app.route("/Image/<cardName>", methods=['GET'])
def getImage(cardName = ""):
    return send_file('Images/'+cardName+'.jpg', mimetype='image/jpg')

@app.route("/Test", methods=['GET'])
def getInventory():
    return prepareResponse("true")

@app.route('/AddPlayer/<name>', methods=['POST'])
def AddPlayer(name = ""):
    resp = prepareResponse(board.addPlayer(name))
    return resp

@app.route("/GetPlayer/<name>", methods=['GET'])
def GetPlayer(name = ""):
    player = board.getPlayer(name)
    if player is not None:
        return prepareResponse(player.out())
    return prepareResponse(player)

@app.route("/UseCard/<playerName>/<cardName>", methods=['POST'])
def UseCard(cardName = "", playerName = ""):
    player = board.getPlayer(playerName)
    player.tryUseCardAsAction(cardName)
    board.performPotentialAttackOnOthers(player, cardName)
    board.performPotentialEffectOnOthers(player,cardName)
    return prepareResponse(player.out())

@app.route("/StartGame", methods=["POST"])
def StartGame():
    return prepareResponse(board.startGame())
    
@app.route("/EndTurn/<playerName>", methods=["POST"])
def EndTurn(playerName = ""):
    return prepareResponse(board.passTurn(playerName))

@app.route("/ResetGame", methods=["POST"])
def ResetGame():
    board = Board()
    return prepareResponse("true")

def prepareResponse(value):
    response = jsonify({'data': str(value)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    board = Board()
    app.run(debug=True, port=80, host='0.0.0.0')
