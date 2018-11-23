def guess(num):
    lo = 1
    hi = 100
    while lo <= hi:
        mid = (lo + hi) // 2
        print('猜测中:{0}'.format(mid))
        if num < mid:
            hi = mid - 1
        elif mid < num:
            lo = mid + 1
        else:
            print('===猜中===:{0}'.format(mid))
            break


your_input_num = int(input('输入你要猜的数(1~100之间的自然数):'))
guess(your_input_num)
