input = [list(map(int, x.split())) for x in open("day02.in").readlines()]

reports = [list(map(int, x)) for x in input]


def is_safe(report):
    all_increasing = all([x2 > x1 for x1, x2 in zip(report, report[1:])])
    all_decreasing = all([x2 < x1 for x1, x2 in zip(report, report[1:])])
    levels_tolerated = all([abs(x2 - x1) <= 3 for x1, x2 in zip(report, report[1:])])
    return (all_increasing or all_decreasing) and levels_tolerated


ans1 = sum([is_safe(report) for report in reports])
print("part1", ans1)


def is_safe_dampened(report):
    expanded = [report]
    for i in range(len(report)):
        expanded.append(report[:i] + report[i + 1 :])
    for r in expanded:
        if is_safe(r):
            return True
    return False


ans2 = sum([is_safe_dampened(report) for report in reports])
print("part2", ans2)
