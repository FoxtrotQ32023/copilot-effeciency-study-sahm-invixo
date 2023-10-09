import geopy.distance

def ass01_main():
    # Load input file into list
    with open("Assignment01/airlinehub.in") as inputFile:
        lines = [line.rstrip() for line in inputFile]

    # Split list into sets
    airport_sets = []
    for line in lines:
        if not "." in line:
            airport_sets.append([])
        else:
            airport_sets[len(airport_sets) - 1].append(line)

    # For each set identify the airport with the shortest distance to the other airports within the set
    best_hubs = []
    for airset in airport_sets:
        best_hubs.append( find_best_hub(airset) )

    return best_hubs

def find_best_hub(airport_set):
    # Loop through coordinates and calculate distance to all other airports in set
    shortest_distance = 9999999
    shortest_distance_ids = []
    for i, coord in enumerate(airport_set):
        other_coords = (airport_set[:i] + airport_set[i+1:])
        for other_coord in other_coords:
            distance = geopy.distance.geodesic(coord, other_coord).km
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_distance_ids = [i]
            elif distance == shortest_distance:
                shortest_distance_ids.append(i)

    # Best hub is the first of the identified shortest_distance_ids
    best_hub = airport_set[shortest_distance_ids[0]]

    # Ensure we have 2 digits on each coordinate
    coords = best_hub.split(" ")
    coord_one = '{0:.2f}'.format(float(coords[0]))
    coord_two = '{0:.2f}'.format(float(coords[1]))
    best_hub = " ".join([coord_one, coord_two])

    print(best_hub)
    return best_hub



if __name__ == "__main__":
    ass01_main()
