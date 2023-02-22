#!/usr/bin/env python3
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
routeNumber = 0
#my option
'''
def permutations(route, ports):
    print("{}--{}".format(route, ports))
    for index, value in enumerate(ports):
        newRoute = route + [value]
        newPorts = ports[:index] + ports[index+1:]
        if len(newPorts) == 0:
            global routeNumber
            routeNumber += 1
            print("route number:{}".format(routeNumber))
            print(' '.join([portnames[i] for i in newRoute]))
        else:
            permutations(newRoute, newPorts)
'''


#Option of course
def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i+1:])


#This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))







