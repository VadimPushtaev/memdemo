run-brk: brk
	./brk

run-mmap:
	python mmap_script.py

run-anon: anon
	./anon

brk: brk.c
	gcc -std=c99 brk.c -o brk

anon: anon.c
	gcc -std=c99 anon.c -o anon

