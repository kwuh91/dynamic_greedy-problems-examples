# найти минимальный набор станций, который бы покрывал все 50 штатов?
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}  # set

stations = {}
stations["kone"] = {"id", "nv", "ut"}  # set
stations["ktwo"] = {"wa", "id", "mt"}  # set
stations["kthree"] = {"or", "nv", "ca"}  # set
stations["kfour"] = {"nv", "ut"}  # set
stations["kfive"] = {"ca", "az"}  # set

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states & states_needed
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
