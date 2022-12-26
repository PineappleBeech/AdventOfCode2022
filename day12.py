import util
import numpy as np

alpha = "abcdefghijklmnopqrstuvwxyz"

def main():
    lines = util.get_input(12).splitlines()
    for i, line in enumerate(lines):
        if "S" in line:
            start = (i, line.index("S"))
            lines[i] = line.replace("S", "a")
        if "E" in line:
            end = (i, line.index("E"))
            lines[i] = line.replace("E", "z")

    map = np.array([[alpha.find(c) for c in line] for line in lines])

    routes = np.full(map.shape, -1)

    routes[start] = 0

    while True:
        new_routes = np.copy(routes)

        for i in range(map.shape[0]):
            for j in range(map.shape[1]):
                if routes[i, j] == -1:
                    continue
                if i > 0 and routes[i-1, j] == -1 and map[i-1, j] - map[i, j] <= 1:
                    new_routes[i-1, j] = routes[i, j] + 1
                if i < map.shape[0] - 1 and routes[i+1, j] == -1 and map[i+1, j] - map[i, j] <= 1:
                    new_routes[i+1, j] = routes[i, j] + 1
                if j > 0 and routes[i, j-1] == -1 and map[i, j-1] - map[i, j] <= 1:
                    new_routes[i, j-1] = routes[i, j] + 1
                if j < map.shape[1] - 1 and routes[i, j+1] == -1 and map[i, j+1] - map[i, j] <= 1:
                    new_routes[i, j+1] = routes[i, j] + 1

        routes = new_routes
        print("1 step")

        if routes[end] != -1:
            break

    print(routes[end])

def main2():
    lines = util.get_input(12).splitlines()
    for i, line in enumerate(lines):
        if "E" in line:
            end = (i, line.index("E"))
            lines[i] = line.replace("E", "z")

    map = np.array([[alpha.find(c) for c in line] for line in lines])

    routes = np.full(map.shape, -1)

    routes[end] = 0

    while True:
        new_routes = np.copy(routes)

        for i in range(map.shape[0]):
            for j in range(map.shape[1]):
                if routes[i, j] == -1:
                    continue
                if i > 0 and routes[i-1, j] == -1 and map[i-1, j] - map[i, j] >= -1:
                    new_routes[i-1, j] = routes[i, j] + 1
                if i < map.shape[0] - 1 and routes[i+1, j] == -1 and map[i+1, j] - map[i, j] >= -1:
                    new_routes[i+1, j] = routes[i, j] + 1
                if j > 0 and routes[i, j-1] == -1 and map[i, j-1] - map[i, j] >= -1:
                    new_routes[i, j-1] = routes[i, j] + 1
                if j < map.shape[1] - 1 and routes[i, j+1] == -1 and map[i, j+1] - map[i, j] >= -1:
                    new_routes[i, j+1] = routes[i, j] + 1



        routes = new_routes
        print("1 step")

        a = np.all([(routes > 0), (map == 0)], axis=0)

        if np.any(a):
            break

    print(np.max(routes))


if __name__ == "__main__":
    #main()
    main2()