# Function for detecting adjacent mines
def adjacent_mine_count(mine_grid, row, col):

    # Define adjacent directions relative to the cell in question, there are 8
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    # Determine the dimentions of the grid (A are rows and B are columns)
    A = len(mine_grid)
    B = len(mine_grid)

    # Initialise counter
    mine_count = 0

    # Iterate through every direction
    for dx, dy in directions:                                              # Loop goes through each pair (dx, dy)
        x, y = row + dx, col + dy                                          # x and y are calculated coordinates of adjecent cell (x = row + dx, y = col + dy)
        if 0 <= x < A and 0 <= y < B and mine_grid[x][y] == "#":           # Check if the adjacent cell is within bounds and contains a mine
            mine_count += 1                                                # Increment count by one if mine is found in an adjacent cell
    return mine_count                                                      # Total mines after looping 8 directions


# Function for returning grid with replaced "-" for the number of adjacent mines
def reveal_mine_grid(mine_grid):

    # Determine the dimentions of the grid (A are rows and B are columns)
    A = len(mine_grid)
    B = len(mine_grid)

    # Initialise final grid
    revealed_mine_grid = []

    # Iterated through each cell in the grid
    for row in range(A):                                                    # First loop goes therough rows
        new_row = []                                                        # Initialised for each row to store the transformed cells
        for col in range(B):                                                # Second loop goes through columns
            if mine_grid[row][col] == "#":                                  # If mine ("#") detected
                new_row.append("#")                                         # Add "#" to the cell
            else:                                                           
                mine_count = adjacent_mine_count(mine_grid, row, col)       # Count adjacent mines for non-mine cells
                new_row.append(mine_count)                                  # Add the adjacent cell mine count
        revealed_mine_grid.append(new_row)                                  # Add the transformed row to the new gride

    # Returned fully transformed grid
    return revealed_mine_grid                                               



# Example input grid
untransformed_grid = [["-", "#", "-", "#", "-"], 
                      ["-", "#", "#", "-", "#"], 
                      ["-", "-", "-", "#", "-"],
                      ["#", "-", "#", "-", "#"],
                      ["-", "#", "-", "-", "-"]]

# Generate output grid
transformed_grid = reveal_mine_grid(untransformed_grid)

# Print out resultant grid
for row in transformed_grid:
    print(row)