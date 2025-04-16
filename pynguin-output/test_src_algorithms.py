# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src.algorithms as module_0


def test_case_0():
    str_0 = "Price cannot be negative"
    var_0 = module_0.binary_search(str_0, str_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    var_0 = module_0.binary_search(dict_0, dict_0)
    assert var_0 == -1
    module_0.fibonacci(dict_0)


def test_case_2():
    float_0 = -4487.643836
    with pytest.raises(ValueError):
        module_0.fibonacci(float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1
    var_0 = module_0.fibonacci(int_0)
    assert var_0 == 1
    bool_0 = False
    var_1 = module_0.fibonacci(bool_0)
    assert var_1 is False
    var_2 = module_0.fibonacci(int_0)
    var_3 = module_0.fibonacci(var_2)
    module_0.binary_search(var_3, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 216
    var_0 = module_0.fibonacci(int_0)
    assert var_0 == 619220451666590135228675387863297874269396512
    list_0 = []
    module_0.fibonacci(list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"=\xb9\x01\xf0}"
    bool_0 = True
    var_0 = module_0.binary_search(bytes_0, bool_0)
    assert var_0 == 2
    str_0 = "Price cannot be negative"
    module_0.fibonacci(str_0)
