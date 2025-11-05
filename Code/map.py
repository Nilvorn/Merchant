import math



PortRoyale = {
    "Name" : "Port Royale",
    "Description" :
    "Once the richest city in the Caribbean, now half-sunken but still active in trade."
    "YearFounded: 1655",
    "Population" : 25000,
    "Location" : (1,2)

}


Nassau = {
    "Name" : "Nassau",
    "Description" :
    "A free port in the Bahamas that thrives on smuggling and outlaw trade."
    "YearFounded: 1655",
    "Population" : 25000,
    "Location" : (3,4)

}


Tortuga = {
    "Name" : "Tortuga",
    "Description" :
    "A small pirate-controlled island known for black market trade."
    "YearFounded: 1655",
    "Population" : 25000,
    "Location" : ()

}


Kingston = {
    "Name" : "Kingston",
    "Description" :
    "The largest British trade port in Jamaica and a center for sugar exports."
    "YearFounded: 1655",
    "Population" : 25000,
    "Location" : ()

}


Havana = {
    "Name" : "Havana",
    "Description" :
    "Spains greatest port and the hub of its treasure fleets."
    "YearFounded: 1655",
    "Population" : 25000,
    "Location" : ()


}
SanJuan = {
    "Name" : "San Juan",
    "Description" :
    "A fortified port in Puerto Rico known for steady commerce and naval presence."
    "YearFounded: 1655",
    "Population" : 25000,
    "Location" : ()

}


SantoDomingo = {
    "Name" : "Santo Domingo",
    "Description" :
    "An older, quieter Spanish port where smaller traders thrive away from the empires’ eyes."
    "YearFounded: 1655",
    "Population" : 25000,
    "Location" : ()

}

def getAllPorts():
    allPorts = PortRoyale, Nassau, Tortuga, Kingston, Havana, SanJuan, SantoDomingo
    return allPorts

def getStartPort():
    startPort = PortRoyale
    return PortRoyale

def findDistanceBetweenPorts(PortA,PortB):
    PortAX, PortAY = PortA["Location"]
    PortBX, PortBY = PortB["Location"]

    totalX = PortAX - PortBX
    totalY = PortAY - PortBY

    distance = math.sqrt(math.pow(totalX, 2) + math.pow(totalY, 2))

def getAllPortDistancesFromPort(currentPort):
    portDistances = []

    for port in getAllPorts():
        if (port["Name"] == currentPort["Name"]):
            continue;
        distance = findDistanceBetweenPorts(currentPort, port)

        portDistance = {
            "Port" : port,
            "Distance" : distance
        }
        portDistances.append(portDistances)
    return portDistances