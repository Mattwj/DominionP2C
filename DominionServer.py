from CardEffectsLogic import isAttackCard
from flask import Flask, jsonify, render_template, send_file
from Board import Board
import subprocess

#Test Commit

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

@app.route("/BuyPhase/<playerName>", methods=["POST"])
def MoveToBuyPhase(playerName = ""):
    player = board.getPlayer(playerName)
    player.calculateCoins()
    return prepareResponse(player.out())

@app.route("/GetCards", methods=["GET"])
def GetCards():
    return prepareResponse(board.getCards())

@app.route("/GetCardsWithCounts", methods=["GET"])
def GetCardsWithCounts():
    return prepareResponse(board.getCardsWithCounts())

@app.route("/StartGame", methods=["POST"])
def StartGame():
    return prepareResponse(board.startGame())
    
@app.route("/EndTurn/<playerName>", methods=["POST"])
def EndTurn(playerName = ""):
    player = board.getPlayer(playerName)
    return prepareResponse(board.passTurn(player))

@app.route("/ResetGame", methods=["POST"])
def ResetGame():
    board.fullReset()
    return prepareResponse("true")

@app.route("/IsTurn/<playerName>", methods=["GET"])
def IsTurn(playerName = ""):
    return prepareResponse(board.currPlayer == playerName)

@app.route("/BuyCard/<playerName>/<cardName>", methods=["POST"])
def BuyCard(playerName = "", cardName = ""):
    player = board.getPlayer(playerName)
    player.tryBuyCard(cardName)
    return prepareResponse(player.out())

@app.route("/Endpoints", methods=["GET"])
def EndpointDocumentation():
    endpointsInfo = {}
    endpointsInfo.append("/GitPull : GET - Performs a Git Pull and is used to update the server - No parameters")
    endpointsInfo.append("/Endpoints : GET - Returns information on all endpoints and how to use them - No parameters")
    endpointsInfo.append("/ : GET - Gets the webpage - No parameters")
    endpointsInfo.append("/Image/<CardName> : GET - Gets an image from the Image folder - the CardName parameter is the name of the card")
    endpointsInfo.append("/Test : GET - Performs a Test to see if the server is up - No parameters")
    endpointsInfo.append("/AddPlayer/<PlayerName> : POST - Adds a player to the game - the PlayerName parameter is the name of the player")
    endpointsInfo.append("/GetPlayer/<PlayerName> : GET - Get the player with the given name - the PlayerName parameter is the name of the player")
    endpointsInfo.append("/UseCard/<PlayerName>/<CardName> : POST - Attempts to have the given player used the passed card - the PlayerName parameter is the name of the player, the CardName is the name of the card that is being attempted to be used")
    endpointsInfo.append("/BuyPhase/<PlayerName> : POST - Triggers the buy phase for a player - the PlayerName is the name of the player")
    endpointsInfo.append("/GetCards : GET - Gets the list of the 10 cards being used in the current game - No parameters")
    endpointsInfo.append("/GetCardsWithCounts : GET - Gets the list of the 10 cards being used in the current game with another list with their respective counts - No parameters")
    endpointsInfo.append("/StartGame : GET - Starts the game - No parameters")
    endpointsInfo.append("/EndTurn/<PlayerName> : POST - Triggers the end of turn for the passed player and returns the next player in turn (logic needs changing eventually) - the PlayerName parameter is the name of the player")
    endpointsInfo.append("/ResetGame : POST - Resets the game removing all data - TESTING ONLY - No parameters")
    endpointsInfo.append("/IsTurn/<PlayerName> : GET - Returns turn if its currently the passed players turn - the PlayerName parameter is the name of the player")
    return prepareResponse(endpointsInfo)
    

def prepareResponse(value):
    response = jsonify({'data': str(value)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    board = Board()
    app.run(debug=True, port=80, host='0.0.0.0')
