def find_last_string(given_list, skip_first=1, need_cleaning=False):
    if skip_first > len(given_list):
        raise ValueError('Skip-number is greater than the number of items!')
    if need_cleaning:
        g_list = []
        for _ in given_list:
            g_list.append(_.strip())
    else:
        g_list = given_list
    item_index = 0
    start_index = skip_first - 1
    g_list[start_index:]
    for curr_item in g_list:
        if type(curr_item) == str and curr_item != '':
            item_index = g_list.index(curr_item)
    if item_index == 0:
        raise ValueError('All items are empty strings!')
    return item_index
