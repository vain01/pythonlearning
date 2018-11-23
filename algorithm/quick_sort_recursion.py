def quick_sort(nums):
    if not nums or len(nums) == 1:
        return nums

    pivot = nums[0]
    left_hand = []
    right_hand = []

    for item in nums[1:]:
        if item < pivot:
            left_hand.append(item)
        else:
            right_hand.append(item)
            
    return quick_sort(left_hand) + [pivot] + quick_sort(right_hand)


num_list = [1, 3, 5, 2, 68, 4, 5, 6, 6, 69]
print(quick_sort(num_list))
