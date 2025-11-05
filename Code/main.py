from map import getAllPorts,getStartPort
from player import Player
player = Player()
allPorts = getAllPorts()
startPort = getStartPort()

print ("Welcome to the high seas Merchant")

print ("Please select the name of your mighty vessel.")

player.shipname = input("> ")

print ("The valiant vessel " + player.shipname + " is currently docked at " + startPort['Name'] + ".")


print("Ports:")
for port in allPorts:
    print("- " + port["Name"])


input("\nThe program has finished. Press any key to exit.");