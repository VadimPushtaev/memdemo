from multiprocessing import Pipe
import setproctitle
import gc
import mmap
import os

gc.disable()
pid = os.getpid()

print(f'/proc/{pid}/')

input("Press any key to create huge dict")
d = {x: x for x in range(10_000_000)}

input("Press any key to fork")
parent_conn, child_conn = Pipe()
if os.fork():
    input("Press any key to touch dict")
    for _ in d.keys():
        pass

    input("Press any key to finish")
    parent_conn.send('x')

else:
    setproctitle.setproctitle('FORK huge_dict')
    child_conn.recv()

