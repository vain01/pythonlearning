import sys, warnings

if sys.version_info[0] < 3:
    warnings.warn('Your phthon version is less than 3', RuntimeWarning)
else:
    print('Proceed is normal')
