import util
import numpy as np

def main():
    lines = util.get_input(24).splitlines()
    grid = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
    up_wind = np.zeros_like(grid)
    down_wind = np.zeros_like(grid)
    left_wind = np.zeros_like(grid)
    right_wind = np.zeros_like(grid)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                grid[i, j] = 1
            elif c == "^":
                up_wind[i, j] = 1
            elif c == "v":
                down_wind[i, j] = 1
            elif c == "<":
                left_wind[i, j] = 1
            elif c == ">":
                right_wind[i, j] = 1

    start_pos = np.array([0, 0])
    end_pos = np.array([len(lines) - 1, 0])
    while True:
        if grid[start_pos[0], start_pos[1]] == 0:
            break
        start_pos[1] += 1

    while True:
        if grid[end_pos[0], end_pos[1]] == 0:
            break
        end_pos[1] += 1


    end_pos = tuple(end_pos)

    person_pos = set()
    person_pos.add(tuple(start_pos))
    counter = 0

    while True:
        up_wind[1:-1, 1:-1] = np.roll(up_wind[1:-1, 1:-1], -1, axis=0)
        down_wind[1:-1, 1:-1] = np.roll(down_wind[1:-1, 1:-1], 1, axis=0)
        left_wind[1:-1, 1:-1] = np.roll(left_wind[1:-1, 1:-1], -1, axis=1)
        right_wind[1:-1, 1:-1] = np.roll(right_wind[1:-1, 1:-1], 1, axis=1)

        new_pos = set()
        for pos in person_pos:
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                if pos[0] + offset[0] < 0 or pos[0] + offset[0] >= grid.shape[0]:
                    continue
                if grid[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if up_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if down_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if left_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if right_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                new_pos.add(tuple(np.array(pos) + np.array(offset)))

        counter += 1
        print(counter)

        if any(p == end_pos for p in new_pos):
            break

        person_pos = new_pos


def main2():
    lines = util.get_input(24).splitlines()
    grid = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
    up_wind = np.zeros_like(grid)
    down_wind = np.zeros_like(grid)
    left_wind = np.zeros_like(grid)
    right_wind = np.zeros_like(grid)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                grid[i, j] = 1
            elif c == "^":
                up_wind[i, j] = 1
            elif c == "v":
                down_wind[i, j] = 1
            elif c == "<":
                left_wind[i, j] = 1
            elif c == ">":
                right_wind[i, j] = 1

    start_pos = np.array([0, 0])
    end_pos = np.array([len(lines) - 1, 0])
    while True:
        if grid[start_pos[0], start_pos[1]] == 0:
            break
        start_pos[1] += 1

    while True:
        if grid[end_pos[0], end_pos[1]] == 0:
            break
        end_pos[1] += 1

    start_pos = tuple(start_pos)
    end_pos = tuple(end_pos)

    person_pos = set()
    person_pos.add(start_pos)
    counter = 0

    while True:
        up_wind[1:-1, 1:-1] = np.roll(up_wind[1:-1, 1:-1], -1, axis=0)
        down_wind[1:-1, 1:-1] = np.roll(down_wind[1:-1, 1:-1], 1, axis=0)
        left_wind[1:-1, 1:-1] = np.roll(left_wind[1:-1, 1:-1], -1, axis=1)
        right_wind[1:-1, 1:-1] = np.roll(right_wind[1:-1, 1:-1], 1, axis=1)

        new_pos = set()
        for pos in person_pos:
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                if pos[0] + offset[0] < 0 or pos[0] + offset[0] >= grid.shape[0]:
                    continue
                if grid[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if up_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if down_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if left_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if right_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                new_pos.add(tuple(np.array(pos) + np.array(offset)))

        counter += 1
        print(counter)

        if any(p == end_pos for p in new_pos):
            break

        person_pos = new_pos

    person_pos = set()
    person_pos.add(end_pos)

    while True:
        up_wind[1:-1, 1:-1] = np.roll(up_wind[1:-1, 1:-1], -1, axis=0)
        down_wind[1:-1, 1:-1] = np.roll(down_wind[1:-1, 1:-1], 1, axis=0)
        left_wind[1:-1, 1:-1] = np.roll(left_wind[1:-1, 1:-1], -1, axis=1)
        right_wind[1:-1, 1:-1] = np.roll(right_wind[1:-1, 1:-1], 1, axis=1)

        new_pos = set()
        for pos in person_pos:
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                if pos[0] + offset[0] < 0 or pos[0] + offset[0] >= grid.shape[0]:
                    continue
                if grid[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if up_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if down_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if left_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if right_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                new_pos.add(tuple(np.array(pos) + np.array(offset)))

        counter += 1
        print(counter)

        if any(p == start_pos for p in new_pos):
            break

        person_pos = new_pos

    person_pos = set()
    person_pos.add(start_pos)

    while True:
        up_wind[1:-1, 1:-1] = np.roll(up_wind[1:-1, 1:-1], -1, axis=0)
        down_wind[1:-1, 1:-1] = np.roll(down_wind[1:-1, 1:-1], 1, axis=0)
        left_wind[1:-1, 1:-1] = np.roll(left_wind[1:-1, 1:-1], -1, axis=1)
        right_wind[1:-1, 1:-1] = np.roll(right_wind[1:-1, 1:-1], 1, axis=1)

        new_pos = set()
        for pos in person_pos:
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                if pos[0] + offset[0] < 0 or pos[0] + offset[0] >= grid.shape[0]:
                    continue
                if grid[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if up_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if down_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if left_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                if right_wind[pos[0] + offset[0], pos[1] + offset[1]] == 1:
                    continue
                new_pos.add(tuple(np.array(pos) + np.array(offset)))

        counter += 1
        print(counter)

        if any(p == end_pos for p in new_pos):
            break

        person_pos = new_pos

    print(counter)


if __name__ == "__main__":
    main2()