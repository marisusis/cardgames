import random
import math

def buildCard(suit,value):
    ending = "  |"
    result = "\n"
    if (len(value) >= 2):
        ending = " |"
    if (suit=="H"):
        result+="\033[91m"
        result += (" ___\n")
        result += "|"+value+ending+"\n"
        result += ("|(`)|\n")
        result += ("|_\_|\n")
        result += "\033[0m"
    elif (suit == "S"):
        result += "\033[90m"
        result += (" ___\n")
        result += "|"+value+ending+"\n"
        result += ("| ^ |\n")
        result += ("|(,)|\n")
        result += "\033[0m"
    elif (suit == "D"):
        result += "\033[91m"
        result += (" ___\n")
        result += "|"+value+ending+"\n"
        result += ("| /\|\n")
        result += ("|_\/|\n")
        result += "\033[0m"
    elif (suit == "C"):
        result += "\033[90m"
        result += (" ___\n")
        result += "|"+value+ending+"\n"
        result += ("| o |\n")
        result += ("|o,o|\n")
        result += "\033[0m"
    return result

values = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits = ["H","C","S","D"]
cardsUsed = ["4D"]
cards = {'player':[],'cpu':[]}
gameOver = False

def useCard(card):
    if (cardUsed(card.get("value"),card.get("suit"))):
        print("[!]: cannot discard card; card already used")
    else:
        cardsUsed.append(value+suit)

def cardUsed(card):
    if (cardsUsed.count(card.get("value")+card.get("suit")) > 0):
        return True
    else:
        return False

def getCardArt(card,over):
    if (over or card.get("face")):
        return buildCard(card.get("suit"),card.get("value"))
    else:
        return "[ ]"
    return "BAD"


def addCardToHand(ent,card):
    cards.get(ent).append(card)
    return True

# def dealCard():

def showCards(ent):
    i = 0
    print(ent+" cards: ",end="")
    while (i < len(cards.get(ent))):
        card = cards.get(ent)[i]
        print(getCardArt(card,False),end="")
        i += 1
    print("")

def oShowCards(ent,override):
    i = 0
    print(ent+" cards: ",end="")
    while (i < len(cards.get(ent))):
        card = cards.get(ent)[i]
        print(getCardArt(card,override),end="")
        i += 1
    print("")

def getRandomCard(face):
    return {'suit':random.choice(suits),"value":random.choice(values),"face":face}

def doRound():
    addCardToHand("player",getRandomCard(True))
    addCardToHand("cpu",getRandomCard(True))
    addCardToHand("player",getRandomCard(True))
    addCardToHand("cpu",getRandomCard(False))
    showCards("player")
    # print(str(getHandSum("player")))
    showCards("cpu")
    ok = 0
    while (True):
        if (ok == 0):
            ok = doAction("player",input("action: "))
        elif (ok == 1):
            ok = doDealer()
        elif (ok == 3):
            oShowCards("player", True)
            oShowCards("cpu", True)
            print("cpu wins")
            break
        elif (ok == 4):
            oShowCards("player", True)
            oShowCards("cpu", True)
            print("player wins")
            break
        else:
            oShowCards("player", True)
            oShowCards("cpu", True)
            if (getHandSum("player") < getHandSum("cpu")):
                print("cpu wins 1")
                break
            elif (getHandSum("player") == 21):
                print("player wins 2")
                break
            elif (getHandSum("player") > getHandSum("cpu")):
                print("player wins 3")
                break
            else:
                print("error")
                break


def doAction(ent,action):
    if (action == "stand"):
        print(ent + " chooses to stand.")
        showCards("player")
        return checkOver(ent,1)
    elif (action == "double"):
        print(ent + " chooses to double down.")
        showCards("player")
        return checkOver(ent,0)
    elif (action == "hit"):
        print(ent + " chooses to hit.")
        addCardToHand(ent,getRandomCard(True))
        showCards("player")
        return checkOver(ent,0)


def checkOver(ent,otherwise):
    if (ent == "player"):
        if (getHandSum("player")>21):
            return 3
    if (ent == "cpu"):
        if (getHandSum("cpu")>21):
            return 4
    return otherwise

def checkBlackJack(ent):
    if (getHandSum(ent) == 21):
        return True
    else:
        return True

def getHandSum(ent):
    i = 0
    sum = 0
    while (i < len(cards.get(ent))):
        card = cards.get(ent)[i]
        value = card.get("value")
        if (value == "Q" or value == "K" or value == "J"):
            value = "10"
        elif (value == "A"):
            value = "11"
        sum += int(value)
        i += 1
    return sum

def doDealer():
    if (getHandSum("cpu") >= 17) :
        doAction("cpu","stand")
    elif (getHandSum("cpu") <= 16) :
        doAction("cpu","hit")
    elif (getHandSum("cpu") >= 21):
        return 2;


buildCard("C","10")
buildCard("C","1")
buildCard("D","A")
doRound()

print()
