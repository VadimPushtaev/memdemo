import random
from multiprocessing import Pipe
import setproctitle
import gc
import mmap
import os

def collect():
    gc.collect(0)
    gc.collect(1)
    gc.collect(2)

gc.disable()
pid = os.getpid()

print(f'/proc/{pid}/')

input("Press any key to create huge bytearray")
d = bytearray(b'0123456789' * 100_000_000)

input("Press any key to fork")
parent_conn, child_conn = Pipe()
if os.fork():
    input("Press any key to collect")
    collect()

    input("Press any key to touch")
    parent_conn.send('x')
    for _ in d:
        pass

    input("Press any key to finish")
    parent_conn.send('x')

else:
    setproctitle.setproctitle('FORK good')

    child_conn.recv()
    for _ in d:
        pass

    child_conn.recv()

