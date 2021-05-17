from aski import двоцифрени


def test0():
    assert двоцифрени([64, 65, 66]) == '@AB'


def test1():
    assert двоцифрени(list(range(27, 33))) == ''


def test2():
    assert двоцифрени([-3, -2, -1]) == ''


def test3():
    assert двоцифрени([100, 101, 200, 3000]) == ''


def test4():
    assert двоцифрени(list(range(33, 100))) == '!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abc'

