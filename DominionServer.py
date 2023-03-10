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
    player.MoveToBuy()
    return prepareResponse(player.out())

@app.route("/BuyCard/<playerName>/<cardName>", methods=["POST"])
def BuyCard(playerName = "", cardName=""):
    player = board.getPlayer(playerName)
    return prepareResponse(board.tryToBuyCard(player, cardName))

@app.route("/GetCards", methods=["GET"])
def GetCards():
    return prepareResponse(board.getCards())

@app.route("/GetCardsWithCounts", methods=["GET"])
def GetCardsWithCounts():
    return prepareResponse(board.getAllCardsWithCounts())

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

@app.route("/IsGameOver", methods=["GET"])
def IsGameOver() :
    isOver, result = board.isGameOver()
    if isOver == True:
        return prepareResponse(result)
    return  prepareResponse("false")

@app.route("/IsTurn/<playerName>", methods=["GET"])
def IsTurn(playerName = ""):
    return prepareResponse(board.currPlayer == playerName)

@app.route("/Endpoints", methods=["GET"])
def EndpointDocumentation():
    endpointsInfo = ""
    endpointsInfo = endpointsInfo + "/GitPull : GET - Performs a Git Pull and is used to update the server - No parameters \n"
    endpointsInfo = endpointsInfo + "/Endpoints : GET - Returns information on all endpoints and how to use them - No parameters \n"
    endpointsInfo = endpointsInfo + "/ : GET - Gets the webpage - No parameters \n"
    endpointsInfo = endpointsInfo + "/Image/<CardName> : GET - Gets an image from the Image folder - the CardName parameter is the name of the card \n"
    endpointsInfo = endpointsInfo + "/Test : GET - Performs a Test to see if the server is up - No parameters \n"
    endpointsInfo = endpointsInfo + "/AddPlayer/<PlayerName> : POST - Adds a player to the game - the PlayerName parameter is the name of the player \n"
    endpointsInfo = endpointsInfo + "/GetPlayer/<PlayerName> : GET - Get the player with the given name - the PlayerName parameter is the name of the player \n"
    endpointsInfo = endpointsInfo + "/UseCard/<PlayerName>/<CardName> : POST - Attempts to have the given player used the passed card - the PlayerName parameter is the name of the player, the CardName is the name of the card that is being attempted to be used \n"
    endpointsInfo = endpointsInfo + "/BuyCard/<PlayerName>/<CardName> : POST - Attempts to have the given player buy the passed card - the PlayerName parameter is the name of the player, the CardName is the name of the card that is being attempted to be bought \n"
    endpointsInfo = endpointsInfo + "/BuyPhase/<PlayerName> : POST - Triggers the buy phase for a player - the PlayerName is the name of the player \n"
    endpointsInfo = endpointsInfo + "/GetCards : GET - Gets the list of the 10 cards being used in the current game - No parameters \n"
    endpointsInfo = endpointsInfo + "/GetCardsWithCounts : GET - Gets the list of all purchasable cards being used in the current game with another list with their respective counts - No parameters \n"
    endpointsInfo = endpointsInfo + "/StartGame : GET - Starts the game - No parameters \n"
    endpointsInfo = endpointsInfo + "/EndTurn/<PlayerName> : POST - Triggers the end of turn for the passed player and returns the next player in turn (logic needs changing eventually) - the PlayerName parameter is the name of the player \n"
    endpointsInfo = endpointsInfo + "/ResetGame : POST - Resets the game removing all data - TESTING ONLY - No parameters \n"
    endpointsInfo = endpointsInfo + "/IsTurn/<PlayerName> : GET - Returns true if its currently the passed players turn - the PlayerName parameter is the name of the player \n"
    endpointsInfo = endpointsInfo + "/IsGameOver : GET - Returns false if game is not over otherwise returns a dictionary with player names and final scores - No parameters \n"
    return prepareResponse(endpointsInfo)
    

def prepareResponse(value):
    response = jsonify({'data': str(value)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    board = Board()
    app.run(debug=True, port=80, host='0.0.0.0')
