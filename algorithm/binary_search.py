def search(nums, key):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print('猜测中:{0}'.format(nums[mid]))
        if key < nums[mid]:
            hi = mid - 1
        elif nums[mid] < key:
            lo = mid + 1
        else:
            return mid


num_tuple = (3, 5, 6, 7, 8, 9, 11)
num = 6
print(search(num_tuple, num))
