import functools

import util
import re

def main():
    lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()
    lines = util.get_input(15).splitlines()
    ranges = []
    for line in lines:
        m = re.findall(r"=(-?\d+)", line)
        sx = int(m[0])
        sy = int(m[1])
        bx = int(m[2])
        by = int(m[3])

        diff = abs(sx - bx) + abs(sy - by)

        h = abs(sy - 2000000)

        diff -= h

        if diff < 0:
            continue

        ranges.append(range(sx-diff, sx+diff))

    s = functools.reduce(lambda x, y: set(x).union(set(y)), ranges)
    print(len(s))

def main2():
    lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()
    lines = util.get_input(15).splitlines()
    ranges = []
    sensors = []
    for line in lines:
        m = re.findall(r"=(-?\d+)", line)
        sx = int(m[0])
        sy = int(m[1])
        bx = int(m[2])
        by = int(m[3])

        diff = abs(sx - bx) + abs(sy - by)

        sensors.append((sx, sy, diff))

    found = False

    for s in sensors:
        for x in range(-s[2]-1, +s[2]+2):
            for pos in ((s[0]+x, s[1]+s[2]-abs(x)+1), (s[0]+x, s[1]-s[2]+abs(x)-1)):
                #print(f"Checking {pos}")
                if 0 <= pos[0] <= 4000000 and 0 <= pos[1] <= 4000000:
                    in_range = False
                    for s2 in sensors:
                        if s2 == s:
                            continue

                        if abs(s2[0] - pos[0]) + abs(s2[1] - pos[1]) <= s2[2]:
                            in_range = True
                    if not in_range:
                        print(pos)
                        found = True
                        break
            if found:
                break
        if found:
            break
        print("Sensor at x={}, y={}: closest beacon is at x={}, y={}".format(s[0], s[1], pos[0], pos[1]))

    print(pos[0]*4000000 + pos[1])

if __name__ == "__main__":
    main2()