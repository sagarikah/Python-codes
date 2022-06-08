import math

def getFare(source, destination):
    distance= 0
    
    if source in bus_stops and destination in bus_stops:
        for i in range(len(bus_stops)):
            if bus_stops[i] == source:
                src_pos= i

        for j in range(len(bus_stops)):
            if bus_stops[j] == destination:
                dest_pos= j
        
        if src_pos < dest_pos:
            temp_pos= src_pos+1
            while temp_pos <= dest_pos:
                distance += path[temp_pos]
                temp_pos += 1

            fare= math.ceil((distance/1000) * 5)
            return fare

        elif src_pos > dest_pos:
            if src_pos < len(bus_stops)-1:
                temp_pos= src_pos + 1

                while temp_pos <= len(bus_stops)-1:
                    distance += path[temp_pos]
                    temp_pos += 1

            temp_pos= 0
            while temp_pos <= dest_pos:
                distance += path[temp_pos]
                temp_pos += 1

            fare= math.ceil((distance/1000) * 5)
            return fare

        else:
            distance= 0
            fare= 0
            return fare

    else:
        return False
    

bus_stops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI","CA"]
path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]

source= input("Enter source: ")
destination= input("Enter destination: ")

fare= getFare(source, destination)

if fare:
    print("Bus fare= ",str(fare) + " INR")
else:
    print("Invalid input")

