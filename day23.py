import util
import numpy as np

def main():
    lines = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".splitlines()
    lines = util.get_input(23).splitlines()
    grid = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                grid[i, j] = 1

    directions = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])

    clockwise = np.array([[0, 1], [-1, 0]])
    counter_clockwise = np.array([[0, -1], [1, 0]])

    old_grid = np.zeros_like(grid)
    counter  = 0
    past_grids = []

    while not np.array_equal(grid, old_grid):
        counter += 1
        print(counter)
        old_grid = grid.copy()
        if (grid[:, 0] == 1).any():
            grid = np.pad(grid, ((0, 0), (1, 0)))
        if (grid[:, -1] == 1).any():
            grid = np.pad(grid, ((0, 0), (0, 1)))
        if (grid[0, :] == 1).any():
            grid = np.pad(grid, ((1, 0), (0, 0)))
        if (grid[-1, :] == 1).any():
            grid = np.pad(grid, ((0, 1), (0, 0)))

        moving = np.zeros_like(grid)
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i, j] == 1:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if x == 0 and y == 0:
                                continue
                            if grid[i + x, j + y] == 1:
                                moving[i, j] = 1
                                break
                        if moving[i, j] == 1:
                            break

        moving_index = np.where(moving == 1)
        moving_directions = []
        for i, j in zip(moving_index[0], moving_index[1]):
            for d in directions:
                forward = grid[i + d[0], j + d[1]]
                d_left = d + counter_clockwise @ d
                left = grid[i + d_left[0], j + d_left[1]]
                d_right = d + clockwise @ d
                right = grid[i + d_right[0], j + d_right[1]]
                if not any([forward, left, right]):
                    moving_directions.append((i, j, d))
                    break

        for i, j, d in moving_directions:
            end_pos = (i + d[0], j + d[1])
            if not any((i2 + d2[0], j2 + d2[1]) == end_pos for i2, j2, d2 in moving_directions if (i2, j2) != (i, j)):
                grid[i, j] = 0
                grid[end_pos] = 1

        if (grid[:, 0] == 1).any():
            grid = np.pad(grid, ((0, 0), (1, 0)))
        if (grid[:, -1] == 1).any():
            grid = np.pad(grid, ((0, 0), (0, 1)))
        if (grid[0, :] == 1).any():
            grid = np.pad(grid, ((1, 0), (0, 0)))
        if (grid[-1, :] == 1).any():
            grid = np.pad(grid, ((0, 1), (0, 0)))


        directions = np.roll(directions, -1, axis=0)
        if any(np.array_equal(grid, g) for g in past_grids):
            print('repeated')

        past_grids.append(grid.copy())

    while (grid[:, 0] == 0).all():
        grid = grid[:, 1:]
    while (grid[:, -1] == 0).all():
        grid = grid[:, :-1]
    while (grid[0, :] == 0).all():
        grid = grid[1:, :]
    while (grid[-1, :] == 0).all():
        grid = grid[:-1, :]

    print(counter)
    display(grid)





def display(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

if __name__ == '__main__':
    main()