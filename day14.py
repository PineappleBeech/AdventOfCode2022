import util

def main():
    lines = util.get_input(14).splitlines()
    rocks_x = []
    rocks_y = []
    max_y = 0
    for line in lines:
        points = line.split(" -> ")
        for start, end in zip(points[:-1], points[1:]):
            start_x, start_y = map(int, start.split(","))
            end_x, end_y = map(int, end.split(","))
            max_y = max(max_y, start_y, end_y)
            if start_x == end_x:
                if start_y < end_y:
                    rocks_y.append((start_x, range(start_y, end_y+1)))
                else:
                    rocks_y.append((start_x, range(end_y, start_y+1)))
            elif start_y == end_y:
                if start_x < end_x:
                    rocks_x.append((start_y, range(start_x, end_x+1)))
                else:
                    rocks_x.append((start_y, range(end_x, start_x+1)))

    sands = []
    reached_abyss = False
    while not reached_abyss:
        sand = (500,0)
        while True:
            can_fall = False
            for new_pos in (sand[0], sand[1]+1), (sand[0]-1, sand[1]+1), (sand[0]+1, sand[1]+1):
                if check_pos(new_pos, rocks_x, rocks_y, sands):
                    sand = new_pos
                    can_fall = True
                    break
            if not can_fall:
                sands.append(sand)
                break
            if sand[1] == max_y:
                reached_abyss = True
                break
    print(len(sands))


def main2():
    lines = util.get_input(14).splitlines()
    rocks_x = []
    rocks_y = []
    max_y = 0
    for line in lines:
        points = line.split(" -> ")
        for start, end in zip(points[:-1], points[1:]):
            start_x, start_y = map(int, start.split(","))
            end_x, end_y = map(int, end.split(","))
            max_y = max(max_y, start_y, end_y)
            if start_x == end_x:
                if start_y < end_y:
                    rocks_y.append((start_x, range(start_y, end_y+1)))
                else:
                    rocks_y.append((start_x, range(end_y, start_y+1)))
            elif start_y == end_y:
                if start_x < end_x:
                    rocks_x.append((start_y, range(start_x, end_x+1)))
                else:
                    rocks_x.append((start_y, range(end_x, start_x+1)))
    rocks_x.append((max_y+2, range(-1000000, 1000000)))

    sands = []
    reached_abyss = False
    drop_sand((500,0), sands, rocks_x, rocks_y)
    print(len(sands))


def check_pos(pos, rocks_x, rocks_y, sands):
    for y, x in rocks_x:
        if pos[1] == y and pos[0] in x:
            return False
    for x, y in rocks_y:
        if pos[0] == x and pos[1] in y:
            return False
    if pos in sands:
        return False
    return True


def drop_sand(pos, sands, rocks_x, rocks_y):
    if pos in sands:
        return
    sands.append(pos)
    if check_pos((pos[0], pos[1]+1), rocks_x, rocks_y, []):
        drop_sand((pos[0], pos[1]+1), sands, rocks_x, rocks_y)
    if check_pos((pos[0]-1, pos[1]+1), rocks_x, rocks_y, []):
        drop_sand((pos[0]-1, pos[1]+1), sands, rocks_x, rocks_y)
    if check_pos((pos[0]+1, pos[1]+1), rocks_x, rocks_y, []):
        drop_sand((pos[0]+1, pos[1]+1), sands, rocks_x, rocks_y)


if __name__ == "__main__":
    #main()
    main2()