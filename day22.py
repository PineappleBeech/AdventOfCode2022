import util
import numpy as np
import re

clockwise = np.array([[0, 1], [-1, 0]], dtype=np.int32)
counter_clockwise = np.array([[0, -1], [1, 0]], dtype=np.int32)
edges = [((0, 1, 2), (2, 0, 2)),
         ((0, 1, 3), (3, 0, 2)),
         ((0, 2, 3), (3, 0, 1)),
         ((0, 2, 0), (2, 1, 0)),
         ((0, 2, 1), (1, 1, 0)),
         ((1, 1, 2), (2, 0, 3)),
         ((2, 1, 1), (3, 0, 0))]

# 0,1 red
# 0,2 blue
# 1,1 yellow
# 2,1 orange
# 2,0 green
# 3,0 white

edges2 = [((0, 2, 2), (1, 1, 3)),
          ((0, 2, 3), (1, 0, 3)),
          ((0, 2, 0), (2, 3, 0)),
          ((1, 0, 2), (2, 3, 1)),
          ((1, 0, 1), (2, 2, 1)),
          ((1, 1, 1), (2, 2, 2)),
          ((1, 2, 0), (2, 3, 3))]
edges = edges + [(i[1], i[0]) for i in edges]
edges2 = edges2 + [(i[1], i[0]) for i in edges2]

def main():
    lines = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".splitlines()
    lines = util.get_input(22).splitlines()
    instructions = lines[-1]
    lines = lines[:-2]
    grid = np.zeros((len(lines)+2, max(len(x) for x in lines)+2), dtype=np.int8)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                grid[i+1, j+1] = 1
            elif c == '.':
                grid[i+1, j+1] = 2

    pos = np.ones(2, dtype=np.int32)
    direction = np.array([0, 1], dtype=np.int32)
    while grid[pos[0]][pos[1]] != 2:
        pos[1] += 1

    distance = re.match(r"(\d+)", instructions).group(1)
    instructions = instructions[len(distance):]
    distance = int(distance)
    pos = move(pos, distance, direction, grid)
    rotations = 0
    while len(instructions) > 0:
        if instructions[0] == 'L':
            direction = np.matmul(counter_clockwise, direction)
            rotations -= 1
        elif instructions[0] == 'R':
            direction = np.matmul(clockwise, direction)
            rotations += 1
        else:
            print("Error: invalid instruction")
        instructions = instructions[1:]
        distance = re.match(r"(\d+)", instructions).group(1)
        instructions = instructions[len(distance):]
        distance = int(distance)
        pos = move(pos, distance, direction, grid)
        continue
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                if x == pos[1] and y == pos[0]:
                    print("X", end="")
                elif grid[y][x] == 1:
                    print("#", end='')
                elif grid[y][x] == 2:
                    print(".", end='')
                elif grid[y][x] == 0:
                    print(" ", end='')
            print()
        print(pos)
        _ = 0

    print(pos)
    num = pos[0] * 1000 + pos[1] * 4 + (rotations % 4)
    print(num)

def move(pos, distance, direction, grid):
    for i in range(distance):
        new_pos = pos + direction
        if grid[new_pos[0]][new_pos[1]] == 1:
            break
        elif grid[new_pos[0]][new_pos[1]] == 0:
            search_pos = np.copy(pos)
            while grid[search_pos[0]][search_pos[1]] != 0:
                search_pos -= direction
            search_pos += direction
            if grid[search_pos[0]][search_pos[1]] == 1:
                break
            else:
                pos = search_pos
        else:
            pos = new_pos
    return pos

def main2():
    lines = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".splitlines()
    lines = util.get_input(22).splitlines()
    instructions = lines[-1]
    lines = lines[:-2]
    grid = np.zeros((len(lines)+2, max(len(x) for x in lines)+2), dtype=np.int8)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                grid[i+1, j+1] = 1
            elif c == '.':
                grid[i+1, j+1] = 2

    visited = np.copy(grid)

    pos = np.ones(2, dtype=np.int32)
    direction = np.array([0, 1], dtype=np.int32)
    while grid[pos[0]][pos[1]] != 2:
        pos[1] += 1

    distance = re.match(r"(\d+)", instructions).group(1)
    instructions = instructions[len(distance):]
    distance = int(distance)
    pos, direction = move2(pos, distance, direction, grid, visited)
    while len(instructions) > 0:
        if instructions[0] == 'L':
            direction = np.matmul(counter_clockwise, direction)
        elif instructions[0] == 'R':
            direction = np.matmul(clockwise, direction)
        else:
            print("Error: invalid instruction")
        instructions = instructions[1:]
        distance = re.match(r"(\d+)", instructions).group(1)
        instructions = instructions[len(distance):]
        distance = int(distance)
        old_direction = np.copy(direction)
        pos, direction = move2(pos, distance, direction, grid, visited)
        continue
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                if x == pos[1] and y == pos[0]:
                    print("X", end="")
                elif grid[y][x] == 1:
                    print("#", end='')
                elif grid[y][x] == 2:
                    print(".", end='')
                elif grid[y][x] == 0:
                    print(" ", end='')
                else:
                    print("?", end='')
            print()
        print(pos)
        _ = 0

    print(pos)
    assert np.array_equal(old_direction, direction)
    num = pos[0] * 1000 + pos[1] * 4 + to_rotation(old_direction)
    print(num)
    #display2(visited)

