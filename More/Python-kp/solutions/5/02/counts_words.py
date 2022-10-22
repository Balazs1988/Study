def counts_words(given_tuple, is_first=False):
    if len(given_tuple) == 0:
        raise ValueError('Empty tuple!')
    count = 0
    if is_first:
        for _ in given_tuple:
            if type(_) == str and 'L' == _[0]:
                count += 1
    else:
        for _ in given_tuple:
            if type(_) == str and 'L' in _:
                count += 1
    return count
