import curses
import random
import time

# Constants for the game
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
INITIAL_SNAKE_LENGTH = 5
SNAKE_HEAD = 's'
SNAKE_FIRST_BODY = 'n'
SNAKE_MIDDLE_BODY = 'a'
SNAKE_LAST_BODY = 'k'
SNAKE_TAIL = 'e'
OBSTACLE = '▓'

KEYS = {
    curses.KEY_UP: (0, -1),
    curses.KEY_DOWN: (0, 1),
    curses.KEY_LEFT: (-1, 0),
    curses.KEY_RIGHT: (1, 0)
}

def create_food(snake, obstacles, screen_height, screen_width):
    while True:
        food = (random.randint(1, screen_width - 2), random.randint(1, screen_height - 2))
        if food not in snake and food not in obstacles:
            return food

def create_obstacles(screen_height, screen_width):
    obstacles = set()
    num_obstacles = (screen_height * screen_width) // 20
    while len(obstacles) < num_obstacles:
        length = random.randint(5, 10)
        if random.choice([True, False]):  # Horizontal or Vertical
            x = random.randint(1, screen_width - length - 1)
            y = random.randint(1, screen_height - 2)
            for i in range(length):
                obstacles.add((x + i, y))
        else:
            x = random.randint(1, screen_width - 2)
            y = random.randint(1, screen_height - length - 1)
            for i in range(length):
                obstacles.add((x, y + i))
    return obstacles

def main(stdscr):
    direction = KEYS[curses.KEY_RIGHT]
    curses.curs_set(0)
    stdscr.nodelay(1)
    initial_speed = 150  # 0.15 seconds
    slow_speed = 300   # 0.3 seconds
    stdscr.timeout(initial_speed)

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal food
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Special food
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Obstacles

    screen_height, screen_width = stdscr.getmaxyx()
    
    # Initialize snake in the middle of the screen
    snake = [(screen_width // 2 + i, screen_height // 2) for i in range(INITIAL_SNAKE_LENGTH)]
    direction = KEYS[curses.KEY_RIGHT]
    
    # Create obstacles ensuring they do not overlap with the initial snake position
    obstacles = create_obstacles(screen_height, screen_width)
    while any(segment in obstacles for segment in snake):
        obstacles = create_obstacles(screen_height, screen_width)
    
    normal_food = create_food(snake, obstacles, screen_height, screen_width)
    special_food = create_food(snake, obstacles, screen_height, screen_width)
    
    normal_food_eaten = 0
    special_food_eaten = 0
    pause = False
    start_time = time.time()

    while True:
        stdscr.clear()
        
        for y, x in obstacles:
            stdscr.addch(x, y, OBSTACLE, curses.color_pair(4))

        for i, (y, x) in enumerate(snake):
            if i == 0:
                stdscr.addstr(x, y, SNAKE_HEAD, curses.color_pair(3))
            elif i == 1:
                stdscr.addstr(x, y, SNAKE_FIRST_BODY, curses.color_pair(3))
            elif i == len(snake) - 1:
                stdscr.addstr(x, y, SNAKE_TAIL, curses.color_pair(3))
            elif i == len(snake) - 2:
                stdscr.addstr(x, y, SNAKE_LAST_BODY, curses.color_pair(3))
            else:
                stdscr.addstr(x, y, SNAKE_MIDDLE_BODY, curses.color_pair(3))

        stdscr.addch(normal_food[1], normal_food[0], NORMAL_FOOD, curses.color_pair(1))
        stdscr.addch(special_food[1], special_food[0], SPECIAL_FOOD, curses.color_pair(2))

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord(' '):
            pause = not pause

        if pause:
            continue

        if key in KEYS:
            direction = KEYS[key]

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Wrap around the screen boundaries
        new_head = (new_head[0] % screen_width, new_head[1] % screen_height)

        # Game over conditions
        if new_head in snake or new_head in obstacles:
            break

        snake.insert(0, new_head)

        if new_head == normal_food:
            normal_food_eaten += 1
            normal_food = create_food(snake, obstacles, screen_height, screen_width)
        elif new_head == special_food:
            special_food_eaten += 1
            special_food = create_food(snake, obstacles, screen_height, screen_width)
            if len(snake) > 1:
                snake.pop()
        else:
            snake.pop()

        # Adjust speed after 2 seconds
        if time.time() - start_time < 2:
            stdscr.timeout(initial_speed)
        else:
            stdscr.timeout(slow_speed)

    stdscr.clear()
    stdscr.addstr(screen_height // 2, screen_width // 2 - 10, "Game Over!")
    stdscr.addstr(screen_height // 2 + 1, screen_width // 2 - 10, f"Normal food eaten: {normal_food_eaten}")
    stdscr.addstr(screen_height // 2 + 2, screen_width // 2 - 10, f"Special food eaten: {special_food_eaten}")
    stdscr.refresh()
    stdscr.nodelay(0)
    stdscr.getch()

curses.wrapper(main)
