def find_stations_within_distance(mrt_map, orig, dist):
    """returns a list that contains all the stations that can be reached from the station orig within dist
stops. Order of the stations in the returned list doesn’t matter"""
    final_list = []
    # For directly linked stations (same line)
    for each_line in mrt_map:           # iterate through the diff mrt lines
        if orig in each_line:
            index_of_orig = each_line.index(orig)         # find index of orig in each_line
            for each_station in each_line:
                index_of_station = each_line.index(each_station)   # find index of station
                if abs(index_of_station - index_of_orig) == dist or abs(index_of_station - index_of_orig) < dist:
                    if each_station != orig:              # add all except ownself
                        final_list.append(each_station)
    # For indirectly linked stations(on diff lines)--> Find common stations(Newton, Little India)
    initial_distance = 0
    if 'Little India' in final_list:
        # Find dist between orig and Little India
        for each_line in mrt_map:
            if orig in each_line and 'Little India' in each_line:
                index_of_common_station = each_line.index('Little India')
                index_of_initial_station = each_line.index(orig)
                initial_distance += abs(index_of_common_station-index_of_initial_station)
        # To get stations from another line that is within dist
            if 'Little India' in each_line:
                for each_station in each_line:
                    index_of_station = each_line.index(each_station)
                    index_of_common_station = each_line.index('Little India')
                    if each_station not in final_list:             # To prevent repeated items
                        if each_station != orig:                   # If not initial station
                            if abs(index_of_common_station-index_of_station) < dist-initial_distance:
                                final_list.append(each_station)
    # For Newton line onwards (red line)
    if 'Newton' in final_list:
        for each_line in mrt_map:
            if 'Newton' in each_line:
                index_of_common_station = each_line.index('Newton')
                for each_station in each_line:
                    index_of_station = each_line.index(each_station)
                    if abs(index_of_station-index_of_common_station) < dist-initial_distance:
                        if each_station not in final_list:
                            final_list.append(each_station)
    return final_list

#print(find_stations_within_distance([['Botanic Gardens', 'Stevens', 'Newton', 'Little India', 'Rochor'],
#['Newton', 'Novena', 'Toa Payoh', 'Braddell', 'Bishan'],
#['Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng']], 'Botanic Gardens', 2))
#print(find_stations_within_distance([['Botanic Gardens', 'Stevens', 'Newton', 'Little India', 'Rochor'],
#['Newton', 'Novena', 'Toa Payoh', 'Braddell', 'Bishan'],
#['Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng']], 'Little India', 1))
print(find_stations_within_distance([['Botanic Gardens', 'Stevens', 'Newton', 'Little India', 'Rochor'],
['Newton', 'Novena', 'Toa Payoh', 'Braddell', 'Bishan'],
['Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng']], 'Dhoby Ghaut', 3))