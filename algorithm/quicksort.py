listArray = [1, 3, 5, 2, 6, 4, 5, 6, 6, 69]
def quickSort(list):
    if(not list or len(list) == 1):
        return list
    pivot = list[0]
    leftHand = []
    rightHand = []
    for item in list[1:]:
        if pivot > item:
            leftHand.append(item)
        else:
            rightHand.append(item)
    return quickSort(leftHand) + [pivot] + quickSort(rightHand)


print(quickSort(listArray))

