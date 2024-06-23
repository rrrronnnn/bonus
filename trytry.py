import random
import os

def read_maze_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
        N = (len(lines) ) // 2  # 行數
        M = (len(lines[0]) + 1) // 4  # 列數

    maze = {}
    for i in range(N):
        for j in range(M):
            if lines[2 * i + 1][4 * j + 1] == 'X':
                maze[(i, j)] = 1
            else:
                maze[(i, j)] = 0

    return maze, N, M

def generate_maze(maze, N, M):
    path = [(0, 0)]
    i, j = 0, 0

    while i < N - 1 or j < M - 1:
        if i == N - 1:
            j += 1
        elif j == M - 1:
            i += 1
        else:
            if random.choice([True, False]):
                i += 1
            else:
                j += 1
        path.append((i, j))

    for cell in path:
        maze[cell] = 2

    return maze

def add_obstacles(maze, min_obstacles, N, M):
    obstacles_added = 0
    while obstacles_added < min_obstacles:
        i, j = random.randint(0, N-1), random.randint(0, M-1)
        if maze[(i, j)] == 0:
            maze[(i, j)] = 1
            obstacles_added += 1

def set_obstacle(maze, N, M):
    try:
        x, y = map(int, input("輸入要設置障礙物的坐標 (x, y): ").split())
        if (x, y) not in maze:
            raise IndexError
        if maze[(x, y)] == 2:
            print("錯誤：不能在路徑上設置障礙物。")
        else:
            maze[(x, y)] = 1
    except (ValueError, IndexError):
        print("錯誤：無效的坐標。")

def remove_obstacle(maze, N, M):
    try:
        x, y = map(int, input("輸入要移除障礙物的坐標 (x, y): ").split())
        if (x, y) not in maze:
            raise IndexError
        if maze[(x, y)] == 2:
            print("錯誤：不能移除路徑。")
        else:
            maze[(x, y)] = 0
    except (ValueError, IndexError):
        print("錯誤：無效的坐標。")

def print_maze(maze, N, M):
    for i in range(N):
        # Print top border of each row
        print("+---" * M + "+")
        for j in range(M):
            if maze[(i, j)] == 0:
                print("|   ", end='')
            elif maze[(i, j)] == 1:
                print("| X ", end='')
            elif maze[(i, j)] == 2:
                print("| O ", end='')
        print("|")  # End of row border
    # Print bottom border of the last row
    print("+---" * M + "+")

def main():
    while True:
        filename = input("輸入迷宮文件名 (例如，grid77.txt 或 grid99.txt): ")
        if os.path.exists(filename):
            break
        else:
            print("錯誤：文件未找到。請輸入有效的文件名。")

    maze, N, M = read_maze_file(filename)
    maze = generate_maze(maze, N, M)
    print_maze(maze, N, M)
    while True:
        try:
            min_obstacles = int(input(f"輸入要添加的最小障礙物數量 (0-{N*M}): "))
            if 0 <= min_obstacles <= N * M:
                break
            else:
                raise ValueError
        except ValueError:
            print("錯誤：請輸入有效的數字。")

    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)

    while True:
        print("\n菜單:")
        print("1. 設置障礙物")
        print("2. 移除障礙物")
        print("3. 打印迷宮")
        print("4. 退出")
        choice = input("輸入你的選擇: ")

        if choice == '1':
            set_obstacle(maze, N, M)
        elif choice == '2':
            remove_obstacle(maze, N, M)
        elif choice == '3':
            print_maze(maze, N, M)
        elif choice == '4':
            break
        else:
            print("錯誤：無效的選擇。")

if __name__ == "__main__":
    main()