from collections import Counter

input = [x.split() for x in open("day01.in").readlines()]

left = sorted([int(x[0]) for x in input])
right = sorted([int(x[1]) for x in input])

total_distance = 0
for i in range(len(left)):
    id_left, id_right = left[i], right[i]
    distance = abs(id_left - id_right)
    total_distance += distance
print("part1", total_distance)

M = Counter({id: 0 for id in left})
M.update(id for id in right if id in M)
total_similarity = sum(id * count for id, count in M.items())
print("part2", total_similarity)
