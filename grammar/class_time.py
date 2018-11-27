class Time:
    """
    表示一天的时间

    属性:小时hour,分钟minute,秒second
    """


time = Time()
time.hour = 12
time.minute = 3
time.second = 8
time.millisecond = 33

print(time)
print('{0}:{1}:{2}'.format(time.hour, time.minute, time.second))
print('%.2d:%.2d:%.2d:%.3d' % (time.hour, time.minute, time.second, time.millisecond))
