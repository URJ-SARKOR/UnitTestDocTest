import unittest


def umnojenie(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a * b


def plus(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a + b


def minus(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a - b


def delenie(a: int, b: int):
    if type(a) != int:
        return 'Error'
    return a / b


class Test(unittest.TestCase):
    def test_umnojenie(self):
        self.assertEqual(umnojenie(15, 3), 45, 'Ошибка !')

    def test_plus(self):
        self.assertEqual(plus(55, 55), 110, 'Что за фигня ?')

    def test_minus(self):
        self.assertEqual(minus(60, 15), 45, 'Ошибка может попробуешь еще ?')

    def test_delenie(self):
        self.assertEqual(delenie(55, 11), 5, 'Ошибка!')
