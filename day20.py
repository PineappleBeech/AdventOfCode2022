import util
import numpy as np

def main():
    data = '''1
2
-3
3
-2
0
4'''.splitlines()
    #data = util.get_input(20).splitlines()
    #array = np.array([int(x) * 1503 for x in data], dtype=np.int64)
    array = np.array([int(x) * 2 for x in data], dtype=np.int64)
    map_array = np.copy(array)
    inverted = False
    for j in range(1):
        for i in range(len(array)):
            dest = (map_array[i]) % (len(array) - 1)  # -1 because it is being placed in an array that excludes itself
            if dest == 0:
                continue
            if inverted != (dest < 0):
                inverted = not inverted
                array = np.flip(array)
            if dest < 0:
                dest = -dest

            if inverted:
                print("Error: inverted")

            source = np.where(array == map_array[i])[0][0]

            array = np.roll(array, -source)
            array = np.concatenate((array[1:dest+1], array[0:1], array[dest+1:]))
            _ = 0
        _ = 0

    if inverted:
        array = np.flip(array)

    zero_index = np.where(array == 0)[0][0]
    num1 = int(array[(zero_index + 1000) % len(array)])
    num2 = int(array[(zero_index + 2000) % len(array)])
    num3 = int(array[(zero_index + 3000) % len(array)])

    #print(sum((num1, num2, num3)) * 811589153 / 1503)
    print(sum((num1, num2, num3)))


def main2():
    data = '''1
2
-3
3
-2
0
4'''.splitlines()
    data = util.get_input(20).splitlines()
    array = [int(x) for x in data]
    map_array = array.copy()
    for j in range(1):
        for i in range(len(array)):
            num = map_array[i] # number to move
            dest = (num) % (len(array) - 1) # index to move to
            if dest == 0:
                continue

            source = array.index(num) # index of number to move
            array = array[:source] + array[source+1:]

            index = (dest + source) % (len(array))
            array = array[:index] + [num] + array[index:]

        #print(array)

    zero_index = array.index(0)
    num1 = int(array[(zero_index + 1000) % len(array)])
    num2 = int(array[(zero_index + 2000) % len(array)])
    num3 = int(array[(zero_index + 3000) % len(array)])

    print(sum((num1, num2, num3)))


def main3():
    data = '''1
2
-3
3
-2
0
4'''.splitlines()
    data = util.get_input(20).splitlines()
    array = [int(x) * 811589153 for x in data]
    map_array = array.copy()
    length = len(array)
    modified_array = list(range(length))
    for j in range(10):
        for i in range(len(array)):
            num = map_array[i]
            offset = num % (length - 1)
            index = modified_array.index(i)
            modified_array = modified_array[:index] + modified_array[index+1:]
            end = (index + offset) % (length - 1)
            modified_array = modified_array[:end] + [i] + modified_array[end:]
            #print(array)

        zero_index = array.index(0)
        #print(array[zero_index:] + array[:zero_index])

    array = [array[i] for i in modified_array]

    zero_index = array.index(0)
    num1 = int(array[(zero_index + 1000) % len(array)])
    num2 = int(array[(zero_index + 2000) % len(array)])
    num3 = int(array[(zero_index + 3000) % len(array)])

    print(sum((num1, num2, num3)))




if __name__ == '__main__':
    main3()