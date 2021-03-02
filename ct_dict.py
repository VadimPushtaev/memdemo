from multiprocessing import Pipe
import setproctitle
import gc
import mmap
import os
import ctypes


class CppDict:
    _so = None

    @classmethod
    def init_so(cls):
        if cls._so is None:
            cls._so = ctypes.cdll.LoadLibrary("./dict.so")
            cls._so.make_dict.argtypes = []
            cls._so.set_value.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
            cls._so.get_value.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
            cls._so.get_value.restype = ctypes.c_char_p

    def __init__(self):
        self.init_so()
        self._d = self._so.make_dict()

    def __getitem__(self, key):
        return self._so.get_value(self._d, key)

    def __setitem__(self, key, value):
        return self._so.set_value(self._d, key, value)

N = 1_000_000


gc.disable()
pid = os.getpid()

print(f'/proc/{pid}/')

d = CppDict()
input("Press any key to create huge dict")
for x in range(N):
    d[f'key_{x}'.encode('latin1')] = f'value_{x}'.encode('latin1')

input("Press any key to fork")
parent_conn, child_conn = Pipe()
if os.fork():
    input("Press any key to touch dict")
    for x in range(N):
        y = d[f'key_{x}'.encode('latin1')]

    input("Press any key to finish")
    parent_conn.send('x')

else:
    setproctitle.setproctitle('FORK ct_dict')
    child_conn.recv()

