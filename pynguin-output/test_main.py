# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import main as module_0


def test_case_0():
    int_0 = -1773
    str_0 = module_0.triangle(int_0, int_0, int_0)
    assert str_0 == "Equilateral triangle"


def test_case_1():
    bytes_0 = b"\xb7\xe8\xca\xa3\xd5\x8a,\x92\xec!\xd5tw \xe7"
    bool_0 = True
    str_0 = module_0.triangle(bytes_0, bool_0, bool_0)
    assert str_0 == "Isosceles triangle"


def test_case_2():
    none_type_0 = None
    int_0 = -2616
    str_0 = module_0.triangle(none_type_0, none_type_0, int_0)
    assert str_0 == "Isosceles triangle"


def test_case_3():
    bool_0 = True
    int_0 = -764
    bool_1 = False
    str_0 = module_0.triangle(bool_0, int_0, bool_1)
    assert str_0 == "Scalene triangle"
