SUFFIXES = {1024: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1000: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size o human-readable form.

    :param size: file size in bytes
    :param a_kilobyte_is_1024_bytes: if Ture(default), use multiples of 1024. if False, use multiples of 1000
    :return: string
    '''

    if size < 0:
        raise ValueError('number must be non-negative')
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:0.1f} {1}'.format(size, suffix)
    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate_size(1000))
    print(approximate_size(1000, False))
    print(approximate_size(8192))
    print(approximate_size(8192, False))
    print(approximate_size(1000000000000))
    print(approximate_size(1000000000000, False))
    print(approximate_size(3000000000000))
    print(approximate_size(3000000000000, False))
