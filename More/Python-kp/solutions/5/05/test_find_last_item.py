import find_last_item


def test_find_last_item_3():
    given_list = ['zero', 'one', 'two', 'three', '']
    assert find_last_item.find_last_string(given_list) == 3


def test_find_last_item_5():
    given_list = ['zero', 'one', 'two', 'three', '', 'five']
    assert find_last_item.find_last_string(given_list) == 5


def test_find_last_item_none():
    given_list = ['']
    assert find_last_item.find_last_string(given_list) == ValueError


def test_find_last_item_none2():
    given_list = ['']
    assert find_last_item.find_last_string(given_list, 2) == ValueError


def test_find_last_item_5a():
    given_list = ['', 'one', 'two', 'three', '', 'five']
    assert find_last_item.find_last_string(given_list, 3) == 5


def test_find_last_item_strip():
    given_list = ['', ' one', ' two ', 'three', '', 'five    ']
    assert find_last_item.find_last_string(given_list, 3, True) == 5
