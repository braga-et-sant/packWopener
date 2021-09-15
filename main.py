#!/usr/bin/python3
import test
import PySimpleGUI as sg

#TODO: Figure out why popups keep closing the program
#TODO: Implement sets checkbox in uitest.py

goldSets = ["Gold Series", "Gold Series 2009", "Gold Series 3", "Gold Series 4: Pyramids Edition",
            "Gold Series: Haunted Mine"]

draftSets = ["Legend of Blue Eyes White Dragon", "Metal Raiders", "Spell Ruler", "Pharaoh's Servant",
            "Labyrinth of Nightmare", "Legacy of Darkness", "Pharaonic Guardian", "Magician's Force",
            "Dark Crisis", "Invasion of Chaos", "Ancient Sanctuary", "Soul of the Duelist",
            "Rise of Destiny", "Flaming Eternity", "The Lost Millennium", "Cybernetic Revolution",
            "Elemental Energy", "Shadow of Infinity", "Enemy of Justice", "Power of the Duelist",
            "Cyberdark Impact", "Strike of Neos", "Force of the Breaker", "Tactical Evolution",
            "Gladiator's Assault", "Phantom Darkness", "Light of Destruction", "The Duelist Genesis",
            "Crossroads of Chaos", "Crimson Crisis", "Raging Battle", "Ancient Prophecy",
            "Stardust Overdrive", "Dark Beginning 1", "Dark Beginning 2", "Dark Revelation Volume 1",
            "Dark Revelation Volume 2", "Dark Revelation Volume 3", "Dark Revelation Volume 4",
            "Hidden Arsenal", "Gold Series", "Dark Legends", "Retro Pack", "Gold Series 2009",
            "Retro Pack 2"]

hiddenArset = ["Hidden Arsenal", "Hidden Arsenal 2", "Hidden Arsenal 3", "Hidden Arsenal 4: Trishula's Triumph",
               "Hidden Arsenal 5: Steelswarm Invasion", "Hidden Arsenal 5: Steelswarm Invasion: Special Edition",
               "Hidden Arsenal 6: Omega Xyz", "Hidden Arsenal 7: Knight of Stars", "Hidden Arsenal: Special Edition",
]

SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

ydkmess = "Pulled packs will be put in a YDK file inside ./pulls."
remextmess = "Doesn't add any copies of the card to the YDK after you have acquired 3"
sepfoilmess = "Adds the foil pulls to a different YDK file also inside ./pulls"
boxratmess = "Makes the box adhere to common box ratios, with a small RNG"

def main():
    writeYdk = False
    trimYdk = False
    writeFoil = False
    ratio = False

    layout = [[sg.Text('Please type the set to be pulled below:')],
              ###Checkboxes
              [sg.Checkbox('YDK Output', tooltip=ydkmess, enable_events=True, key="-YDKOut-"),
               sg.Checkbox('Remove Extras', tooltip=remextmess, disabled=True, enable_events=True, key="-RemExtra-"),
               sg.Checkbox('Separate Foils', tooltip=sepfoilmess, disabled=True, enable_events=True, key="-SepFoil-"),
               sg.Checkbox('Box Ratios', tooltip=boxratmess, enable_events=True, key="-BoxRat-") ],
              ###CheckBoxes
              [sg.In(key='-IN-')],
              [sg.Button('Go'), sg.Button('Clear'), sg.Button('Exit')],
              [sg.Output(size=(100, 20), key='-OUTPUT-')]
              ]

    window = sg.Window('Pack Opener', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Go':
            if values['-IN-'] in test.coreSets or values['-IN-'] in test.reprintSets or values['-IN-'] in test.battleSets or values['-IN-'] in test.buildSets or values['-IN-'] in test.collectionSets or values['-IN-'] in test.duelistSets or values['-IN-'] in test.goldSets or values['-IN-'] in test.hiddenArset or values['-IN-'] in test.collectorBoxSets or values['-IN-'] in test.sixtySets or values['-IN-'] in test.otherSets or values['-IN-'] in test.retropack:
                print("This set exists in the files")
                pullMultiple([values['-IN-']], writeYdk, trimYdk, writeFoil, ratio)
                #sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
                window['-IN-'].update('')
            elif values['-IN-'] == "All":
                print("Pulling all packs")
                pullMultiple(draftSets, writeYdk, trimYdk, writeFoil, ratio)
                #sg.popup("You have just pulled everything")
                window['-IN-'].update('')
            else:
                print("Invalid Output")
        if event == 'Clear':
            #sg.popup_get_text(f"Your favorite color is {values['-COLOR-'][0]}")
            window['-OUTPUT-'].update('')
        if event == "-YDKOut-":
            window['-RemExtra-'].update(disabled=writeYdk)
            if(window['-RemExtra-'].get() == True):
                window['-RemExtra-'].update(False)
            if (window['-SepFoil-'].get() == True):
                window['-SepFoil-'].update(False)
            window['-SepFoil-'].update(disabled=writeYdk)
            writeYdk = not writeYdk
            print(f"YDKOut is now {writeYdk}")
        if event == "-RemExtra-":
            trimYdk = not trimYdk
            print(f"RemExtra is now {trimYdk}")
        if event == "-SepFoil-":
            writeFoil = not writeFoil
            print(f"SepFoil is now {writeYdk}")
        if event == "-BoxRat-":
            ratio = not ratio
            print(f"BoxRat is now {ratio}")
    window.close()

def pullMultiple(packs, writeYdk, trimYdk, writeFoil, ratio):
    howmany = 0
    writeYdk = True
    trimYdk = True
    writeFoil = True
    ratio = True
    for pack in packs:
        if pack in goldSets:
            howmany = 5
        elif pack in hiddenArset:
            howmany = 8
        else:
            howmany = 24
        test.main(pack, howmany, writeYdk, trimYdk, writeFoil, ratio)


if __name__ == '__main__':
    main()
