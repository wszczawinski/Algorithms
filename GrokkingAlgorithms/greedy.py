states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

print(f"States needed: {states_needed} \n")

stations = {}
stations["k-one"] = set(["id", "nv", "ut"])
stations["k-two"] = set(["wa", "id", "mt"])
stations["k-three"] = set(["or", "nv", "ca"])
stations["k-four"] = set(["nv", "ut"])
stations["k-five"] = set(["ca", "az"])

print(f"Stations: {stations} \n")

final_stations = set()

while states_needed:
    best_solution = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_solution = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_solution)


print(f"Final stations: {final_stations} \n")
