import random

import requests
import json
import pprint

common = []
short = []
sshort = []
rare = []
super = []
ultra = []
ulti = []
secret = []
ghost = []
sets = ["Legend of Blue Eyes White Dragon", "Metal Raiders", "Spell Ruler", "Pharaoh's Servant",
        "Labyrinth of Nightmare", "Legacy of Darkness", "Pharaonic Guardian", "Magician's Force",
        "Dark Crisis", "Invasion of Chaos", "Ancient Sanctuary", "Soul of the Duelist",
        "Rise of Destiny", "Flaming Eternity", "The Lost Millennium", "Cybernetic Revolution",
        "Elemental Energy", "Shadow of Infinity", "Enemy of Justice", "Power of the Duelist",
        "Cyberdark Impact", "Strike of Neos", "Force of the Breaker", "Tactical Evolution",
        "Gladiator's Assault", "Phantom Darkness", "Light of Destruction", "The Duelist Genesis",
        "Crossroads of Chaos", "Crimson Crisis", "Raging Battle", "Ancient Prophecy",
        "Stardust Overdrive", "Absolute Powerforce", "The Shining Darkness", "Duelist Revolution"]
hasSshort = False
ultra24 = False
hasUltimate = False
hasSecret = True
hasGhost = False
super5 = False
secret23 = False
setupDone = False


def randCard(pack):
    return pack[random.randint(-1, len(pack) - 1)]


def setup(packName):
    global hasSshort
    global ultra24
    global hasUltimate
    global hasSecret
    global hasGhost
    global super5
    global secret23
    global setupDone

    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    site = "?cardset=" + packName
    setupDone = True
    random.seed()

    first_response = requests.get(base_url + site)
    response_list = first_response.json()

    print(first_response.json())

    if ("error" in response_list):
        print("Invalid pack")
        return

        # print(response_list )
    print("\n\n")

    data = response_list["data"]

    if packName in sets[sets.index("Legend of Blue Eyes White Dragon"):sets.index("Legacy of Darkness")]:
        hasSshort = True
        print("This pack has Super Short Prints")
    if packName in sets[sets.index("Legacy of Darkness"):sets.index("Tactical Evolution")]:
        ultra24 = True
        hasUltimate = True
        print("This pack has 1:24 Ultras")
        print("This pack has Ultimates")
        if not (packName in sets[sets.index("Strike of Neos"):sets.index("Tactical Evolution")]):
            hasSecret = False
            print("This pack has no Secret Rares")
    if packName in sets[sets.index("Tactical Evolution"):]:
        hasGhost = True
        super5 = True
        hasUltimate = True
        print("This pak has Ghost Rares")
        print("This pack has 1:5 Supers")
        print("This pack has Ultimates")
        if packName in sets[sets.index("The Shining Darkness"):]:
            secret23 = True
            print("This pack has 1:23 Secrets")



    for card in data:
        # print(card)
        addFlag = 0
        for cardset in card["card_sets"]:

            importantInfo = {
                "name": card["name"],
                "id": card["id"],
                "rarity": ""
            }

            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Common"):
                importantInfo["rarity"] = "Common"
                common.append(importantInfo) if importantInfo not in common else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Short Print"):
                importantInfo["rarity"] = "Short Print"
                short.append(importantInfo) if importantInfo not in short else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Super Short Print"):
                importantInfo["rarity"] = "Super Short Print"
                sshort.append(importantInfo) if importantInfo not in sshort else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Rare"):
                importantInfo["rarity"] = "Rare"
                rare.append(importantInfo) if importantInfo not in rare else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Super Rare"):
                importantInfo["rarity"] = "Super Rare"
                super.append(importantInfo) if importantInfo not in super else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Ultra Rare"):
                importantInfo["rarity"] = "Ultra Rare"
                ultra.append(importantInfo) if importantInfo not in ultra else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Secret Rare"):
                importantInfo["rarity"] = "Secret Rare"
                secret.append(importantInfo) if importantInfo not in secret else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Ultimate Rare"):
                importantInfo["rarity"] = "Ultimate Rare"
                ulti.append(importantInfo) if importantInfo not in ulti else None
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Ghost Rare"):
                importantInfo["rarity"] = "Ghost Rare"
                ghost.append(importantInfo) if importantInfo not in ghost else None

    print(common)
    print(len(common))
    print(short)
    print(len(short))
    print(sshort)
    print(len(sshort))
    print(rare)
    print(len(rare))
    print(super)
    print(len(super))
    print(ultra)
    print(len(ultra))
    print(secret)
    print(len(secret))
    print(ulti)
    print(len(ulti))
    print(ghost)
    print(len(ghost))


# Super Short prints seemingly discontinued after Legacy of Darkness
# Soul of the Duelist and onwards changes:
# Ultras are 1 in 24
# Ultimata rares become a thing
# No more secret rares
# Strike of Neos: Secret Rares return
# Tactical Evolution and onwards:
# Ultras go back to 1 in 12
# Ghost Rares become a thing
# Supers become 1 in 5 instead of 6
# The Shining Darkness: Secrets go to 1 in 23
# Ultimate: 1 in 32 packs
# Ghost: 1 in 288


