#!/usr/bin/env python3
from enum import Enum
#Let's assume thata the boat is relatively modern and produces 0.020Kg of CO2 emissiones
# per kilometer for the amount of pineapples that we are shipping.
emission = 0.020  #Kg of CO2 / Km
AMS_distance = 8943 #Amsterdam is 8943Km from PAN=Panama
print("Emissions caused by traveling from Panama to Amsterdam is:{}".format(emission * AMS_distance))

#============================
#hint:
# rows = 3
# cols = 4
# array_2d = [[0 for j in range(cols)] for i in range(rows)]

class City(Enum):
    PAN = 0
    AMS = 1
    CAS = 2
    NYC = 3
    HEL = 4
#destination ->  PAM,AMS,CAS,NYC,HEL
#  o   PAM
#  r   AMS         
#  i   CAS
#  g   NYC
#  i   HEL 
#  n   
#  
table = [[0,8943,8019,3652,10545],
         [8943,0,2619,6317,2078],
         [8019,2619,0,5836,4939],
         [3652,6317,5836,0,7825],
         [10545,2078,4939,7825,0]]

print(table)

#Input PAN,AMS,CAS,NYC,HEL
routes = [[City.PAN,City.AMS,City.CAS,City.NYC,City.HEL],
         [City.PAN,City.NYC,City.CAS,City.AMS,City.HEL],
         [City.PAN,City.NYC,City.AMS,City.CAS,City.HEL]]

for route in routes:
    print("Route:{}".format(route)) 
    totalDistance = 0
    for origin in range( len(route) - 1 ):
        destination = origin + 1
        partialDistance = table[route[origin].value][route[destination].value]
        print(partialDistance) 
        totalDistance += partialDistance
    print("total distance = {}".format(totalDistance))
    print("Total emission of CO2 = {}".format(totalDistance * emission))








