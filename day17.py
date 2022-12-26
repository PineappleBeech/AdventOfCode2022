import itertools

import util

shapes = [((0,0), (1,0), (2,0), (3,0)),             # Horizontal line
          ((1,0), (0,1), (1,1), (2,1), (1,2)),      # Plus
          ((0,0), (1,0), (2,0), (2,1), (2,2)),      # L
          ((0,0), (0,1), (0,2), (0,3)),             # Vertical line
          ((0,0), (1,0), (0,1), (1,1))]             # Square


def main():
    wind = util.get_input(17)[:-1]
    #wind = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    wind_index = 0
    rocks = {(x, 0) for x in range(7)}

    i = 0
    while i < 2022:
        shape = shapes[i % len(shapes)]

        shape = move(shape, (2, max_height_total(rocks) + 4))
        shape_start = shape

        shape, wind_index = move_wind(shape, wind, wind_index, rocks)

        while all(s not in rocks for s in move(shape, (0, -1))):
            shape = move(shape, (0, -1))

            shape, wind_index = move_wind(shape, wind, wind_index, rocks)

        rocks = rocks.union(set(shape))

        if False:
            for y in range(max_height_total(rocks) + 1, -1, -1):
                for x in range(7):
                    if (x, y) in rocks:
                        print("#", end="")
                    else:
                        print(".", end="")

                print()
            print()


        i += 1

    print(max_height_total(rocks))

def max_height(column, rocks):
    return max([y for x, y in rocks if x == column], default=0)

def max_height_total(rocks):
    return max([y for x, y in rocks], default=0)

def move(shape, offset):
    return [(x + offset[0], y + offset[1]) for x, y in shape]

def try_move(shape, offset, rocks):
    after = move(shape, offset)
    if any(x < 0 or x > 6 for x, y in after):
        return shape
    if any((x, y) in rocks for x, y in after):
        return shape
    return after

def move_wind(shape, wind, wind_index, rocks):
    if wind[wind_index] == ">":
        return try_move(shape, (1, 0), rocks), (wind_index + 1) % len(wind)
    elif wind[wind_index] == "<":
        return try_move(shape, (-1, 0), rocks), (wind_index + 1) % len(wind)

def main2():
    wind = util.get_input(17)[:-1]
    wind = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    wind_index = 0
    rocks = {(x, 0) for x in range(7)}
    #rocks = leaky_set(1000, rocks)
    one_cycle = len(wind) * len(shapes)
    shape_gen = itertools.cycle(shapes)

    rock_sets = []
    rocks_fallen_per_cycle = []
    heights = []
    old_rocks = rocks.copy()
    recent_rocks = rocks.copy()

    rocks_fallen = 0

    while True:
        counter = 0
        while True:
            old_index = wind_index
            rocks, wind_index = drop_rock(rocks, shape_gen, wind, wind_index)
            rocks_fallen += 1
            counter += 1
            if wind_index < old_index:
                break
            continue
            counter += 1
            if counter % 1000 == 0:
                print(counter)
                rocks.update(recent_rocks)
                m = [max_height(x, rocks) for x in range(7)]
                recent_rocks = {r for r in recent_rocks if r[1] > m[r[0]] - 150}
                print(len(recent_rocks))

        rock_sets.append((frozenset(normalize(rocks - old_rocks)), wind_index, rocks_fallen % 5))
        rocks_fallen_per_cycle.append(rocks_fallen)
        heights.append(max_height_total(rocks))
        old_rocks = rocks.copy()

        if rock_sets[-1] in rock_sets[:-1]:
            break

        print("Keep going")

    cycles = len(rock_sets) - rock_sets[:-1].index(rock_sets[-1]) - 1 # how many cycles are in the pattern
    height_per_cycle = heights[-1] - heights[-cycles - 1] # how much the height increases per cycle

    one_cycle = rocks_fallen_per_cycle[-1] - rocks_fallen_per_cycle[-1-cycles] # how many rocks are dropped in one cycle

    print(cycles)
    print(height_per_cycle)

    print(counter)
    print(rocks_fallen)

    count_left = 1000000000000 - rocks_fallen

    cycles_needed = count_left // (one_cycle)

    rocks_fallen += cycles_needed * one_cycle

    while rocks_fallen < 1000000000000:
        rocks, wind_index = drop_rock(rocks, shape_gen, wind, wind_index)
        rocks_fallen += 1

    print(max_height_total(rocks) + height_per_cycle * cycles_needed)


def drop_rock(rocks, shape_gen, wind, wind_index):
    shape = next(shape_gen)

    shape = move(shape, (2, max_height_total(rocks) + 4))

    shape, wind_index = move_wind(shape, wind, wind_index, rocks)

    while all(s not in rocks for s in move(shape, (0, -1))):
        shape = move(shape, (0, -1))

        shape, wind_index = move_wind(shape, wind, wind_index, rocks)

    rocks = rocks.union(set(shape))

    return rocks, wind_index


def normalize(rocks):
    min_y = min(y for x, y in rocks)
    return {(x, y - min_y) for x, y in rocks}


def print_top(rocks):
    for y in range(max_height_total(rocks) + 1, max_height_total(rocks) - 10, -1):
        for x in range(7):
            if (x, y) in rocks:
                print("#", end="")
            else:
                print(".", end="")

        print()
    print()


if __name__ == "__main__":
    main2()