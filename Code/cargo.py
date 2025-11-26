class Cargo:
    name = "Unnamed Cargo"
    basePrice = 0

rum = Cargo()
rum.name = "Rum"
rum.basePrice = 10

spices = Cargo()
spices.name = "Spices"
spices.basePrice = 20

blackPowder = Cargo()
blackPowder.name = "Black Powder"
blackPowder.basePrice = 50

pistols = Cargo()
pistols.name = "Pistols"
pistols.basePrice = 100

muskets = Cargo()
muskets.name = "Muskets"
muskets.basePrice = 150

sugar = Cargo()
sugar.name = "Sugar"
sugar.basePrice = 5

cannonballs = Cargo()
cannonballs.name = "Cannon Balls"
cannonballs.basePrice = 25

tobacco = Cargo()
tobacco.name = "Tobacco"
tobacco.basePrice = 15

grain = Cargo()
grain.name = "Grain"
grain.basePrice = 8

def getAllCargo():
    allCargo = [rum, spices, blackPowder, pistols, muskets, sugar, cannonballs, tobacco, grain]
    return allCargo

