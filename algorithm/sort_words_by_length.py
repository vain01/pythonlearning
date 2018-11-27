def sort_by_length(words):
    tmp_list = []
    for word in words:
        tmp_list.append((len(word), word))

    tmp_list.sort(reverse=True)

    res = []
    for length, word in tmp_list:
        res.append(word)

    return res


word_list = ['Hi', 'Hello', 'Go', 'fine', 'Fine', 'fine', 'small', 'hi']
print(sort_by_length(word_list))
