class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, other):
        seconds = self.time_to_int() + other
        return int_to_time(seconds)


def int_to_time(seconds):
    ret = Time()
    ret.minute, ret.second = divmod(seconds, 60)
    ret.hour, ret.minute = divmod(ret.minute, 60)
    return ret


start = Time(9, 45)
print(start)
print(start.hour)
print(start.minute)
print(start.second)
duration = Time(1, 25)
end = start + duration
print(end)
print(70 + Time())

total = sum([start, duration, end])
print(total)

