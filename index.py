
airports = [
	 {
		 "start": 'ISB',
		 "end": 'LHR',
		 "cost": 1000
	 },
	 {
		 "start": 'LHR',
		 "end": 'NYC',
		 "cost": 750
	 },
	 {
		 "start": 'CBS',
		 "end": 'NYC',
		 "cost": 775
	 },
	 {
		 "start": 'ISB',
		 "end": 'CBS',
		 "cost": 575
	 },
	 {
		 "start": 'CBS',
		 "end": 'GRC',
		 "cost": 731
	 },
	 {
		 "start": 'NYC',
		 "end": 'GRC',
		 "cost": 459
	 }
 ]

""" 
    I have written a Python Script, That is used to find the cheapest path from starting city to destination city.
    I wrote a outer function named find_cheapest_path, which takes three parameters, a list of airports, 
    starting_point, and ending_point.
    I have written another function inside the outer function named all_possible_paths, which also takes three
    parameters current, path, and visited_airports. Basically inner function is a recursive function that 
    finds all possible path from starting to destination point and their cost.
"""

def find_cheapest_path(airports, start, end):
    def all_possible_paths(current, path, visited_airports):
        visited_airports.add(current) # I am storing the visted airports to avoid re-visting the airport during the search.

        if current == end: # If current == end, its mean path is found.
            paths.append(path.copy()) # paths is a list of lists that store the indexes of possible path.
            costs.append(sum(airports[i]['cost'] for i in path)) # Store the cost of possible path.
            visited_airports.remove(current) # When current == end comes, we get one of the possible path so we don't need to store current in visited_airports set that we have already stored.
            return

        for i, airport in enumerate(airports): # I am looping over the given airports' list.
            if airport['start'] == current and i not in visited_airports: # I am checking starting point of each dictionary from airport item and if current is equal and index of 'i' not present in visted_airports then go down
                all_possible_paths(airport['end'], path + [i], visited_airports) # call the recursive function to find the all posible path from start to end.

    paths = [] # 'paths' is a list of all possible 'path'. 'path' is also a list which stores the index of all airports that come in given root.
    costs = [] # 'costs' is a list that stores the cost of each possible path.
    visited_airports = set() # 'visited_airports' is a set which is used to store the visited airports index.
    path = [] # 'path' is a list which stores the index of all airports, which come in given root.

    all_possible_paths(start, path, visited_airports) # I am calling the all_possible_paths function inside find_cheapest_path function.

    if not paths:
        return None  # If not any path exists

    min_cost_index = costs.index(min(costs)) # Extracts the index of item from costs list of lowest value.
    min_cost_path = paths[min_cost_index] # Extracts the root or path from the paths list on the bases of lowest cost index.

    cheapest_path = [airports[i]['start'] for i in min_cost_path] + [end] #  I get the starting point of dictionary present in airports list, on the bases of index stored min_cost_path and then add the destination city the end.

    return  cheapest_path, min(costs) # Return the list of cheapest path and its cost.

start_point = 'ISB'
end_point = 'NYC'

result = find_cheapest_path(airports, start_point, end_point)

if result:
    path, cost = result
    print(f"The cheapest path from {start_point} to {end_point} is: {path}")
    print(f"The cost of {path} is: {cost}")
else:
    print(f"No possible path found from {start_point} to {end_point}")