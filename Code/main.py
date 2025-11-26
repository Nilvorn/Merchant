from prettytable import PrettyTable
from map import *
from player import *
from cargo import *
import os

allPorts = getAllPorts()
startPort = getStartPort()
player = Player(startPort)

print ("Welcome to the high seas Merchant")

# print ("Please select the name of your mighty vessel.")
# player.shipname = input("> ")
player.shipname = "HMS Bob"

print ("The valiant vessel " + player.shipname + " is currently docked at " + startPort['Name'] + ".")


def getPortToTravelUI():

    print("Where shall we travel?")
    print("")
    for port in allPorts:
        withinRange = player.isPortWithingRange(port)
        if (withinRange):
            print("-  " + port["Name"])
        else:
            print("-  " + port["Name"] + "   [TOO FAR]")


    playerPortInput = input(" ")
    portToTravelTo = 'No port'
    for port in allPorts:
        if (playerPortInput == port["Name"]):
            portToTravelTo = port
    
    if (portToTravelTo == 'No port'):
        print("Can you read a map Captain?")
        return None

    withinRange = player.isPortWithingRange(portToTravelTo)
    if (withinRange):
        print("We are off captain.")
        return portToTravelTo
    else:
        print("We can't make it there captain.")
        return None

# while True:
#     os.system("cls")
#     portToTravelTo = getPortToTravelUI()

#     if (portToTravelTo == None):
#         input("(Press any key to continue...)")
#     else:
#         break
# print("Going to : " + str(portToTravelTo))

def leavePortUI():
    portToTravelTo = getPortToTravelUI()
    if (portToTravelTo == -1):
        return
    player.currentLocation = portToTravelTo
    sailingUI()

def currentPortUI():
    os.system("cls")
    print("- " + player.currentLocation["Name"] + "  -\n")
    print("Establised " + str(player.currentLocation["YearFounded"]) + 
          "| Population " +  str(player.currentLocation["Population"]))
    print("\n" + player.currentLocation["Description"])
    input("\n(Press any key to continue...)")

def sailingUI():
    os.system("cls")
    print("Traveling...")
    input("Press any key to arrive at port...")

def holdUI():
    os.system("cls")
    table = PrettyTable()
    table.field_names = ["Name", "No."]
    # TODO: Loop over all player cargo types
    # Something like: for cargo in allPlayerCargo:
    # Then call table.addRow
    table.add_row(["Rum",0])
    table.add_row(["Spices",0])
    table.add_row(["Black Powder",0])
    table.add_row(["Pistols",0])
    table.add_row(["Muskets",0])
    table.add_row(["Sugar",0])
    table.add_row(["Cannon Ball",0])
    table.add_row(["Tobacco",0])
    table.add_row(["Grain",0])

    print("--HOLD--")
    print("Capacity: " + str(player.shipCargoSpace))
    print(table)
    input("\n(Press any key to return.)")

currentPortUI()

def mainUI():
    while True:
        os.system("cls")
        print("The vessel " + player.shipName + " is currently docked at " + player.currentLocation["Name"] + " harbour" ".\n")
        print("Captain, what are your orders?\n")
        print("1. Disembark the ship and visit the current port.")
        print("2. Sail out to another port.")
        print("3. See what is in the hold.")
        print("4. Quit game\n")

        playerInput = input("> ")
        if (playerInput == "4"):
            continue
        elif (playerInput == "1"):
            currentPortUI()
        elif (playerInput == "2"):
            leavePortUI()
        elif (playerInput == "3"):
            holdUI()

mainUI()

input("\nThe program has finished. Press any key to exit.")