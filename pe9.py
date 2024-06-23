import random

def generate_path(N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly. Exceptions for TypeError 
    # and KeyError are handled.

    maze = {(i, j): 0 for i in range(N) for j in range(M)}
    
    # Generate a random path
    path = [(0, 0)]
    current_pos = (0, 0)
    while current_pos != (N-1, M-1):
        possible_moves = []
        if current_pos[0] < N-1:
            possible_moves.append((current_pos[0]+1, current_pos[1]))
        if current_pos[1] < M-1:
            possible_moves.append((current_pos[0], current_pos[1]+1))
        move = random.choice(possible_moves)
        path.append(move)
        current_pos = move
    # Mark the path cells as 2
    for cell in path:
        maze[cell] = 2
    
    return maze


def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

     # Calculate the maximum number of obstacles that can be placed
    max_obstacles = N * M - 1  # Exclude the starting cell from the count

    if min_obstacles > max_obstacles:
        raise ValueError("The minimum number of obstacles is greater than the maximum possible.")

    obstacles_added = 0

    while obstacles_added < min_obstacles:
        row = random.randint(0, N - 1)
        col = random.randint(0, M - 1)

        if maze[(row, col)] == 0:
            maze[(row, col)] = 1
            obstacles_added += 1

    print(f"Added {obstacles_added} obstacles.")

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    try:
        row = int(input("Enter the row coordinate: "))
        col = int(input("Enter the column coordinate: "))

        if row < 0 or row >= N or col < 0 or col >= M:
            raise KeyError("Coordinates are out of bounds.")

        if maze[(row, col)] == 2:
            print("Error: Cannot set obstacle on a path cell.")
        elif maze[(row, col)] == 1:
            print("Error: Obstacle is already present in the cell.")
        else:
            maze[(row, col)] = 1
            print("Obstacle set successfully.")
    except ValueError:
        print("Error: Invalid coordinates. Please enter integers.")
    except KeyError:
        print("Error: Invalid coordinates. Please enter valid row and column values.")


def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    try:
        row = int(input("Enter the row coordinate of the cell: "))
        col = int(input("Enter the column coordinate of the cell: "))
        
        if row < 0 or row >= N or col < 0 or col >= M:
            raise ValueError("Invalid coordinates. Please enter valid coordinates within the maze.")
        
        if maze[(row, col)] == 2:
            raise ValueError("Cannot remove obstacle from a cell that is part of the path.")
        
        maze[(row, col)] = 0
        print("Obstacle removed successfully.")
    except ValueError as e:
        print("Error:", str(e))


def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells. If a KeyError occurs while trying to access a cell, it is 
    # caught and a message is printed.

    try:
        for i in range(N):
            for j in range(M):
                cell = maze[(i, j)]
                if cell == 0:
                    print(" ", end=" ")
                elif cell == 1:
                    print("X", end=" ")
                elif cell == 2:
                    print("O", end=" ")
            print()
    except KeyError:
        print("Error: Invalid maze configuration. Please check the maze blueprint file.")


def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    while True:
        try:
            filename = input("Enter the maze blueprint file name: ")
            maze_file = open(filename, 'r')

            maze = {}
            N = 0
            M = 0

            for line in maze_file:
                line = line.strip()
                if line:
                    row_cells = line.split("|")
                    if not M:
                        M = len(row_cells)
                    for col, cell in enumerate(row_cells):
                        if cell.strip() == "":
                            maze[(N, col)] = 0  # Empty cell
                        else:
                            maze[(N, col)] = 1  # Obstacle cell
                    N += 1

            min_obstacles = int(input("Enter the minimum number of obstacles(0-55): "))
            print_maze(maze,N,M)
            #add_obstacles(maze, min_obstacles, N, M)

            while True:
                print("\nMenu:")
                print("1. Set obstacle")
                print("2. Remove obstacle")
                print("3. Print maze")
                print("4. Exit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    set_obstacle(maze, N, M)
                elif choice == '2':
                    remove_obstacle(maze, N, M)
                elif choice == '3':
                    print_maze(maze, N, M)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a valid menu option.")

            maze_file.close()
            break
        except IOError:
            print("IOError occured in main function.File not found.Please enter a valid file.")
        except ValueError as e:
            print("Error:", str(e))
        except NameError as e:
            print("Error:", str(e))
        except KeyError:
            print("Error: Invalid maze blueprint file.")
        except Exception as e:
            print("An error occurred:", str(e))
main()
