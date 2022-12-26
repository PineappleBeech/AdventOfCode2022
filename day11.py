import math

import util

def main():
    inp = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines()
    inp = util.get_input(11).splitlines()
    monkeys = []
    for line in inp:
        if line == "":
            continue
        command = line.split()[0]
        if command == "Monkey":
            monkeys.append({})
        elif command == "Starting":
            monkeys[-1]["items"] = [int(i.replace(",", "")) for i in line.split()[2:]]
        elif command == "Operation:":
            op = line.split()[3:]
            assert op[0] == "old"
            other = op[2]
            monkeys[-1]["operation"] = op_factory(op[1], other)
        elif command == "Test:":
            value = int(line.split()[3])
            monkeys[-1]["test"] = test_factory(value)
        elif command == "If":
            if line.split()[1] == "true:":
                monkeys[-1]["true"] = int(line.split()[5])
            else:
                monkeys[-1]["false"] = int(line.split()[5])


    ops = [0 for i in range(len(monkeys))]

    for i in range(20):
        for j, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                item = monkey["operation"](item)
                ops[j] += 1
                item = item // 3
                if monkey["test"](item):
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
            monkey["items"] = []
        print(f"Round {i} done")

    ops.sort()
    print(ops[-1] * ops[-2])


def op_factory(op, other):
    if op == "*":
        if other == "old":
            return lambda x: x * x
        else:
            return lambda x: x * int(other)
    elif op == "+":
        if other == "old":
            return lambda x: x + x
        else:
            return lambda x: x + int(other)

def test_factory(value):
    def t(x):
        return x % value == 0
    return t


def main2():
    inp = util.get_input(11).splitlines()
    monkeys = []
    test_values = []
    for line in inp:
        if line == "":
            continue
        command = line.split()[0]
        if command == "Monkey":
            monkeys.append({})
        elif command == "Starting":
            monkeys[-1]["items"] = [int(i.replace(",", "")) for i in line.split()[2:]]
        elif command == "Operation:":
            op = line.split()[3:]
            assert op[0] == "old"
            other = op[2]
            monkeys[-1]["operation"] = op_factory(op[1], other)
        elif command == "Test:":
            value = int(line.split()[3])
            monkeys[-1]["test"] = test_factory(value)
            test_values.append(value)
        elif command == "If":
            if line.split()[1] == "true:":
                monkeys[-1]["true"] = int(line.split()[5])
            else:
                monkeys[-1]["false"] = int(line.split()[5])

    lcm = math.lcm(*test_values)
    ops = [0 for i in range(len(monkeys))]

    for i in range(10000):
        for j, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                item = monkey["operation"](item)
                ops[j] += 1
                item = item % lcm
                #item = item // 3
                if monkey["test"](item):
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
            monkey["items"] = []
        if i % 100 == 0:
            print(f"Round {i} done")

    ops.sort()
    print(ops[-1] * ops[-2])

if __name__ == "__main__":
    main()
    main2()