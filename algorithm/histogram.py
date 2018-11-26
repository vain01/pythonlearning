def histogram(nums):
    ret = {}
    for item in nums:
        ret[item] = ret.get(item, 0) + 1
    return ret


num_list = [1, 3, 5, 2, 6, 4, 5, 6, 6, 69]
print(histogram(num_list))
