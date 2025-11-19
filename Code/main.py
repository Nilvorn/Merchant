from map import *
from player import Player
import os

allPorts = getAllPorts()
startPort = getStartPort()
player = Player(startPort)

print ("Welcome to the high seas Merchant")

# print ("Please select the name of your mighty vessel.")
# player.shipname = input("> ")
player.shipname = "HMS bob"

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

input("\nThe program has finished. Press any key to exit.")