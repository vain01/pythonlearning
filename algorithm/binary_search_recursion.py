def search(nums, key):
    if not nums or not key:
        return None
    return search_recursion(nums, 0, len(nums) - 1, key)


def search_recursion(nums, low_index, high_index, key):
    if not nums or low_index > high_index or not key:
        return None
    mid = (low_index + high_index) // 2
    if key < nums[mid]:
        return search_recursion(nums, low_index, high_index - 1, key)
    elif nums[mid] < key:
        return search_recursion(nums, low_index + 1, high_index, key)
    else:
        return mid


num_list = [3, 4, 5, 6, 7, 8, 33, 66]
num = 3
print(search(num_list, num))
