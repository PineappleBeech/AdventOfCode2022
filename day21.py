import util
import re
from decimal import Decimal

def main():
    lines = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''.splitlines()
    lines = util.get_input(21).splitlines()
    vars = {}
    operations = []
    for line in lines:
        if "+" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) \+ ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "+"))
            if m.group(1) == "root":
                targets = [m.group(2), m.group(3)]
        elif "-" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) - ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "-"))
        elif "*" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) \* ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "*"))
        elif "/" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) / ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "/"))
        else:
            m = re.match(r"([a-z]{4}): (\d+)", line)
            vars[m.group(1)] = int(m.group(2))

    while "root" not in vars:
        for op in operations:
            if op[1] in vars and op[2] in vars:
                if op[3] == "+":
                    vars[op[0]] = vars[op[1]] + vars[op[2]]
                elif op[3] == "-":
                    vars[op[0]] = vars[op[1]] - vars[op[2]]
                elif op[3] == "*":
                    vars[op[0]] = vars[op[1]] * vars[op[2]]
                elif op[3] == "/":
                    vars[op[0]] = vars[op[1]] // vars[op[2]]
                operations.remove(op)

    print(targets)
    print(vars["root"])


def main2():
    lines = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''.splitlines()
    lines = util.get_input(21).splitlines()
    vars = {}
    operations = []
    for line in lines:
        if "+" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) \+ ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "+"))
            if m.group(1) == "root":
                targets = [m.group(2), m.group(3)]
        elif "-" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) - ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "-"))
        elif "*" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) \* ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "*"))
        elif "/" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) / ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "/"))
        else:
            m = re.match(r"([a-z]{4}): (\d+)", line)
            vars[m.group(1)] = Decimal(m.group(2))

    del vars["humn"]

    old = 0

    while len(operations) != old:
        old = len(operations)
        for op in operations:
            if op[1] in vars and op[2] in vars:
                if op[3] == "+":
                    vars[op[0]] = vars[op[1]] + vars[op[2]]
                elif op[3] == "-":
                    vars[op[0]] = vars[op[1]] - vars[op[2]]
                elif op[3] == "*":
                    vars[op[0]] = vars[op[1]] * vars[op[2]]
                elif op[3] == "/":
                    vars[op[0]] = vars[op[1]] // vars[op[2]]
                operations.remove(op)

    if targets[0] in vars:
        print(targets[0])
        print(vars[targets[0]])
        t = 1
    else:
        print(targets[1])
        print(vars[targets[1]])
        t = 0

    vars[targets[t]] = vars[targets[t-1]]
    operations2 = operations.copy()

    while "humn" not in vars:
        for op in operations:
            if op[0] in vars and (op[1] in vars or op[2] in vars):
                if op[1] in vars:
                    res = 2
                else:
                    res = 1
                if op[3] == "+":
                    vars[op[res]] = vars[op[0]] - vars[op[3-res]]
                elif op[3] == "-":
                    if res == 1:
                        vars[op[res]] = vars[op[0]] + vars[op[3-res]]
                    else:
                        vars[op[res]] = vars[op[0]] - vars[op[3-res]]
                elif op[3] == "*":
                    if op == ('zvlm', 'tczv', 'zfrj', '*'):
                        print()
                    vars[op[res]] = vars[op[0]] / vars[op[3-res]]
                elif op[3] == "/":
                    if res == 1:
                        vars[op[res]] = vars[op[0]] * vars[op[3-res]]
                    else:
                        vars[op[res]] = vars[op[0]] // vars[op[3-res]]

                operations.remove(op)

    print(vars["humn"])

    for op in operations2:
        if op[3] == "+":
            assert vars[op[0]] == vars[op[1]] + vars[op[2]]
        elif op[3] == "-":
            assert vars[op[0]] == vars[op[1]] - vars[op[2]]
        elif op[3] == "*":
            assert vars[op[0]] == vars[op[1]] * vars[op[2]]
        elif op[3] == "/":
            assert vars[op[0]] == vars[op[1]] // vars[op[2]]

    print(vars["humn"])

def main3():
    lines = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''.splitlines()
    lines = '''root: aaaa + cccc
cccc: dddd - humn
dddd: 10
humn: 2
aaaa: 32'''.splitlines()
    lines = util.get_input(21).splitlines()
    vars = {}
    operations = []
    for line in lines:
        if "+" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) \+ ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "+"))
            if m.group(1) == "root":
                targets = [m.group(2), m.group(3)]
        elif "-" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) - ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "-"))
        elif "*" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) \* ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "*"))
        elif "/" in line:
            m = re.match(r"([a-z]{4}): ([a-z]{4}) / ([a-z]{4})", line)
            operations.append((m.group(1), m.group(2), m.group(3), "/"))
        else:
            m = re.match(r"([a-z]{4}): (\d+)", line)
            vars[m.group(1)] = Decimal(m.group(2))

    del vars["humn"]

    old = 0

    while len(operations) != old:
        old = len(operations)
        for op in operations:
            if op[1] in vars and op[2] in vars:
                if op[3] == "+":
                    vars[op[0]] = vars[op[1]] + vars[op[2]]
                elif op[3] == "-":
                    vars[op[0]] = vars[op[1]] - vars[op[2]]
                elif op[3] == "*":
                    vars[op[0]] = vars[op[1]] * vars[op[2]]
                elif op[3] == "/":
                    vars[op[0]] = vars[op[1]] // vars[op[2]]
                operations.remove(op)

    if targets[0] in vars:
        print(targets[0])
        print(vars[targets[0]])
        t = 1
    else:
        print(targets[1])
        print(vars[targets[1]])
        t = 0

    #vars[targets[t]] = vars[targets[t - 1]]
    operations2 = operations.copy()

    l = ["humn"]

    while targets[t] not in l:
        for op in operations:
            if l[-1] == op[1] or l[-1] == op[2]:
                if l[-1] == op[1]:
                    l[-1] = ("x", op[3], op[2])
                else:
                    l[-1] = (op[1], op[3], "x")
                l.append(op[0])
                operations.remove(op)

    num = vars[targets[1-t]]

    for op in reversed(l[:-1]):
        if op[0] == "x":
            if op[1] == "+":
                num -= vars[op[2]]
            elif op[1] == "-":
                num += vars[op[2]]
            elif op[1] == "*":
                num /= vars[op[2]]
            elif op[1] == "/":
                num *= vars[op[2]]

        elif op[2] == "x":
            if op[1] == "+":
                num -= vars[op[0]]
            elif op[1] == "-":
                num = vars[op[0]] - num
            elif op[1] == "*":
                num /= vars[op[0]]
            elif op[1] == "/":
                #num = vars[op[0]] / num
                num = num / vars[op[0]]
                assert False

    print(num)


if __name__ == "__main__":
    main3()