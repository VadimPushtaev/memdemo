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

input("Press any key to create huge dict")
d = {x: [x] for x in range(10_000_000)}

input("Press any key to fork")
parent_conn, child_conn = Pipe()
if os.fork():
    input("Press any key to collect")
    collect()

    input("Press any key to finish")
    parent_conn.send('x')

else:
    setproctitle.setproctitle('FORK huge_dict_gc')
    child_conn.recv()


