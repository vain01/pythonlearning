def search(nums, key):
    low_index = 0
    high_index = len(nums) - 1
    while low_index <= high_index:
        mid = (low_index + high_index) // 2
        print('猜测中:{0}'.format(nums[mid]))
        if key < nums[mid]:
            high_index = mid - 1
        elif nums[mid] < key:
            low_index = mid + 1
        else:
            return mid


num_tuple = (3, 5, 6, 7, 8, 9, 11)
num = 6
print(search(num_tuple, num))
