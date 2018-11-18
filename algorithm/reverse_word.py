import string


def reverse(sentence):
    return sentence[::-1]


def reverse_by_word(sentence):
    result = ''
    word = ''
    for char in sentence:
        if (char in string.punctuation) or char == ' ':
            result += word
            result += char
            word = ''
        else:
            word = char + word
    if word != '':
        result += word

    return result


one_sentence = "I am Hao."
print(one_sentence)
print(reverse(one_sentence))
print(reverse_by_word(reverse(one_sentence)))