def openPack(packName):

    global hasSshort
    global ultra24
    global hasUltimate
    global hasSecret
    global hasGhost
    global super5
    global secret23
    global setupDone

    if not setupDone:
        setup(packName)

    pack = []

    for i in range(0, 7):
        srarity = random.randint(0, 60)
        if (hasSshort and len(sshort) != 0 and srarity == 1):
            pack.append(randCard(sshort))
        elif (len(short) != 0 and (srarity == 2 or srarity == 3)):
            pack.append(randCard(short))
        else:
            pack.append(randCard(common))

    pack.append(randCard(rare))

    if hasGhost:
        rarity = random.randint(0, 288)
        if(rarity == 0):
            pack.append(randCard(ghost))
            return pack

    if hasSecret:
        if secret23:
            rarity = random.randint(0, 23)
        else:
            rarity = random.randint(0, 31)
        if(rarity == 0):
            pack.append(randCard(secret))
            return pack

    if hasUltimate:
        rarity = random.randint(0, 32)
        if(rarity == 0):
            pack.append(randCard(ulti))
            return pack

    if ultra24:
        rarity = random.randint(0, 24)
    else:
        rarity = random.randint(0, 12)
    if(rarity == 0):
        pack.append(randCard(ultra))
        return pack

    if super5:
        rarity = random.randint(0, 5)
    else:
        rarity = random.randint(0, 6)
    if(rarity == 0):
        pack.append(randCard(super))
        return pack

    srarity = random.randint(0, 60)
    if (len(sshort) != 0 and srarity == 1):
        pack.append(randCard(sshort))
    elif (len(short) != 0 and (srarity == 2 or srarity == 3)):
        pack.append(randCard(short))
    else:
        pack.append(randCard(common))

    return pack

def foilPrint(list, rarityName):
    if (len(list) > 0):
        print("You pulled " + str(len(list)) + " " + rarityName + "(s): ")
        for card in list:
            if(list[len(list) - 1] == card):
                print(card["name"])
            else:
                print(card["name"], end=", ")

def foilCount(cardlist, sepFoils, packName, packNumber):
    print("High Rarity cards pulled:")
    mySuper = []
    myUltra = []
    myShort = []
    mySShort = []
    myUltimate = []
    mySecret = []
    myGhost = []
    for card in cardlist:
        if (card["rarity"] == "Super Rare"):
            mySuper.append(card)
        if (card["rarity"] == "Ultra Rare"):
            myUltra.append(card)
        if (card["rarity"] == "Short Print"):
            myShort.append(card)
        if (hasSshort and card["rarity"] == "Super Short Print"):
            mySShort.append(card)
        if (hasUltimate and card["rarity"] == "Ultimate Rare"):
            myUltimate.append(card)
        if (hasSecret and card["rarity"] == "Secret Rare"):
            mySecret.append(card)
        if (hasGhost and card["rarity"] == "Ghost Rare"):
            myGhost.append(card)

    if(sepFoils):
        f = open(packName + str(packNumber) + "packsDraftFoils.ydk", "x")
        f.write("#Made with IasonPackOpener Foils Only File\n")
        f.write("#main\n")
        for card in myGhost:
            f.write(str(card["id"]) + "\n")
        for card in mySecret:
            f.write(str(card["id"]) + "\n")
        for card in myUltimate:
            f.write(str(card["id"]) + "\n")
        for card in myUltra:
            f.write(str(card["id"]) + "\n")
        for card in mySuper:
            f.write(str(card["id"]) + "\n")




    foilPrint(mySuper, "Super Rare")
    foilPrint(myUltra, "Ultra Rare")
    foilPrint(myShort, "Normal Rare")
    foilPrint(mySShort, "Super Short Print")
    foilPrint(myUltimate, "Ultimate Rare")
    foilPrint(mySecret, "Secret Rare")
    foilPrint(myGhost, "Ghost Rare")


def main():
    packName = input("Which pack to open: ")
    print(packName)
    packNumber = input("How many packs: ")
    print(packNumber)

    write = False
    trim = True
    cardlist = []
    countFoils = True
    sepFoils = False

    packName = "The Shining Darkness"
    packNumber = 24

    packlist = []

    for i in range(0, int(packNumber)):
        packlist.append(openPack(packName))

    if write:
        if(trim):
            f = open(packName + str(packNumber) + "packsDraftTrimmed.ydk", "x")
        else:
            f = open(packName + str(packNumber) + "packsDraft.ydk", "x")
        f.write("#Made with IasonPackOpener\n")
        f.write("#main\n")

    for pack in packlist:
        print("Opening one pack of " + packName)
        for card in pack:
            print(card)
            cardlist.append(card)
            if write:
                if(trim):
                    if(cardlist.count(card) < 3):
                        f.write(str(card["id"]) + "\n")
                else:
                    f.write(str(card["id"]) + "\n")

    if(countFoils):
        foilCount(cardlist, sepFoils, packName, packNumber)


if __name__ == '__main__':
    main()
