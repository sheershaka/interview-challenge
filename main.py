import json
import pandas as pd
import api
import data
import sys
from datetime import datetime, timedelta
import time
import assumptions

curr_route_id = 'Red'
curr_stop_id = '70061'

def main(argv):
    
    dt = datetime.today()
    print("Date used to find the data", dt.strftime("%Y-%m-%d"))

    # Perform API request for MBTA Routes of type 0,1
    # Print long_name of each route
    # Return list of ids for routes to be used in other API requests
    routeIdList = data.routeIdList()
    routeIDtoStopIdMap = data.routeIDtoStopIdMap(routeIdList)
    #routeIDtoStopIdMap = {'Red': ['70061', '70063', '70064', '70065', '70066', '70067', '70068', '70069', '70070', '70071', '70072', '70073', '70074', '70075', '70076', '70077', '70078', '70079', '70080', '70081', '70082', '70083', '70084', '70085', '70086', '70087', '70088', '70089', '70090', '70091', '70092', '70093', '70094', '70095', '70096', '70097', '70098', '70099', '70100', '70101', '70102', '70103', '70104', '70105'], 'Mattapan': ['70261', '70263', '70264', '70265', '70266', '70267', '70268', '70269', '70270', '70271', '70272', '70273', '70274', '70275', '70276'], 'Orange': ['11531', '1222', '1258', '17861', '70001', '70002', '70003', '70004', '70005', '70006', '70007', '70008', '70009', '70010', '70011', '70012', '70013', '70014', '70015', '70016', '70017', '70018', '70019', '70020', '70021', '70022', '70023', '70024', '70025', '70026', '70027', '70028', '70029', '70030', '70031', '70032', '70033', '70034', '70035', '70036', '70278', '70279', '875', '9070002', '9070003', '9070004', '9070005', '9070007'], 'Green-B': ['70106', '70107', '70110', '70111', '70112', '70113', '70114', '70115', '70116', '70117', '70120', '70121', '70124', '70125', '70126', '70127', '70128', '70129', '70130', '70131', '70134', '70135', '70136', '70137', '70138', '70139', '70140', '70141', '70142', '70143', '70144', '70145', '70146', '70147', '70148', '70149', '70152', '70153', '70154', '70155', '70156', '70157', '70158', '70159', '70196', '70200', '70201', '70202', '70203', '70204', '70205', '70206', '71150', '71151', '71199'], 'Green-C': ['70150', '70151', '70152', '70153', '70154', '70155', '70156', '70157', '70158', '70159', '70197', '70200', '70201', '70202', '70203', '70204', '70205', '70206', '70211', '70212', '70213', '70214', '70215', '70216', '70217', '70218', '70219', '70220', '70223', '70224', '70225', '70226', '70227', '70228', '70229', '70230', '70231', '70232', '70233', '70234', '70235', '70236', '70237', '70238'], 'Green-D': ['70150', '70151', '70152', '70153', '70154', '70155', '70156', '70157', '70158', '70159', '70160', '70161', '70162', '70163', '70164', '70165', '70166', '70167', '70168', '70169', '70170', '70171', '70172', '70173', '70174', '70175', '70176', '70177', '70178', '70179', '70180', '70181', '70182', '70183', '70186', '70187', '70198', '70200', '70201', '70202', '70203', '70204', '70205', '70206'], 'Green-E': ['1415', '14155', '14159', '21458', '70154', '70155', '70156', '70157', '70158', '70159', '70199', '70200', '70201', '70202', '70203', '70204', '70205', '70206', '70239', '70240', '70241', '70242', '70243', '70244', '70245', '70246', '70247', '70248', '70249', '70250', '70251', '70252', '70253', '70254', '70255', '70256', '70257', '70258', '70260'], 'Blue': ['70038', '70039', '70040', '70041', '70042', '70043', '70044', '70045', '70046', '70047', '70048', '70049', '70050', '70051', '70052', '70053', '70054', '70055', '70056', '70057', '70058', '70059', '70060', '70838']}

    # ----- QUESTION ONE -----

    # TO PREPARE THE SCHEDULE LIST for a given stop ID and datetime string, do the following
    tripIdToArrivalTimeAndRouteAndDirectionMap = data.tripIDtoScheduleMap(routeIDtoStopIdMap['Red'][10], dt.strftime("%Y-%m-%d"))
    tripIdToBusiestHoursCoordinateMap = data.findBusiestHours(tripIdToArrivalTimeAndRouteAndDirectionMap)
    print(tripIdToBusiestHoursCoordinateMap)

    ## Do for all station (this throws 429 error because we are sending too many requests)
    # stopIDToBusiestHoursCoordinateMap = {}
    # for routeId in routeIdList:
    # 	for stopId in routeIDtoStopIdMap[routeId]:
    # 		tripIdToArrivalTimeAndRouteAndDirectionMap = data.tripIDtoScheduleMap(stopId, dt.strftime("%Y-%m-%d"))
    # 		tripIdToBusiestHoursCoordinateMap = data.findBusiestHours(tripIdToArrivalTimeAndRouteAndDirectionMap)
    # 		print(tripIdToBusiestHoursCoordinateMap)
    # 		stopIDToBusiestHoursCoordinateMap[stopId] = tripIdToBusiestHoursCoordinateMap



    #tripIdToBusiestHoursCoordinateMap = {'46180743': ['2021-01-31T07:08:00', 'Red', 1], '46180744': ['2021-01-31T07:23:00', 'Red', 1], '46180745': ['2021-01-31T07:37:00', 'Red', 1], '46180746': ['2021-01-31T07:51:00', 'Red', 1], '46180747': ['2021-01-31T08:06:00', 'Red', 1], '46180748': ['2021-01-31T08:20:00', 'Red', 1], '46180749': ['2021-01-31T08:34:00', 'Red', 1], '46180750': ['2021-01-31T08:49:00', 'Red', 1], '46180821': ['2021-01-31T07:00:00', 'Red', 0], '46180822': ['2021-01-31T07:14:00', 'Red', 0], '46180823': ['2021-01-31T07:28:00', 'Red', 0], '46180824': ['2021-01-31T07:43:00', 'Red', 0], '46180825': ['2021-01-31T07:57:00', 'Red', 0], '46180826': ['2021-01-31T08:12:00', 'Red', 0], '46180827': ['2021-01-31T08:26:00', 'Red', 0], '46180828': ['2021-01-31T08:40:00', 'Red', 0], '46180829': ['2021-01-31T08:54:00', 'Red', 0], '46180896': ['2021-01-31T07:02:00', 'Red', 1], '46180897': ['2021-01-31T07:16:00', 'Red', 1], '46180898': ['2021-01-31T07:31:00', 'Red', 1], '46180899': ['2021-01-31T07:45:00', 'Red', 1], '46180900': ['2021-01-31T07:59:00', 'Red', 1], '46180901': ['2021-01-31T08:14:00', 'Red', 1], '46180902': ['2021-01-31T08:28:00', 'Red', 1], '46180903': ['2021-01-31T08:42:00', 'Red', 1], '46180904': ['2021-01-31T08:57:00', 'Red', 1], '46180972': ['2021-01-31T07:07:00', 'Red', 0], '46180973': ['2021-01-31T07:21:00', 'Red', 0], '46180974': ['2021-01-31T07:36:00', 'Red', 0], '46180975': ['2021-01-31T07:50:00', 'Red', 0], '46180976': ['2021-01-31T08:04:00', 'Red', 0], '46180977': ['2021-01-31T08:19:00', 'Red', 0], '46180978': ['2021-01-31T08:33:00', 'Red', 0], '46180979': ['2021-01-31T08:47:00', 'Red', 0]}

    # ----- QUESTION TWO -----

    # create cordinate list for the stop id
    # cordinates = []
    arrival_times = {}
    times = []
    for trip_id in tripIdToBusiestHoursCoordinateMap.keys():
    	array = tripIdToBusiestHoursCoordinateMap[trip_id]
    	t = datetime.strptime(array[0], '%Y-%m-%dT%H:%M:%S')
    	tripIdToBusiestHoursCoordinateMap[trip_id][0] = t
    	arrival_times[t] = [trip_id, array[1], array[2]]
    	times.append(t)
    times.sort()

    min_time = times[0]
    result_times = {}
    result_sale = {}
    total_sale = 0
    for i in range(len(times)-1):
    	t = times[i]
    	t_end = t + timedelta(seconds=assumptions.T_duration)
    	t_next = times[i+1]

    	time_to_switch = (t_next - t_end).total_seconds()
    	total_time = (t_next - t).total_seconds()

    	key = arrival_times[t][1] + '-' + str(arrival_times[t][2])
    	next_key = arrival_times[t_next][1] + '-' + str(arrival_times[t_next][2])
    	sales = 0
    	if key == next_key:
    		if time_to_switch >= assumptions.T_bw_SameLineCars:
    			# have enough time to switch
    			sales = assumptions.getMaxProfitFromTrain(assumptions.T_duration)
    		else:
    			# dont have enought time to switch
    			sales = assumptions.getMaxProfitFromTrain(total_time-time_to_switch)
    			t_end = t_next-timedelta(seconds=assumptions.T_bw_SameLineCars)
    	else:
    		if time_to_switch >= assumptions.T_bw_DifferentLine:
    			# have enough time to switch
    			sales = assumptions.getMaxProfitFromTrain(assumptions.T_duration)
    		else:
    			# dont have enought time to switch
    			sales = assumptions.getMaxProfitFromTrain(total_time-time_to_switch)
    			t_end = t_next-timedelta(seconds=assumptions.T_bw_DifferentLine)
    	if key in result_sale:
    		result_sale[key]+=sales
    		result_times[key].append([t.strftime("%Y-%m-%dT%H:%M:%S"), t_end.strftime("%Y-%m-%dT%H:%M:%S")])
    	else:
    		result_sale[key]=sales
    		result_times[key] = [[t.strftime("%Y-%m-%dT%H:%M:%S"), t_end.strftime("%Y-%m-%dT%H:%M:%S")]]
    	total_sale+=sales

    assumptions.print_results(1, result_times, result_sale, total_sale)

    # ----- QUESTION THREE -----

    # Use the same method as question two since we are not changing the cars and he/she just go the the second car to make sale
    # Later on if we change the cars, then we send the second person with the delay of the seconds the first saleman stayed in the first car
    # this way they both can follow the same pattern without ever clashing.
    total_salesmen = 2
    assumptions.print_results(total_salesmen, result_times, result_sale, total_sale)


    # ----- QUESTION FOUR ------

    # Assuming arbitary n vendors = number of cars per train, then we can use the same function about, each saleman can sell in a different car and follow the train change pattern
    # Later on if we are changing cars, then calculate the subsequent delay caused by all the salemen that went before the present saleman. (but this is not the best solution)

    total_salesmen = 10
    assumptions.print_results(total_salesmen, result_times, result_sale, total_sale)


    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])
