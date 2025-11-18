from map import *
from player import Player

allPorts = getAllPorts()
startPort = getStartPort()
player = Player(startPort)

print ("Welcome to the high seas Merchant")

# print ("Please select the name of your mighty vessel.")
# player.shipname = input("> ")
player.shipname = "HMS bob"

print ("The valiant vessel " + player.shipname + " is currently docked at " + startPort['Name'] + ".")

print("Ports:")
for port in allPorts:
     withinRange = player.isPortWithingRange(port)
     if (withinRange):
         print("- Is " + port["Name"] + " in range? " + str(withinRange))



def getPortToTravelUI():

    print("Where shall we travel?")
    print("")
    for port in allPorts:
        print("-  " + port["Name"] + "    Is in range? " + str(withinRange))

    playerPortInput = input(" ")
    portToTravelTo = 'No port'
    for port in allPorts:
        if (playerPortInput == port["Name"]):
            portToTravelTo = port
    
    if (portToTravelTo == 'No port'):
        print("Can you read a map Captain?")
        return portToTravelTo == False

    if portToTravelTo == False(withinRange):
        print("We can't make it there captain.")
    else:
        print("We are off captain.")


#input("\nThe program has finished. Press any key to exit.");