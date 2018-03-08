import string


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    for item in string.punctuation:
        text = text.replace(item, '')
    return text == reverse(text)


something = input('Input:')
if is_palindrome(something):
    print('Yes. It is a palindrome.')
else:
    print('No. It is not a palindrome')
