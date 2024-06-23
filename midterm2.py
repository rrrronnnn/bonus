import random

def generate_path(N, M):
    # Goal: Generate a maze with a clear path from the starting point to the bottom-right cell using a brute-force approach.
    # Detailed Instructions:
    # 1. Create a 2D list of zeros representing the maze map with dimensions N rows by M columns.
    # 2. Start at the top-left cell of the maze map and add it to the path list.
    # 3. While not at the bottom-right cell of the maze map:
    #     a. If at the bottom row of the maze map, move right.
    #     b. If at the rightmost column of the maze map, move down.
    #     c. Otherwise, randomly choose to move right or down.
    #     d. Mark the chosen cell as part of the path and add it to the path list.
    # 4. Mark the bottom-right cell of the maze map as part of the path and add it to the path list.
    # 5. Return the updated maze map with the path.
    
    maze = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        maze.append(row)

    # your code here

    maze[0][0]=2
    m=0
    n=0
    new_path=[]

    while True:
        choose=[]
        new_path.append([m,n])
        if m<N-2:
            choose.append([m+1,n])
        elif m==N-1 and n<M-1:
            choose.append([m,n+1])
        if n<M-1:
            choose.append([m,n+1])
        elif n==M-1 and m<N-1:
            choose.append([m+1,n])

        c=random.choice(choose)

        if c ==[m+1,n]:
            m+=1
            maze[m][n]=2
        elif c ==[m,n+1]:
            n+=1
            maze[m][n]=2
        if maze[N-1][M-1]==2:
            break


    return maze

def add_obstacles(maze, num_obstacles):
    # Goal: Add a number of obstacles randomly to the maze.
    # Detailed Instructions:
    # 1. While the number of obstacles in the maze is less than num_obstacles:
        # a. Choose a random cell in the maze that is not part of the path or already an obstacle.
        # b. Mark the cell as an obstacle.
    # 2. Return the updated maze map with the obstacles.

    # your code here
    count=0
    while True:
        a=random.randint(0,N-1)
        b=random.randint(0,M-1)
        if maze[a][b] ==0:
            maze[a][b]=1
            count+=1
        if count==num_obstacles:
            break


    return maze

def generate_maze(N, M, num_obstacles):
    # Goal: Generate a maze with a clear path from the starting point to the bottom-right cell and a number of obstacles using a brute-force approach.
    # Detailed Instructions:
    # 1. Call the generate_path function with the arguments N and M to generate a maze with a clear path.
    # 2. Call the add_obstacles function with the generated maze map and the argument num_obstacles to add a number of obstacles randomly to the maze.
    # 3. Return the updated maze map.


    # generate a maze with a clear path from the starting point to the bottom-right cell
    maze = generate_path(N, M)

    # add the number of obstacles randomly to the maze
    maze = add_obstacles(maze, num_obstacles)

    return maze



def print_maze(maze):
    # Goal: Print the maze map as a grid to the console using boundaries with "-", "|", and "+" symbols.
    # Detailed Instructions:
    # 1. For each row in the maze map:
    #   a. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them.
    #   b. For each cell in the row:
    #       If the cell is an obstacle, print an "X" symbol.
    #       Otherwise, print a space character.
    #   c. Print a vertical boundary line with "|" symbols at the ends.
    # 2. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them at the bottom of the maze map.
    
    print("+" + "---+" * len(maze[0]))
    for i in range(len(maze)):
        row_str = "|"
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                row_str += "   "
            elif maze[i][j] == 1:
                row_str += " 1 "
            elif maze[i][j] == 2:
                row_str += " 2 "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * len(maze[0]))

# prompt the user to input the values of N, M, and num_obstacles
N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N*M-(N+M-1)
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))

# generate the maze using the user-specified values
maze = generate_maze(N, M, num_obstacles)

# print the generated maze as a grid to the console
print("Generated Maze Map:")
print_maze(maze)
