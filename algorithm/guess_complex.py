def guess(num):
    min_num = 1
    max_num = 100
    while min_num <= max_num:
        median = (min_num + max_num) // 2
        print('猜测中:{0}'.format(median))
        if num < median:
            max_num = median - 1
        elif median < num:
            min_num = median + 1
        else:
            print('===猜中===:{0}'.format(median))
            break


guessed_num = int(input('输入你要我猜的数(1~100之间的自然数):'))
guess(guessed_num)
