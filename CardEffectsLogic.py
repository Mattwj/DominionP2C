
def activateCard(cardName, player):
    name = str(cardName)
    if name == "Copper":
        player.IncreaseCoins(1)
        return False
        
    if name == "Silver" or name=="Harem":
        player.IncreaseCoins(2)
        return False
        
    if name == "Gold":
        player.IncreaseCoins(3)
        return False
        
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
        
    if name == "Festival":
        player.IncreaseActions(2)
        player.IncreaseBuys(1)
        player.Coins(2)
        
    if name == "Laboratory":
        player.DrawCards(2)
        player.IncreaseActions(1)
        
    if name == "Merchant":
        player.DrawCards(1)
        player.IncreaseActions(1)
        player.AddBuyPhaseEffect(cardName)
        
    if name == "Witch":
        player.DrawCards(3)
        
    if name == "Council Room" :
        player.DrawCards(4)
        player.InceaseBuys(1)
    
    return True

def isAttackCard(cardName) :
    return cardName in ["Witch"]

def useBuyPhaseEffect(cardName, player):
    name = str(cardName)
    if name == "Merchant":
        if "Silver" in player.hand:
            player.IncreaseCoins(1)

def isCoinCard(cardName):
    return cardName in ["Copper", "Silver", "Gold", "Harem"]
