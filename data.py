import api
import pandas as pd
import time

# Perform API request for MBTA Routes of type 0,1
# Print long_name of each route
# Return list of ids for routes to be used in other API requests
def routeIdList():
	response = api.getRouteNames()
	
	json_resp = response.json()
	resp_data = json_resp["data"]
	
	route_id_list = []
	print('\n')
	print("MBTA Train Routes:")
	for data in resp_data:
		id = data['id']
		name = data['attributes']['long_name']
		route_id_list.append(id)
		print(name)
	print('\n')
	# return list of route ids to be used in other queries
	return route_id_list

def routeIDtoStopIdMap(route_id_list):
	
	route_id_to_stop_id_map = {}
	print("MBTA Stops:")
	for route_id in route_id_list:

		response = api.getTripIds(route_id)
		json_resp = response.json()
		resp_data = json_resp["data"]

		trip_id_list = []
		stop_id_list = []

		for data in resp_data:
			trip_id = data['id']
			trip_id_list.append(trip_id)
			for stop in data['relationships']['stops']['data']:
				stop_id = stop['id']
				if stop_id not in stop_id_list:
					stop_id_list.append(stop_id)
		route_id_to_stop_id_map[route_id] = sorted(stop_id_list)

	# return map of route ids to trip id , to be used in other queries
	return route_id_to_stop_id_map

def tripIDtoScheduleMap(stop_id, date):

	response = api.getSchedule(stop_id, date)
	json_resp = response.json()

	resp_data = json_resp["data"]

	tripIdToArrivalTimeAndRouteAndDirection = {}
	#print('Stop ID', stop_id)
	for data in resp_data:
		arrival_time = ''
		if data['attributes']['arrival_time'] == None:
			arrival_time = data['attributes']['departure_time'][:-6]
		else:
			arrival_time = data['attributes']['arrival_time'][:-6]
		# arrival_time = time.strptime(arrival_time, '%Y-%m-%dT%H:%M:%S')
		# departure_time = time.strptime(departure_time, '%Y-%m-%dT%H:%M:%S')
		trip_id = data['relationships']['trip']['data']['id']
		tripIdToArrivalTimeAndRouteAndDirection[trip_id] = [arrival_time, data['relationships']['route']['data']['id'], data['attributes']['direction_id']]
		#print(data['relationships']['trip']['data']['id'], 'time', arrival_time)

	return tripIdToArrivalTimeAndRouteAndDirection

def findBusiestHours(tripIdToScheduleMap):

	busiest_hours_schedule = {}
	counts = [0] * 24
	for trip_id in tripIdToScheduleMap:
		hour = int(tripIdToScheduleMap[trip_id][0][11:13])
		counts[hour] += 1

	max_consec_two_hours_start_index = 0

	for i in range(1, 23):
		if counts[max_consec_two_hours_start_index] + counts[max_consec_two_hours_start_index+1] < counts[i] + counts[i+1]:
			max_consec_two_hours_start_index = i

	for trip_id in tripIdToScheduleMap:
		hour = int(tripIdToScheduleMap[trip_id][0][11:13])
		if hour == max_consec_two_hours_start_index or max_consec_two_hours_start_index+1 == hour:
			busiest_hours_schedule[trip_id] = tripIdToScheduleMap[trip_id]

	print('Busiest Hours are', max_consec_two_hours_start_index, max_consec_two_hours_start_index+1, '\n')

	return busiest_hours_schedule







