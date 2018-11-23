def search(nums, key):
    if not nums or not key:
        return None
    return search_recursion(nums, 0, len(nums) - 1, key)


def search_recursion(nums, lo, hi, key):
    if not nums or lo > hi or not key:
        return None
    mid = (lo + hi) // 2
    if key < nums[mid]:
        return search_recursion(nums, lo, hi - 1, key)
    elif nums[mid] < key:
        return search_recursion(nums, lo + 1, hi, key)
    else:
        return mid


num_list = [3, 4, 5, 6, 7, 8, 33, 66]
num = 3
print(search(num_list, num))
