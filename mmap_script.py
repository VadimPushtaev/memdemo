import mmap
import os

pid = os.getpid()

print(f'/proc/{pid}/')
input("Press any key to map 1GB")

with open('/mnt/vdb/1GB', 'r+b') as f:
    mm = mmap.mmap(f.fileno(), 0)

    input("Press any key to touch mapped file")
    while True:
        line = mm.readline()
        if not line:
            break

    input("Press any key to touch mapped file again")
    mm.seek(0)
    while True:
        line = mm.readline()
        if not line:
            break

    input("Press any key to map and touch another 1GB")
    with open('/mnt/vdb/1GB', 'r+b') as g:
        mm2 = mmap.mmap(g.fileno(), 0)
        while True:
            line = mm2.readline()
            if not line:
                break

    input("Press any key to unmap (first only)")
    mm.close()

input("Press any key to finish")
mm2.close()
