from Player import Player

def activateCard(cardName, player):
    match str(cardName) :
        case "Copper":
            player.IncreaseCoins(1)
        case "Silver":
            player.IncreaseCoins(2)
        case "Gold":
            player.IncreaseCoins(3)
        case "Smithy":
            player.DrawCards(3)
        case "Village":
            player.IncreaseActions(2)
            player.DrawCards(1)
        case "Market":
            player.DrawCards(1)
            player.IncreaseActions(1)
            player.IncreaseBuys(1)
            player.IncreaseCoins(1)
        case "Moat":
            player.DrawCards(2)

def isCoinCard(cardName):
    return cardName in ["Copper", "Silver", "Gold"]