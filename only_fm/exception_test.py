class Time:
    """
    时间类
    """


def valid_time(time):
    if time.second < 0 or time.minute < 0 or time.hour < 0:
        return False
    if time.minute > 60 or time.hour > 24:
        return False
    return True


def add_time(t1, t2):
    # assert valid_time(t2)
    if not valid_time(t1) or not valid_time(t2):
        raise (ValueError, "Time value error")
    # todo


t = Time()
t.hour = 3
t.minute = 7
t.second = 10

ta = Time()
ta.hour = 14
ta.minute = 5
ta.second = 11

add_time(t, ta)
