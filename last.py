import curses
import random

# Constants for the game
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
OBSTACLE = '#'
INITIAL_SNAKE_LENGTH = 3
SNAKE_BODY = '*'
SNAKE_HEAD = '@'
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
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(150)

    screen_height, screen_width = stdscr.getmaxyx()
    snake = [(screen_width // 2 + i, screen_height // 2) for i in range(INITIAL_SNAKE_LENGTH)]
    direction = KEYS[curses.KEY_RIGHT]
    normal_food = create_food(snake, set(), screen_height, screen_width)
    special_food = create_food(snake, set(), screen_height, screen_width)
    obstacles = create_obstacles(screen_height, screen_width)
    
    normal_food_eaten = 0
    special_food_eaten = 0
    pause = False

    while True:
        stdscr.clear()
        
        for y, x in obstacles:
            stdscr.addch(x, y, OBSTACLE, curses.A_REVERSE)

        for y, x in snake:
            stdscr.addch(x, y, SNAKE_BODY)
        stdscr.addch(snake[0][1], snake[0][0], SNAKE_HEAD)

        stdscr.addch(normal_food[1], normal_food[0], NORMAL_FOOD)
        stdscr.addch(special_food[1], special_food[0], SPECIAL_FOOD)

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

    stdscr.clear()
    stdscr.addstr(screen_height // 2, screen_width // 2 - 10, "Game Over!")
    stdscr.addstr(screen_height // 2 + 1, screen_width // 2 - 10, f"Normal food eaten: {normal_food_eaten}")
    stdscr.addstr(screen_height // 2 + 2, screen_width // 2 - 10, f"Special food eaten: {special_food_eaten}")
    stdscr.refresh()
    stdscr.nodelay(0)
    stdscr.getch()

curses.wrapper(main)