def move2(pos, distance, direction, grid, visited):
    n = 50
    for i in range(distance):
        visited[pos[0]][pos[1]] = to_rotation(direction) + 4
        new_pos = pos + direction
        if grid[new_pos[0]][new_pos[1]] == 1:
            break
        elif grid[new_pos[0]][new_pos[1]] == 0:
            p = pos - np.array([1, 1])
            p = p // n
            old_direction = np.copy(direction)
            for edge_pair in edges:
                if edge_pair[0][0] == p[0] and edge_pair[0][1] == p[1] and edge_pair[0][2] == to_rotation(direction):
                    edge = edge_pair
                    break
            else:
                print("Error: no edge found")

            rot_diff = (edge[1][2] - to_rotation(direction) + 2) % 4
            for i in range(rot_diff):
                direction = clockwise @ direction

            p = (pos - np.array([1, 1])) % n

            if to_rotation(old_direction) == 0:
                pos_on_edge = p[0]
            elif to_rotation(old_direction) == 1:
                pos_on_edge = n - 1 - p[1]
            elif to_rotation(old_direction) == 2:
                pos_on_edge = n - 1 - p[0]
            elif to_rotation(old_direction) == 3:
                pos_on_edge = p[1]

            #print(f"From {pos} in direction {to_rotation(old_direction)}")

            new_pos = np.array([1, 1]) + np.array([edge[1][0], edge[1][1]]) * n

            if to_rotation(direction) == 0:
                new_pos[0] += pos_on_edge
            elif to_rotation(direction) == 1:
                new_pos[1] += n - 1 - pos_on_edge
            elif to_rotation(direction) == 2:
                new_pos[0] += n - 1 - pos_on_edge
                new_pos[1] += n - 1
            elif to_rotation(direction) == 3:
                new_pos[1] += pos_on_edge
                new_pos[0] += n - 1

            #print(f"To {new_pos} in direction {to_rotation(direction)}")
            #print()
            if grid[new_pos[0]][new_pos[1]] == 1:
                direction = old_direction
                break
            else:
                pos = new_pos

        else:
            pos = new_pos

    return pos, direction

def test2():
    lines = util.get_input(22).splitlines()
    lines = lines[:-2]
    grid = np.zeros((len(lines)+2, max(len(x) for x in lines)+2), dtype=np.int8)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                grid[i+1, j+1] = 2
            elif c == '.':
                grid[i+1, j+1] = 2
    grid[10, 51] = 1

    visited = np.copy(grid)

    pos, direction = move2(np.array([10,110]), 195, np.array([0, 1]), grid, visited)
    print(pos)
    print(direction)
    '''
    for start in [np.array([10,60]),
                  np.array([10,110]),
                  np.array([60,60]),
                  np.array([110,60]),
                  np.array([110,10]),
                  np.array([160,10])]:
        for start_direction in [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]:
            pos, direction = move2(start, 200, start_direction, grid, visited)
            assert pos[0] == start[0] and pos[1] == start[1]
            assert np.array_equal(direction, start_direction)
            '''
    display2(visited)


def to_rotation(direction):
    if direction[1] == 1:
        return 0
    elif direction[1] == -1:
        return 2
    elif direction[0] == 1:
        return 1
    elif direction[0] == -1:
        return 3
    else:
        print("Error: invalid direction")
        return 0

def is_edge(pos, grid):
    counter = 0
    if grid[pos[0]][pos[1]] == 0:
        return False

    for offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if grid[pos[0] + offset[0]][pos[1] + offset[1]] == 0:
            counter += 1

    return counter == 1

def display(pos, grid):
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if x == pos[1] and y == pos[0]:
                print("X", end="")
            elif grid[y][x] == 1:
                print("#", end='')
            elif grid[y][x] == 2:
                print(".", end='')
            elif grid[y][x] == 0:
                print(" ", end='')
            else:
                print("?", end='')
        print()
    print(pos)

