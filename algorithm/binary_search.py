def search(list_nums, expected_key):
    lo = 0
    hi = len(list_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print('猜测中:{0}'.format(list_nums[mid]))
        if expected_key < list_nums[mid]:
            hi = mid - 1
        elif list_nums[mid] < expected_key:
            lo = mid + 1
        else:
            return mid


testing = (3, 5, 6, 7, 8, 9, 11)
key = 6
print(search(testing, key))
