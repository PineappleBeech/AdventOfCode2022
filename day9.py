import util
import numpy as np

def main():
    lines = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.splitlines()
    lines = util.get_input(9).splitlines()
    head = np.zeros(2, dtype=np.int32)
    tail = np.zeros(2, dtype=np.int32)
    tail_positions = set()
    t = []
    for line in lines:
        direction, distance = line.split()
        distance = int(distance)
        for i in range(distance):
            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "R":
                head[0] += 1
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                if tail[0] < head[0]:
                    tail[0] += 1
                elif tail[0] > head[0]:
                    tail[0] -= 1
                if tail[1] < head[1]:
                    tail[1] += 1
                elif tail[1] > head[1]:
                    tail[1] -= 1
            tail_positions.add(tuple(tail))
            t.append(tuple(tail))
    print(len(tail_positions))


def main2():
    lines = util.get_input(9).splitlines()
    rope = np.zeros((10, 2), dtype=np.int32)
    tail_positions = set()
    for line in lines:
        direction, distance = line.split()
        distance = int(distance)
        for i in range(distance):
            if direction == "U":
                rope[0][1] += 1
            elif direction == "D":
                rope[0][1] -= 1
            elif direction == "L":
                rope[0][0] -= 1
            elif direction == "R":
                rope[0][0] += 1

            for head, tail in zip(rope[:-1], rope[1:]):

                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    if tail[0] < head[0]:
                        tail[0] += 1
                    elif tail[0] > head[0]:
                        tail[0] -= 1
                    if tail[1] < head[1]:
                        tail[1] += 1
                    elif tail[1] > head[1]:
                        tail[1] -= 1
            tail_positions.add(tuple(rope[-1]))
    print(len(tail_positions))


if __name__ == "__main__":
    main()
    main2()