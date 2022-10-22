def test_round_down():
    text = '    kkkk    '
    assert text.strip() == 'kkkk'


def test_round_down2():
    text = '    kkkk'
    assert text.strip('s') == '    kkkk'


def test_round_down3():
    text = 'kkkk    fff'
    assert text.strip('f') == 'kkkk    '


def test_round_down4():
    text = 'kkkk'
    assert text.strip() == 'kkkk'


def test_round_down5():
    text = 'kkkk'
    assert text.strip('k') == ''
