'''
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''

# Islands consist of - connected components
# connected - neighbors (edges)
# directions, NSEW (edges)
# 2d array - graph more or less
# returns (shape of solution) - number of islands

# Offset coordinates?

# How can we find the extent of an island?
# Either of our traversals to find all of the nodes in an island

# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1



'''
"Borrowed" from Rosie DS8 THANKS ROSIE!
'''

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def check_islands(islands):
    island_check = [[False for x in range(len(islands[y]))] for y in range(len(islands))]
    all_islands = []

    for y in range(len(islands)):
        for x in range(len(islands[y])):
            if not island_check[y][x] and islands[y][x] == 1:
                current_group = [[x, y]]
                i = 0
                while i < len(current_group):
                    x_current = current_group[i][0]
                    y_current = current_group[i][1]
                    island_check[y_current][x_current] = True
                    if x_current > 0:
                        if islands[y_current][x_current-1] == 1 and not island_check[y_current][x_current-1]:
                            current_group.append([x_current-1, y_current])
                    if x_current < len(islands[y_current])-1:
                        if islands[y_current][x_current+1] == 1 and not island_check[y_current][x_current+1]:
                            current_group.append([x_current+1, y_current])
                    if y_current > 0:
                        if islands[y_current-1][x_current] == 1 and not island_check[y_current-1][x_current]:
                            current_group.append([x_current, y_current-1])
                    if y_current < len(islands)-1:
                        if islands[y_current+1][x_current] == 1 and not island_check[y_current+1][x_current]:
                            current_group.append([x_current, y_current+1])   
                    i += 1
                all_islands.append(current_group)
    return all_islands
            

                    
            
print(check_islands(islands))


'''
Borrowed from Dave Vazquez. THANKS DAVE!
'''


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def island_counter(islands):
    num_islands = 0
    # iterate through the islands
    for y in range(0, len(islands)):
        for x in range(0, len(islands[y])):
            # if the island-node is part of an island and hasn't been visited
            if islands[y][x] == 1:
                # you've found an island, so increment
                num_islands += 1
                # BFT through the island-node's neighbors
                islands = visit_neighbors(x, y, islands)
    return num_islands


def visit_neighbors(x, y, islands):
    # NORTH
    if y > 0:  # if not at northern edge
        # and neighbor is an island-node
        if islands[y-1][x] == 1:
            # mark it visited by updating value to 0
            islands[y-1][x] = 0
            # and visit all it's neighbors
            islands = visit_neighbors(x, y-1, islands)

    # SOUTH
    if y < 4:
        if islands[y+1][x] == 1:
            islands[y+1][x] = 0
            islands = visit_neighbors(x, y+1, islands)

    # EAST
    if x < 4:
        if islands[y][x+1] == 1:
            islands[y][x+1] = 0
            islands = visit_neighbors(x+1, y, islands)

    # WEST
    if x > 0:
        if islands[y][x-1] == 1:
            islands[y][x-1] = 0
            islands = visit_neighbors(x-1, y, islands)

    return islands


result = island_counter(islands)

print(result)