###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    sorted_cows = [(cow, cows[cow]) for cow in sorted(cows, key = cows.get, reverse=True)]
    #print(sorted_cows)
    result_trips = []
    
    cowsLeft = len(sorted_cows)
    cowsUsed = []
    totalWeight = 0
    while cowsLeft > 0:
        tripWeight = 0
        trip = []
        for cow in sorted_cows:
            if cow not in cowsUsed:
                #print("trying to add {}...".format(cow))
                if (tripWeight + cow[1] <= limit):
                    trip.append(cow[0])
                    cowsUsed.append(cow)
                    cowsLeft -= 1
                    #print("{} added".format(cow))
                    tripWeight += cow[1]
                    #print("total weight of the trip is {}".format(tripWeight))        
        result_trips.append(trip)
        totalWeight += tripWeight
    #print(available_cows)
    #totalWeight += tripWeight              
    #print("total weight shipped is: {}".format(totalWeight))
    return (result_trips, len(result_trips))
            
cows = load_cows('ps1_cow_data.txt')
#test = greedy_cow_transport(cows, limit=10)
#print(test)



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result_trips = []
    
    for partition in get_partitions(cows):
        in_limit = True
        trips = len(partition)
        for trip in partition:
            weight = 0
            for cow in trip:
                weight += cows[cow]   
            if weight > limit:
                in_limit = False
                break
        if in_limit == True:
            if trips < len(result_trips) or len(result_trips) == 0:
                result_trips = partition
                
    return (result_trips, len(result_trips))

#cows = load_cows('ps1_cow_data.txt')
#test = brute_force_cow_transport(cows, limit=10)
#print(test)
    


   
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start_1 = time.time()
    result, trip_no = greedy_cow_transport(cows, limit=10)
    end_1 = time.time()
    print("Greedy time:")
    print(end_1 - start_1)
    print("Greedy result, number of trips:")
    print(result, trip_no)

    start_2 = time.time()
    result, trip_no = brute_force_cow_transport(cows, limit=10)
    end_2 = time.time()
    print("Brute force time:")
    print(end_2 - start_1)
    print("Brute force result, number of trips:")
    print(result, trip_no)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
#print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()

