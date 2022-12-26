import util

import numpy as np

directions = np.array([[1, 0, 0],
                       [-1, 0, 0],
                       [0, 1, 0],
                       [0, -1, 0],
                       [0, 0, 1],
                       [0, 0, -1],])

def main():
    lines = util.get_input(18).splitlines()
    cubes = [list(map(int, i.split(","))) for i in lines]
    maximum = max(max(i) for i in cubes)
    grid = np.zeros((maximum+2, maximum+2, maximum+2), dtype=np.int8)
    total = len(cubes) * 6
    for x, y, z in cubes:
        grid[x, y, z] = 1

    for x,y,z in cubes:
        for d in directions:
            if 0 <= x+d[0] < grid.shape[0] and 0 <= y+d[1] < grid.shape[1] and 0 <= z+d[2] < grid.shape[2]:
                if grid[x+d[0], y+d[1], z+d[2]] == 1:
                    total -= 1

    print(total)


def main2():
    lines = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''.splitlines()
    lines = util.get_input(18).splitlines()
    cubes = [list(map(lambda x: int(x) + 1, i.split(","))) for i in lines]
    maximum = max(max(i) for i in cubes)
    grid = np.zeros((maximum+2, maximum+2, maximum+2), dtype=np.int8)
    total = 0

    for x, y, z in cubes:
        grid[x, y, z] = 1

    old_grid = np.copy(grid)

    # 2 is exterior
    grid[0, :, :] = 2
    grid[-1, :, :] = 2
    grid[:, 0, :] = 2
    grid[:, -1, :] = 2
    grid[:, :, 0] = 2
    grid[:, :, -1] = 2

    count = 1

    while count != 0:
        count = 0

        for x, y, z in np.argwhere(grid == 2):
            for d in directions:
                if 0 <= x+d[0] < grid.shape[0] and 0 <= y+d[1] < grid.shape[1] and 0 <= z+d[2] < grid.shape[2]:
                    if grid[x+d[0], y+d[1], z+d[2]] == 0:
                        grid[x+d[0], y+d[1], z+d[2]] = 2
                        count += 1

    for x,y,z in cubes:
        for d in directions:
            if 0 <= x+d[0] < grid.shape[0] and 0 <= y+d[1] < grid.shape[1] and 0 <= z+d[2] < grid.shape[2]:
                if grid[x+d[0], y+d[1], z+d[2]] == 2:
                    total += 1

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            for z in range(grid.shape[2]):
                print(grid[x,y,z], end="")

            print()

        print()

    print(total)


if __name__ == "__main__":
    #main()
    main2()