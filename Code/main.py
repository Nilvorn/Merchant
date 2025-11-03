from map import getAllPorts
from player import Player

print ("Welcome to Merchant")

allPorts = getAllPorts()

print("### Ports:")
for port in allPorts:
    print("- " + port["Name"])


input("\nThe program has finished. Press any key to exit.");