class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Input:')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('You triggered Ctrd+D')
except KeyboardInterrupt:
    print('You triggered Ctrl+C')
except ShortInputException:
    print('Your text was {0} long, expected at least {1}.'.format(len(text), 3))
else:
    print('No exception was raised.')
