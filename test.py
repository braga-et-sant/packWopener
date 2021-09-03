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
starlight = []
coreSets = ["Legend of Blue Eyes White Dragon", "Metal Raiders", "Spell Ruler", "Pharaoh's Servant",
        "Labyrinth of Nightmare", "Legacy of Darkness", "Pharaonic Guardian", "Magician's Force",
        "Dark Crisis", "Invasion of Chaos", "Ancient Sanctuary", "Soul of the Duelist",
        "Rise of Destiny", "Flaming Eternity", "The Lost Millennium", "Cybernetic Revolution",
        "Elemental Energy", "Shadow of Infinity", "Enemy of Justice", "Power of the Duelist",
        "Cyberdark Impact", "Strike of Neos", "Force of the Breaker", "Tactical Evolution",
        "Gladiator's Assault", "Phantom Darkness", "Light of Destruction", "The Duelist Genesis",
        "Crossroads of Chaos", "Crimson Crisis", "Raging Battle", "Ancient Prophecy",
        "Stardust Overdrive", "Absolute Powerforce", "The Shining Darkness", "Duelist Revolution",
        "Storm of Ragnarok", "Extreme Victory", "Generation Force", "Photon Shockwave",
        "Order of Chaos", "Galactic Overlord", "Return of the Duelist", "Abyss Rising",
        "Cosmo Blazer", "Lord of the Tachyon Galaxy", "Judgment of the Light", "Shadow Specters",
        "Legacy of the Valiant", "Primal Origin", "Duelist Alliance", "The New Challengers",
        "Secrets of Eternity", "Crossed Souls", "Clash of Rebellions", "Dimension of Chaos",
        "Breakers of Shadow", "Shining Victories", "The Dark Illusion", "Invasion: Vengeance",
        "Raging Tempest", "Maximum Crisis", "Code of the Duelist", "Circuit Break",
        "Extreme Force", "Flames of Destruction", "Cybernetic Horizon", "Soul Fusion",
        "Savage Strike", "Dark Neostorm", "Rising Rampage", "Chaos Impact",
        "Ignition Assault", "Eternity Code", "Rise of the Duelist", "Phantom Rage",
        "Blazing Vortex", "Lightning Overdrive", "Dawn of Majesty", "Burst of Destiny",
        "Battle of Chaos"

            ]

setupDone = False

printInfo = True


def randCard(pack):
    return pack[random.randint(-1, len(pack) - 1)]


def setup(packName, packN, boxRatio, cardlist):

    hasSshort = False
    superRate = 1
    ultraRate = 0
    secretRate = 0
    hasUltimate = False
    hasSecret = True
    hasGhost = False
    gHolo = False
    hasStarlight = False
    noRare = False
    packlist = []

    base_url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    site = "?cardset=" + packName
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

    if packName in coreSets:
        cNum = 9
        hasFoilLast = True
        hasRare = True
        if packName in coreSets[coreSets.index("Legend of Blue Eyes White Dragon"):coreSets.index("Soul of the Duelist")]:
            superRate = 6
            ultraRate = 12
            secretRate = 31
            if packName in coreSets[coreSets.index("Legend of Blue Eyes White Dragon"):coreSets.index("Legacy of Darkness")]:
                hasSshort = True
                print("This pack has super short prints")
        if packName in coreSets[coreSets.index("Soul of the Duelist"):coreSets.index("Tactical Evolution")]:
            superRate = 6
            ultraRate = 24
            hasUltimate = True
            print("This pack has 1:24 Ultras")
            print("This pack has Ultimates")
            if packName in coreSets[coreSets.index("Soul of the Duelist"):coreSets.index("Strike of Neos")]:
                hasSecret = False
                print("This pack has no Secret Rares")
        if packName in coreSets[coreSets.index("Tactical Evolution"):coreSets.index("Breakers of Shadow")]:
            hasGhost = True
            superRate = 5
            hasUltimate = True
            print("This pak has Ghost Rares")
            print("This pack has 1:5 Supers")
            print("This pack has Ultimates")
            if packName in coreSets[coreSets.index("The Shining Darkness"):coreSets.index("Breakers of Shadow")]:
                secretRate = 23
                print("This pack has 1:23 Secrets")
        if packName in coreSets[coreSets.index("Breakers of Shadow"):]:
            gHolo = True
            ultraRate = 6
            secretRate = 12
            ultra6 = True
            secret12 = True
            print("This pak has guaranteed Holos every pack")
            print("This pack has 1:6 Ultras")
            print("This pack has 1:12 Secrets")
            if packName in coreSets[coreSets.index("Rising Rampage"):]:
                print("This pack has starlight rares")
                hasStarlight = True
                if packName in coreSets[coreSets.index("Eternity Code"):]:
                    print("This pack has no Rare cards")
                    hasRare = False



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
            if (cardset["set_name"] == packName and cardset["set_rarity"] == "Starlight Rare"):
                importantInfo["rarity"] = "Starlight Rare"
                starlight.append(importantInfo) if importantInfo not in ghost else None

    if(printInfo):
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
        print(starlight)
        print(len(starlight))

    if (boxRatio):

        superOk = False
        ultraOk = False
        secretOk = False

        boxModSuper = 0
        boxModUltra = 0
        boxModSecret = 0
        superMod = random.randint(0, 10)
        if(superMod == 0):
            boxModSuper+=1
        elif(superMod == 9):
            boxModSuper-=1

        ultraMod = random.randint(0, 10)
        if (ultraMod == 0):
            boxModUltra += 1
        elif (ultraMod == 9):
            boxModUltra -= 1

        secretMod = random.randint(0, 10)
        if (secretMod == 0):
            boxModSecret += 1
        elif (secretMod == 9):
            boxModSecret -= 1

        while (not superOk or not ultraOk or not secretOk):
            cardlist = []
            packlist = []
            for i in range(0, packN):
                packlist.append(openPack(packName, hasSshort, ultraRate, superRate, secretRate, hasUltimate, hasSecret,
                                         hasGhost, hasRare, hasStarlight, gHolo, cNum, hasFoilLast))
            for pack in packlist:
                for card in pack:
                    cardlist.append(card)
            foils = foilCount(cardlist, False, packName, packN, True, False)
            superOk = gHolo or len(foils["Super Rare"]) == int(packN / superRate) + boxModSuper
            ultraOk = len(foils["Ultra Rare"]) == int(packN / ultraRate)  + boxModUltra
            secretOk = len(foils["Secret Rare"]) == int(packN / secretRate)  + boxModSecret
        return packlist
    else:
        for i in range(0, packN):
            packlist.append(openPack(packName, hasSshort, ultraRate, superRate, secretRate, hasUltimate, hasSecret,
                                     hasGhost, hasRare, hasStarlight, gHolo, cNum, hasFoilLast))
        return packlist



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


