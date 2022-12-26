import util
import re

def main():
    lines = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''.splitlines()
    lines = util.get_input(19).splitlines()
    total = 0
    for i, line in enumerate(lines):
        m = re.match(r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", line)
        ore = int(m.group(1))
        clay = int(m.group(2))
        obsidian_ore = int(m.group(3))
        obsidian_clay = int(m.group(4))
        geode_ore = int(m.group(5))
        geode_obsidian = int(m.group(6))
        prices = (ore, clay, (obsidian_ore, obsidian_clay), (geode_ore, geode_obsidian))
        geodes = simulate(prices)
        total += geodes * (i + 1)
        #break
    print(f"Total: {total}")


def simulate(prices):
    states = [[[1, 0, 0, 0], [0, 0, 0, 0], i] for i in range(2)] # (robots, materials, next_robot)
    turns = 24
    for i in range(24):
        print(f"Round {i + 1}")
        new_states = []
        for state in states:
            if state[2] == 0:
                if state[1][0] >= prices[0]:
                    state[1][0] -= prices[0]
                    state[0][0] += 1
                    state[1][0] -= 1 # counteract the robot not being built
                    state[2] = -1
            elif state[2] == 1:
                if state[1][0] >= prices[1]:
                    state[1][0] -= prices[1]
                    state[0][1] += 1
                    state[1][1] -= 1
                    state[2] = -1
            elif state[2] == 2:
                if state[1][0] >= prices[2][0] and state[1][1] >= prices[2][1]:
                    state[1][0] -= prices[2][0]
                    state[1][1] -= prices[2][1]
                    state[0][2] += 1
                    state[1][2] -= 1
                    state[2] = -1
            elif state[2] == 3:
                if state[1][0] >= prices[3][0] and state[1][2] >= prices[3][1]:
                    state[1][0] -= prices[3][0]
                    state[1][2] -= prices[3][1]
                    state[0][3] += 1
                    state[1][3] -= 1
                    state[2] = -1
            for j in range(4):
                state[1][j] += state[0][j]

            if state[2] == -1:
                if state[1][0] >= prices[3][0] and state[1][2] >= prices[3][1]:
                    new_state = [state[0].copy(), state[1].copy(), 3]
                    new_states.append(new_state)
                else:
                    for j in range(4):
                        if j == 2 and state[0][1] == 0:
                            continue
                        if j == 3 and state[0][2] == 0:
                            continue
                        new_state = [state[0].copy(), state[1].copy(), j]
                        new_states.append(new_state)
            else:
                new_states.append(state)

        states = new_states

        #states.sort(key=lambda x: valuate(x, prices, turns-i), reverse=True)
        #states = states[:1000]
        max_geodes = max([state[1][3] for state in states])
        if max_geodes > 0:
            states = [state for state in states if state[1][3] == max_geodes]

        print(f"Decreasing states: {len(states)}")

        state_map = {}
        for s in states:
            state_map[freeze(s)] = s

        states = list(state_map.values())

        print(f"States: {len(states)}")

    max_geodes = max([state[1][3] for state in states])
    print(f"Max geodes: {max_geodes}")
    return max_geodes


def freeze(l):
    return tuple(l[0]) ,tuple(l[1]), l[2]


def simulate_recurse(prices):
    states = [[[1, 0, 0, 0], [0, 0, 0, 0], i] for i in range(2)] # (robots, materials, next_robot)
    turns = 24
    for i in range(24):
        print(f"Round {i + 1}")
        new_states = []
        for state in states:
            if state[2] == 0:
                if state[1][0] >= prices[0]:
                    state[1][0] -= prices[0]
                    state[0][0] += 1
                    state[1][0] -= 1 # counteract the robot not being built
                    state[2] = -1
            elif state[2] == 1:
                if state[1][0] >= prices[1]:
                    state[1][0] -= prices[1]
                    state[0][1] += 1
                    state[1][1] -= 1
                    state[2] = -1
            elif state[2] == 2:
                if state[1][0] >= prices[2][0] and state[1][1] >= prices[2][1]:
                    state[1][0] -= prices[2][0]
                    state[1][1] -= prices[2][1]
                    state[0][2] += 1
                    state[1][2] -= 1
                    state[2] = -1
            elif state[2] == 3:
                if state[1][0] >= prices[3][0] and state[1][2] >= prices[3][1]:
                    state[1][0] -= prices[3][0]
                    state[1][2] -= prices[3][1]
                    state[0][3] += 1
                    state[1][3] -= 1
                    state[2] = -1
            for j in range(4):
                state[1][j] += state[0][j]

            if state[2] == -1:
                if state[1][0] >= prices[3][0] and state[1][2] >= prices[3][1]:
                    new_state = [state[0].copy(), state[1].copy(), 3]
                    new_states.append(new_state)
                else:
                    for j in range(4):
                        if j == 2 and state[0][1] == 0:
                            continue
                        if j == 3 and state[0][2] == 0:
                            continue
                        new_state = [state[0].copy(), state[1].copy(), j]
                        new_states.append(new_state)
            else:
                new_states.append(state)

        states = new_states

        #states.sort(key=lambda x: valuate(x, prices, turns-i), reverse=True)
        #states = states[:1000]
        max_geodes = max([state[1][3] for state in states])
        if max_geodes > 0:
            states = [state for state in states if state[1][3] == max_geodes]

        print(f"Decreasing states: {len(states)}")

        state_map = {}
        for s in states:
            state_map[freeze(s)] = s

        states = list(state_map.values())

        print(f"States: {len(states)}")

    max_geodes = max([state[1][3] for state in states])
    print(f"Max geodes: {max_geodes}")
    return max_geodes


def maximize(prices):
    best_list = [0 for i in range(24)]
    best_score = 0
    missing = [[1, 2, 3],
               [0, 2, 3],
               [0, 1, 3],
               [0, 1, 2]]
    while True:
        runs = []
        for i in range(12):
            for j in missing[best_list[i]]:
                new_list = best_list.copy()
                new_list[i] = j
                score = valuate(sim_list(prices, new_list), prices)
                runs.append((new_list, score))
                print(f"{score} with {new_list}")

        new_best_list, new_best_score = max(runs, key=lambda x: x[1])
        if new_best_score == best_score:
            break

        best_list = new_best_list
        best_score = new_best_score

    return sim_list(prices, best_list)[1][3]


def sim_list(prices, l):
    state = [[1, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(24):
        next_robot = l[sum(state[0])]
        if next_robot == 0:
            if state[1][0] >= prices[0]:
                state[1][0] -= prices[0]
                state[0][0] += 1
                state[1][0] -= 1  # counteract the robot not being built
        elif next_robot == 1:
            if state[1][0] >= prices[1]:
                state[1][0] -= prices[1]
                state[0][1] += 1
                state[1][1] -= 1
        elif next_robot == 2:
            if state[1][0] >= prices[2][0] and state[1][1] >= prices[2][1]:
                state[1][0] -= prices[2][0]
                state[1][1] -= prices[2][1]
                state[0][2] += 1
                state[1][2] -= 1
        elif next_robot == 3:
            if state[1][0] >= prices[3][0] and state[1][2] >= prices[3][1]:
                state[1][0] -= prices[3][0]
                state[1][2] -= prices[3][1]
                state[0][3] += 1
                state[1][3] -= 1
        for j in range(4):
            state[1][j] += state[0][j]

    return state


def valuate(state, prices):
    clay = state[1][1]
    obsidian = state[1][2]
    geode = state[1][3]

    if geode > 0:
        return geode + 4
    elif obsidian > 0:
        return clamp(obsidian, 0, prices[3][1]) / prices[3][1] + 2
    else:
        return clamp(clay, 0, prices[2][1]) / prices[2][1]


def valuate_old(state, p, n):
    geode = valuate_geode(state[1][3], p, n)
    obsidian = valuate_obsidian(state[1][2], p, n) / 2
    clay = valuate_clay(state[1][1], p, n) / 4
    ore = valuate_ore(state[1][0], p, n) / 8
    geode_robot = valuate_geode(state[1][3], p, n) * n
    obsidian_robot = valuate_obsidian(state[1][2] * (n-1), p, n) / 1
    clay_robot = valuate_clay(state[1][1] * (n-2), p, n) / 1
    ore_robot = valuate_ore(state[1][0] * (n-3), p, n) / 8

    return geode + geode_robot + obsidian_robot + clay_robot + ore_robot

def valuate_geode(x, p, n):
    return x

def valuate_obsidian(x, p, n):
    x = clamp(x, 0, p[3][1])
    return x * (p[3][1] / (p[3][0] + p[3][1])) * (n-1)

def valuate_clay(x, p, n):
    x = clamp(x, 0, p[2][1])
    return x * (p[3][1] / (p[3][0] + p[3][1])) * (p[2][1] / (p[2][0] + p[2][1])) * (n-2)

def valuate_ore(x, p, n):
    x = clamp(x, 0, 4)
    return (x * (7/9) * (14/17) * (n-3)
            + x * (7/9) * (3/17) * (n-2)
            + x * (2/9) * (n-1))

def clamp(x, a, b):
    return max(a, min(x, b))

def simulate2(prices):
    states = [[[1, 0, 0, 0], [0, 0, 0, 0], i] for i in range(2)] # (robots, materials, next_robot)
    turns = 24
    counter = 0
    for i in range(32):
        print(f"Round {i + 1}")
        new_states = []
        for state in states:
            if state[2] == 0:
                if state[1][0] >= prices[0]:
                    state[1][0] -= prices[0]
                    state[0][0] += 1
                    state[1][0] -= 1 # counteract the robot not being built
                    state[2] = -1
            elif state[2] == 1:
                if state[1][0] >= prices[1]:
                    state[1][0] -= prices[1]
                    state[0][1] += 1
                    state[1][1] -= 1
                    state[2] = -1
            elif state[2] == 2:
                if state[1][0] >= prices[2][0] and state[1][1] >= prices[2][1]:
                    state[1][0] -= prices[2][0]
                    state[1][1] -= prices[2][1]
                    state[0][2] += 1
                    state[1][2] -= 1
                    state[2] = -1
            elif state[2] == 3:
                if state[1][0] >= prices[3][0] and state[1][2] >= prices[3][1]:
                    state[1][0] -= prices[3][0]
                    state[1][2] -= prices[3][1]
                    state[0][3] += 1
                    state[1][3] -= 1
                    state[2] = -1
            for j in range(4):
                state[1][j] += state[0][j]

            if state[2] == -1:
                if state[1][0] >= prices[3][0] and state[1][2] >= prices[3][1]:
                    new_state = [state[0].copy(), state[1].copy(), 3]
                    new_states.append(new_state)
                else:
                    for j in range(4):
                        if j == 2 and state[0][1] == 0:
                            continue
                        if j == 3 and state[0][2] == 0:
                            continue
                        new_state = [state[0].copy(), state[1].copy(), j]
                        new_states.append(new_state)
            else:
                new_states.append(state)

        states = new_states

        #states.sort(key=lambda x: valuate(x, prices, turns-i), reverse=True)
        #states = states[:1000]
        max_geodes = max([state[1][3] for state in states])
        if max_geodes > 0:
            counter += 1
            if counter > 1:
                states = [state for state in states if state[1][3] >= max(1, max_geodes - 4)]

        print(f"Decreasing states: {len(states)}")

        state_map = {}
        for s in states:
            state_map[freeze(s)] = s

        states = list(state_map.values())

        print(f"States: {len(states)}")

    max_geodes = max([state[1][3] for state in states])
    print(f"Max geodes: {max_geodes}")
    return max_geodes

def main2():
    lines = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''.splitlines()
    lines = util.get_input(19).splitlines()[:3]
    total = 1
    print("s")
    for i, line in enumerate(lines):
        m = re.match(r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", line)
        ore = int(m.group(1))
        clay = int(m.group(2))
        obsidian_ore = int(m.group(3))
        obsidian_clay = int(m.group(4))
        geode_ore = int(m.group(5))
        geode_obsidian = int(m.group(6))
        prices = (ore, clay, (obsidian_ore, obsidian_clay), (geode_ore, geode_obsidian))
        geodes = simulate2(prices)
        total *= geodes
        #break
    print(f"Total: {total}")

if __name__ == "__main__":
    main2()