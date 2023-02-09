
def activateCard(cardName, player):
    name = str(cardName)
    if name == "Copper":
        player.IncreaseCoins(1)
        
    if name == "Silver":
        player.IncreaseCoins(2)
        
    if name == "Gold":
        player.IncreaseCoins(3)
        
    if name == "Smithy":
        player.DrawCards(3)
        
    if name == "Village":
        player.IncreaseActions(2)
        player.DrawCards(1)
        
    if name == "Market":
        player.DrawCards(1)
        player.IncreaseActions(1)
        player.IncreaseBuys(1)
        player.IncreaseCoins(1)
        
    if name == "Moat":
        player.DrawCards(2)
    
    return True

def isCoinCard(cardName):
    return cardName in ["Copper", "Silver", "Gold"]
