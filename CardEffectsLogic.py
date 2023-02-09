from Player import Player

def activateCard(cardName, player):
    match str(cardName) :
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