def openPack(packName, hasSshort, ultraRate, superRate, secretRate, hasUltimate, hasSecret, hasGhost, hasStarlight,
             hasRare, gHolo, cNum, hasFoilLast):

    pack = []

    for i in range(0, cNum-2):
        srarity = random.randint(0, 60)
        if (hasSshort and len(sshort) != 0 and srarity == 1):
            pack.append(randCard(sshort))
        elif (len(short) != 0 and (srarity == 2 or srarity == 3)):
            pack.append(randCard(short))
        else:
            pack.append(randCard(common))

    if(not hasRare):
        srarity = random.randint(0, 30)
        if(len(short) != 0 and srarity == 0):
            pack.append(randCard(short))
        else:
            pack.append(randCard(common))
    else:
        pack.append(randCard(rare))

    if hasStarlight:
        rarity = random.randint(0, 576)
        if(rarity == 0):
            pack.append(randCard(starlight))
            return pack

    if hasGhost:
        rarity = random.randint(0, 288)
        if(rarity == 0):
            pack.append(randCard(ghost))
            return pack

    if hasUltimate:
        rarity = random.randint(0, 32)
        if (rarity == 0):
            pack.append(randCard(ulti))
            return pack

    if hasSecret:
        rarity = random.randint(0, secretRate)
        if(rarity == 0):
            pack.append(randCard(secret))
            return pack



    rarity = random.randint(0, ultraRate)
    if(rarity == 0):
        pack.append(randCard(ultra))
        return pack

    if gHolo:
        pack.append(randCard(super))
        return pack
    else:
        rarity = random.randint(0, superRate)
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

def foilCount(cardlist, sepFoils, packName, packNumber, boxRatio, printInfo):
    if(printInfo):
        print("High Rarity cards pulled:")
    mySuper = []
    myUltra = []
    myShort = []
    mySShort = []
    myUltimate = []
    mySecret = []
    myGhost = []
    myStarlight = []
    for card in cardlist:
        if (card["rarity"] == "Short Print"):
            myShort.append(card)
        elif (card["rarity"] == "Super Rare"):
            mySuper.append(card)
        elif (card["rarity"] == "Ultra Rare"):
            myUltra.append(card)
        elif (card["rarity"] == "Super Short Print"):
            mySShort.append(card)
        elif (card["rarity"] == "Ultimate Rare"):
            myUltimate.append(card)
        elif (card["rarity"] == "Secret Rare"):
            mySecret.append(card)
        elif (card["rarity"] == "Ghost Rare"):
            myGhost.append(card)
        elif (card["rarity"] == "Starlight Rare"):
            myStarlight.append(card)



    if(sepFoils):
        foilYdk(mySuper, myUltra, myUltimate, mySecret, myGhost, myStarlight, packName, packNumber)

    if(printInfo):
        foilPrint(myShort, "Normal Rare")
        foilPrint(mySShort, "Super Short Print")
        foilPrint(mySuper, "Super Rare")
        foilPrint(myUltra, "Ultra Rare")
        foilPrint(myUltimate, "Ultimate Rare")
        foilPrint(mySecret, "Secret Rare")
        foilPrint(myGhost, "Ghost Rare")
        foilPrint(myStarlight, "Starlight Rare")

    if (boxRatio):
        foils = {
            "Super Rare": mySuper,
            "Ultra Rare": myUltra,
            "Secret Rare": mySecret
        }
        return foils

def foilYdk( mySuper, myUltra, myUltimate, mySecret, myGhost, myStarlight, packName, packNumber):
    f = open(packName + str(packNumber) + "packsDraftFoils.ydk", "x")
    f.write("#Made with Iason PackOpener Foils Only File\n")
    f.write("#main\n")
    for card in myStarlight:
        f.write(str(card["id"]) + "\n")
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
    boxRatio = True

    packName = "Rising Rampage"
    packNumber = 24


    packlist = setup(packName, packNumber, boxRatio, cardlist)

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
        foilCount(cardlist, sepFoils, packName, packNumber, False, True)

if __name__ == '__main__':
    main()
