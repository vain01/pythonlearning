import string


def reverse(sentence):
    return sentence[::-1]


def reverse_by_word(sentence):
    ret = ''
    word = ''

    for char in sentence:
        if (char in string.punctuation) or char == ' ':
            ret += word
            ret += char
            word = ''
        else:
            word = char + word

    if word != '':
        ret += word

    return ret


origin_sentence = "I am Hao."
print(origin_sentence)
print(reverse(origin_sentence))
print(reverse_by_word(reverse(origin_sentence)))
