import util

def main():
    pairs = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''.split("\n\n")
    pairs = util.get_input(13).split("\n\n")
    pairs = [i.splitlines() for i in pairs]
    total = 0
    s = []
    for i, pair in enumerate(pairs):
        left = eval(pair[0])
        right = eval(pair[1])
        res = check_pair(left, right)
        if res == "l":
            total += i + 1
            s.append(i+1)


    print(total)

def check_pair(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return "n"
        elif left < right:
            return "l"
        elif left > right:
            return "r"
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == len(right):
            tie = "n"
        elif len(left) < len(right):
            tie = "l"
        elif len(left) > len(right):
            tie = "r"
        for i in range(min(len(left), len(right))):
            res = check_pair(left[i], right[i])
            if res == "l" or res == "r":
                return res
        return tie

    elif isinstance(left, list) and isinstance(right, int):
        return check_pair(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return check_pair([left], right)#

def main2():
    lines = util.get_input(13).splitlines()
    packets = [eval(i) for i in lines if i]
    div1 = [[2]]
    div2 = [[6]]
    pos1 = 1
    pos2 = 2
    for i in packets:
        res = check_pair(i, div1)
        if res == "l":
            pos1 += 1
        res = check_pair(i, div2)
        if res == "l":
            pos2 += 1

    print(pos1*pos2)

if __name__ == "__main__":
    main()
    main2()