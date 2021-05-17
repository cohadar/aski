import sys


def ок(број):
    if број < 0 or број >= 100:
        return False
    if број >= 27 and број < 33:
        return False
    if број in [34, 39, 96]:
        return False
    return True


def транс(број):
    return 100 + број if број < 27 else број


def двоцифрени(ндб):
    return ''.join(chr(транс(број)) for број in ндб if ок(број))


def main():
    print(двоцифрени(int(линија) for линија in sys.stdin))

