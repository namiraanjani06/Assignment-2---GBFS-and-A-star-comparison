import heapq
import random

# Directions for movement (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Manhattan distance heuristic
def manhattan_heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search Algorithm
def a_star(grid, start, end):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f, node)
    g_costs = {start: 0}  # g(n) cost (distance from start)
    f_costs = {start: manhattan_heuristic(start, end)}  # f(n) = g(n) + h(n)
    came_from = {}  # To reconstruct the path

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == end:
            # Reconstruct the path from start to end
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for direction in DIRECTIONS:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            # Check if the neighbor is within bounds and not an obstacle
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g_costs[current] + 1  # g(n) = g(current) + 1 (since each move costs 1)

                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    f_cost = tentative_g + manhattan_heuristic(neighbor, end)
                    f_costs[neighbor] = f_cost
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None  # No path found

# Function to generate a random grid with obstacles
def generate_grid(size, num_obstacles):
    grid = [[0 for _ in range(size)] for _ in range(size)]  # 0 represents free space, 1 represents obstacle
    obstacles = 0
    while obstacles < num_obstacles:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if grid[x][y] == 0:  # Make sure it's empty
            grid[x][y] = 1  # Place obstacle
            obstacles += 1
    return grid

# Main function to run the A* algorithm
def run_a_star_algorithm(grid_size, num_obstacles, start, end):
    grid = generate_grid(grid_size, num_obstacles)
    
    print(f"Running A* Search...")
    a_star_path = a_star(grid, start, end)
    
    if a_star_path:
        print("A* Path found:", a_star_path)
    else:
        print("No path found using A*.")

# Example grid size (70x70 grid), obstacles (10), start and end points
grid_size = 70  # 70x70 grid (approx 5000 nodes)
num_obstacles = 10
start = (0, 0)
end = (69, 69)

run_a_star_algorithm(grid_size, num_obstacles, start, end)
