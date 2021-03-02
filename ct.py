import ctypes


def c_max(lst):
    max_so = ctypes.cdll.LoadLibrary("./max.so")
    array_type = ctypes.c_int * len(lst)
    result = max_so.max(array_type(*lst), ctypes.c_int(len(lst)))

    return result


assert 10 == c_max([10])
assert 10 == c_max([7, 10, 5, 4, -2])
assert 10 == c_max([10, 10, 10])
assert 10 == c_max([-10, 10])

print('ok')
