listArray = [1, 3, 5, 2, 68, 4, 5, 6, 6, 69]


def quick_sort(list_nums):
    if not list_nums or len(list_nums) == 1:
        return list_nums
    pivot = list_nums[0]
    left_hand = []
    right_hand = []
    for item in list_nums[1:]:
        if pivot > item:
            left_hand.append(item)
        else:
            right_hand.append(item)
    return quick_sort(left_hand) + [pivot] + quick_sort(right_hand)


print(quick_sort(listArray))

