#!/usr/bin/env python3
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1,5):
        for port3 in range(1,5):
            for port4 in range(1,5):
                for port5 in range(1,5):
                    route = [port1,port2,port3,port4,port5]
                    #statement to check if the route is valid
                    #if(True):
                    '''Option one
                    if(port1 != port2 and port1 != port3 and port1 != port4 and port1 != port5 and
                       port2 != port3 and port2 != port4 and port2 != port5 and 
                       port3 != port4 and port3 != port5 and
                       port4 != port5):
                    '''
                    '''
                    #Option two by course
                    #You don't really have to check that 0 is included. But it is good programming style to ensure
                    # that program works even if we modify it later.
                    if( 0 in route and 1 in route and 2 in route and 3 in route and 4 in route ):
                    '''
                    #Option three by course. It's is the much more elegant one
                    if set(route) == set(range(5)):
                        print(' '.join([portnames[i] for i in route]))


main()







