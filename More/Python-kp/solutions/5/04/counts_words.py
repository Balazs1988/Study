def counts_words(words_list):
    words_dict = {}
    for word in words_list:
        count = words_list.count(word)
        words_dict[word] = count
    return words_dict
