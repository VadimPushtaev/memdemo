run-brk: brk
	./brk

run-mmap:
	python mmap_script.py

run-anon: anon
	./anon

run-ref: ref
	./ref

run-huge-dict:
	python huge_dict.py

run-huge-dict-gc:
	python huge_dict_gc.py

run-barray:
	python barray.py

run-ct: max.so
	python ct.py

brk: brk.c
	gcc -std=c99 brk.c -o brk

anon: anon.c
	gcc -std=c99 anon.c -o anon

ref: ref.c
	gcc -std=c99 ref.c -o ref

max.so: max.c
	gcc -std=c99 -shared -o max.so -fPIC max.c

