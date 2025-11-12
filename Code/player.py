from map import *
class Player:
    def __init__(self, startingPort):
        self.shipName = "Unnamed Ship"

        self.currentLocation = startingPort

        self.gold = 50

        self.shipRange = 5

        self.shipCargoSpace = 5

    def isPortWithingRange(self, destinationPort):
        return findDistanceBetweenPorts(self.currentLocation, destinationPort) < self.shipRange
    