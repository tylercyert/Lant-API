DIRECTIONS = ["N", "E", "S", "W"]

def turn(current_dir, turn_right=True):
    idx = DIRECTIONS.index(current_dir)
    return DIRECTIONS[(idx + (1 if turn_right else -1)) % 4]

def move_forward(x: int, y: int, direction: str) -> tuple[int, int]:
    if direction == "N":
        return x, y - 1
    elif direction == "S":
        return x, y + 1
    elif direction == "E":
        return x + 1, y
    elif direction == "W":
        return x - 1, y
    else:
        raise ValueError(f"Invalid direction: {direction}")


def step(x, y, direction, cell_color):
    if cell_color == 0:
        new_dir = turn(direction, turn_right=True)
        new_color = 1
    else:
        new_dir = turn(direction, turn_right=False)
        new_color = 0

    new_x, new_y = move_forward(x, y, new_dir)

    return {
        "x": new_x,
        "y": new_y,
        "dir": new_dir,
        "new_color": new_color
    }