def display2(grid):
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y][x] == 1:
                print("#", end='')
            elif grid[y][x] == 2:
                print(".", end='')
            elif grid[y][x] == 0:
                print(" ", end='')
            elif grid[y][x] == 4:
                print(">", end='')
            elif grid[y][x] == 5:
                print("v", end='')
            elif grid[y][x] == 6:
                print("<", end='')
            elif grid[y][x] == 7:
                print("^", end='')
            else:
                print("?", end='')
        print()

def main3():
    lines = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5""".splitlines()
    lines = util.get_input(22).splitlines()
    instructions = lines[-1]
    lines = lines[:-2]
    grid = np.zeros((len(lines), max(len(x) for x in lines)), dtype=np.int8)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                grid[i+1, j+1] = 1
            elif c == '.':
                grid[i+1, j+1] = 2

    faces = [grid[0:50, 50:100],
             grid[0:50, 100:150],
             grid[50:100, 50:100],
             grid[100:150, 50:100],
             grid[100:150, 0:50],
             grid[150:200, 0:50]]

    grid2 = np.zeros((52, 52, 52), dtype=np.int8)
    grid2[1:51, 1:51, 0]

    pos = np.ones(2, dtype=np.int32)
    direction = np.array([0, 1], dtype=np.int32)
    while grid[pos[0]][pos[1]] != 2:
        pos[1] += 1

    distance = re.match(r"(\d+)", instructions).group(1)
    instructions = instructions[len(distance):]
    distance = int(distance)
    pos, direction = move2(pos, distance, direction, grid)
    while len(instructions) > 0:
        if instructions[0] == 'L':
            direction = np.matmul(counter_clockwise, direction)
        elif instructions[0] == 'R':
            direction = np.matmul(clockwise, direction)
        else:
            print("Error: invalid instruction")
        instructions = instructions[1:]
        distance = re.match(r"(\d+)", instructions).group(1)
        instructions = instructions[len(distance):]
        distance = int(distance)
        old_direction = np.copy(direction)
        pos, direction = move2(pos, distance, direction, grid)
        continue
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                if x == pos[1] and y == pos[0]:
                    print("X", end="")
                elif grid[y][x] == 1:
                    print("#", end='')
                elif grid[y][x] == 2:
                    print(".", end='')
                elif grid[y][x] == 0:
                    print(" ", end='')
                else:
                    print("?", end='')
            print()
        print(pos)
        _ = 0

    print(pos)
    num = pos[0] * 1000 + pos[1] * 4 + to_rotation(old_direction)
    print(num)
    display2(visited)

def move3(pos, distance, direction, grid):
    n = 50
    for i in range(distance):
        new_pos = pos + direction
        if not in_bounds(new_pos, grid) or grid[new_pos[0]][new_pos[1]] == 0:
            p = pos - np.array([1, 1])
            p = p // n
            old_direction = np.copy(direction)
            for edge_pair in edges:
                if edge_pair[0][0] == p[0] and edge_pair[0][1] == p[1] and edge_pair[0][2] == to_rotation(direction):
                    edge = edge_pair
                    break
            else:
                print("Error: no edge found")

            rot_diff = (edge[1][2] - to_rotation(direction) + 2) % 4
            for i in range(rot_diff):
                direction = clockwise @ direction

            p = (pos - np.array([1, 1])) % n

            if to_rotation(old_direction) == 0:
                pos_on_edge = p[0]
            elif to_rotation(old_direction) == 1:
                pos_on_edge = n - 1 - p[1]
            elif to_rotation(old_direction) == 2:
                pos_on_edge = n - 1 - p[0]
            elif to_rotation(old_direction) == 3:
                pos_on_edge = p[1]

            print(f"From {pos} in direction {to_rotation(old_direction)}")

            new_pos = np.array([1, 1]) + np.array([edge[1][0], edge[1][1]]) * n

            if to_rotation(direction) == 0:
                new_pos[0] += pos_on_edge
            elif to_rotation(direction) == 1:
                new_pos[1] += n - 1 - pos_on_edge
            elif to_rotation(direction) == 2:
                new_pos[0] += n - 1 - pos_on_edge
                new_pos[1] += n - 1
            elif to_rotation(direction) == 3:
                new_pos[1] += pos_on_edge
                new_pos[0] += n - 1

            print(f"To {new_pos} in direction {to_rotation(direction)}")
            print()
            if grid[new_pos[0]][new_pos[1]] == 1:
                break
            else:
                pos = new_pos

        elif grid[new_pos[0]][new_pos[1]] == 1:
            break

        else:
            pos = new_pos

    return pos, direction

def in_bounds(pos, grid):
    return pos[0] >= 0 and pos[0] < grid.shape[0] and pos[1] >= 0 and pos[1] < grid.shape[1]

if __name__ == '__main__':
    main2()