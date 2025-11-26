from map import *
from cargo import *
class Player:
    def __init__(self, startingPort):
        
        self.shipName = "Unnamed Ship"

        self.currentLocation = startingPort

        self.gold = 50

        self.shipRange = 5

        self.shipCargoSpace = 10

        self.shipCargoInventory = {}

        self.setupCargoInventory()
        print("Player is initialized!")
        print("Press any key to continue.")
        input()

    def setupCargoInventory(self):
        allCargo = getAllCargo()
        for cargo in allCargo:
            self.shipCargoInventory[cargo.name] = 0

    def isPortWithingRange(self, destinationPort):
        return findDistanceBetweenPorts(self.currentLocation, destinationPort) < self.shipRange
    