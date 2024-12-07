import re

input = open("day03.in").readlines()

mul_pattern = r"mul\(\d+,\d+\)"
do_pattern = r"do\(\)"
dont_pattern = r"don\'t\(\)"


def eval_mul(expression):
    assert re.match(mul_pattern, expression)
    a, b = map(int, expression[4:-1].split(","))
    return a * b


ans1 = 0
for line in input:
    match = re.findall(mul_pattern, line)
    for mul in match:
        ans1 += eval_mul(mul)
print("part1", ans1)


ops_pattern = "{}|{}|{}".format(mul_pattern, do_pattern, dont_pattern)

ans2 = 0
mul_enabled = True
for line in input:
    match = re.findall(ops_pattern, line)
    for m in match:
        if re.match(mul_pattern, m) and mul_enabled:
            ans2 += eval_mul(m)
        elif re.match(do_pattern, m):
            mul_enabled = True
        elif re.match(dont_pattern, m):
            mul_enabled = False
print("part2", ans2)
