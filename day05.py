top, bottom = open("day05.in").read().strip().split("\n\n")

page_ordering_rules = [list(map(int, x.split("|"))) for x in top.split("\n")]
page_number_updates = [list(map(int, x.split(","))) for x in bottom.split("\n")]


def get_middle_page(page_numbers):
    assert len(page_numbers) % 2 == 1
    middle_index = len(page_numbers) // 2
    middle_page = page_numbers[middle_index]
    return middle_page


def is_in_order(page_numbers):
    for before, after in page_ordering_rules:
        before_index = page_numbers.index(before) if before in page_numbers else None
        after_index = page_numbers.index(after) if after in page_numbers else None
        if (before_index is not None and after_index is not None) and after_index < before_index:
            return False, None
    return True, get_middle_page(page_numbers)


ans1 = 0
for update in page_number_updates:
    in_order, middle_page = is_in_order(update)
    if in_order:
        ans1 += middle_page
print("part1", ans1)


def correct_order(page_numbers):
    while True:
        in_order = True
        for before, after in page_ordering_rules:
            before_index = page_numbers.index(before) if before in page_numbers else None
            after_index = page_numbers.index(after) if after in page_numbers else None
            if (before_index is not None and after_index is not None) and after_index < before_index:
                swap = page_numbers[before_index]
                page_numbers[before_index] = page_numbers[after_index]
                page_numbers[after_index] = swap
                in_order = False
        if in_order:
            break
    return get_middle_page(page_numbers)


ans2 = 0
for update in page_number_updates:
    in_order, _ = is_in_order(update)
    if not in_order:
        middle_page = correct_order(update)
        ans2 += middle_page
print("part2", ans2)
