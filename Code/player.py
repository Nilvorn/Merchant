from map import *
from cargo import *
class Player:
    def __init__(self, startingPort):
        
        self.shipName = "Unnamed Ship"

        self.currentLocation = startingPort

        self.gold = 50

        self.shipRange = 5

        self.shipCargoSpace = 10

        shipCargoInventory = {}

        def setupCargoInventory(self):
            allCargo = getAllCargo()
            for cargo in allCargo:
                shipCargoInventory[cargo.name] = 0
        
        def __init__(self):
            self.setupCargoInventory()
            print("Player is initialized!")
            input()

    def isPortWithingRange(self, destinationPort):
        return findDistanceBetweenPorts(self.currentLocation, destinationPort) < self.shipRange
    