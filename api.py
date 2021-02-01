import requests

api_url_base = 'https://api-v3.mbta.com/'
headers = {'Content-Type': 'application/json'}

def getRouteNames():
	arg = 'routes?filter[type]=0,1'
	resp = requests.get(api_url_base+arg, headers=headers)
	if resp.status_code == 200:
		return resp
	print('Error: getRouteNames API endpoint', resp.status_code)

def getTripIds(route_id):
	arg = 'trips?include=stops&filter[route]=' + route_id
	resp = requests.get(api_url_base+arg, headers=headers)
	if resp.status_code == 200:
		return resp
	print('Error: getRouteNames API endpoint', resp.status_code)

def getSchedule(stop_id, date):
	arg = 'schedules?filter[date]=' + date + '&filter[stop]=' + stop_id
	resp = requests.get(api_url_base+arg, headers=headers)
	if resp.status_code == 200:
		return resp
	print('Error: getRouteNames API endpoint', resp.status_code)

