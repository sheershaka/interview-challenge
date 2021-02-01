import math
# Python variables
# Constants will be modified in the course of evaluating your solution.  Feel free to modify to extend your own evalutation.

# Sales function
A=2
B=10
def salesOverTime(t_seconds):
    return max(math.floor(A*math.atan(t_seconds/B)),0)

# Scenario
CARS_PER_TRAIN      =  8
T_bw_SameLineCars   = 10    # seconds to move between cars on the same line (same train or different train of same color in same direction)
T_bw_DifferentLine  = 45    # seconds to move between cars of trains that are either on different lines (color) or different directions of the same line.

T_duration = 60 # in api arrival time and separture time are the same so I'm assuming each train will stay T_duration seconds at the station

def max_seconds_per_car():
	return math.ceil(math.tan(1.5)*B)

# can be modified in the next version
# right now it doesn't take cars in each train into consideration
def getMaxProfitFromTrain(time_to_switch):
	return salesOverTime(time_to_switch)

def print_results(n_salesmen, result_times, result_sale, total_sale):
	for n in range(min(CARS_PER_TRAIN, n_salesmen)):
		print('\nSale made for the station by salesman ', n+1)
		for i in result_sale.keys():
			print(i, ': ',result_times[i], ', #',result_sale[i])
		print('Total Sold #', total_sale)
