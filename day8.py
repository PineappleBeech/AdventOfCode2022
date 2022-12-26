import util
import numpy as np

def main():
    text = util.get_input(8).splitlines()
    grid = np.array([list(i) for i in text], dtype=np.int8)
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]], dtype=np.int8)
    total = 0
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            visible = False
            for d in directions:
                i = 0
                height = grid[x, y]
                direction_visible = True
                try:
                    while True:
                        i += 1
                        offset = d * i
                        if grid[x + offset[0], y + offset[1]] >= height:
                            direction_visible = False
                            break
                except IndexError:
                    pass
                if direction_visible:
                    visible = True
                    break
            if visible:
                total += 1
    print(total)

def main2():
    text = util.get_input(8).splitlines()
    grid = np.array([list(i) for i in text], dtype=np.int8)
    visible = np.zeros(grid.shape, dtype=np.int8)
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]], dtype=np.int8)
    rotator = np.array([[0, 1], [-1, 0]], dtype=np.int8)
    for i in range(4):
        max_height = np.zeros(grid.shape[0], dtype=np.int8)
        max_height -= 1
        for y in range(grid.shape[1]):
            visible[:, y] = np.maximum(np.where(grid[:, y] > max_height, 1, 0), visible[:, y])
            max_height = np.maximum(max_height, grid[:, y])
        grid = np.rot90(grid)
        visible = np.rot90(visible)
    print(np.sum(visible))

def main3():
    text = '''30373
25512
65332
33549
35390'''.splitlines()
    text = util.get_input(8).splitlines()
    grid = np.array([list(i) for i in text], dtype=np.int8)
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]], dtype=np.int8)
    total = 0
    scores = np.zeros(grid.shape, dtype=np.int32)
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            distances = []
            for d in directions:
                height = grid[x, y]
                i = 1
                while True:
                    offset = d * i
                    tree_pos = (x + offset[0], y + offset[1])
                    if tree_pos[0] < 0 or tree_pos[0] >= grid.shape[0] or tree_pos[1] < 0 or tree_pos[1] >= grid.shape[1]:
                        i -= 1
                        break
                    tree = grid[x + offset[0], y + offset[1]]
                    if tree >= height:
                        break
                    i += 1
                distances.append(i)
            scores[x, y] = distances[0] * distances[1] * distances[2] * distances[3]
    print(np.max(scores))



if __name__ == "__main__":
    main3()