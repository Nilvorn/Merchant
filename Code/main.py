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
    input("...")

currentPortUI()

def mainUI():
    while True:
        os.system("cls")
        print("The vessel " + player.shipName + " is currently docked at " + player.currentLocation["Name"] + " harbour" ".\n")
        print("Captain, what are your orders?\n")
        print("1. Disembark the ship and visit the current port.")
        print("2. Sail out to another port")
        print("3. Quit game\n")

        playerInput = input("> ")
        if (playerInput == "3"):
            return
        elif (playerInput == "1"):
            currentPortUI()
        elif (playerInput == "2"):
            portToTravelTo = getPortToTravelUI()
            if (portToTravelTo == -1):
                continue
            player.currentLocation = portToTravelTo
            sailingUI()

mainUI()

# def holdUI():
#     os.system("cls")
#     print("- Cargo Hold -\n")
#     print("You have " + str(player.shipCargoSpace) + " total cargo space.")
#     print("You are currently using " + str(usedCargoSpace) + " of it.\n")
#     print("Cargo Inventory:\n")
#     for cargoName in player.shipCargoInventory:
#         print(cargoName + " : " + str(player.shipCargoInventory[cargoName]))
#     input("\n(Press any key to continue...)")

input("\nThe program has finished. Press any key to exit.")