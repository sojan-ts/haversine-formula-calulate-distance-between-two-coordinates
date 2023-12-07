
import math

def haversine_distance(coord1: tuple, coord2: tuple):
    lon1, lat1 = coord1
    lon2, lat2 = coord2

    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c 
    km = meters / 1000.0

    meters = round(meters, 3)
    km = round(km, 3)
    miles = km * 0.621371
    print(f"Distance: {meters} m")
    print(f"Distance: {km} km")
    print(f"Distance: {miles} miles")
 

if __name__ == "__main__":
    lat1 = 9.5845068
    lon1 = 76.5222935
    lat2 = 9.5845178
    lon2 = 76.5222887
    
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)
    print("Distance between", coord1, "and" , coord2, ":")
    haversine_distance(coord1, coord2)