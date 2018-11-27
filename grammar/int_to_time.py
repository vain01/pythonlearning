class Time:
    pass


def int_to_time(seconds):
    time = Time()

    minutes, time.seconds = divmod(seconds, 60)
    time.hour, time.minutes = divmod(minutes, 60)

    return time


def time_to_int(time):
    minutes = time.hour * 60 + time.minutes
    seconds = minutes * 60 + time.seconds

    return seconds


t = Time()
t.hour = 12
t.minutes = 6
t.seconds = 33

print('{0}:{1}:{2}'.format(t.hour, t.minutes, t.seconds))
int_converted = time_to_int(t)
print(int_converted)
time_converted = int_to_time(int_converted)
print('{0}:{1}:{2}'.format(time_converted.hour, time_converted.minutes, time_converted.seconds))
print(t == int_to_time(time_to_int(t)))
