#define _GNU_SOURCE
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

#define GB 1024*1024*1024



int main(int argc, char *argv[]) {
    char s[1024];
    int pipe[2];
    pipe2(pipe, 0);

    printf("Press any key to allocate 1GB\n");
    getchar();

    void* addr = mmap(NULL, GB, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, 0, 0);
    
    if (fork()) {
        printf("Press any key to touch 1GB\n");
        getchar();

        write(pipe[1], "x", 1);
        for (int i=0; i < GB - 1024; i += 1024) {
            memcpy(s, addr + i, 1024);
        }

        printf("Press any key to modify\n");
        getchar();

        write(pipe[1], "x", 1);
        for (int i=0; i < GB - 1024; i += 1024) {
            memcpy(addr + i, "foo", 3);
        }

        printf("Press any key to unmap\n");
        getchar();

        munmap(addr, GB);

        printf("Press any key to finish\n");
        getchar();

        write(pipe[1], "x", 1);
    }
    else {
        argv[0][0] = 'F';
        char buf[1];
        read(pipe[0], buf, 1);  // touch now
        for (int i=0; i < GB - 1024; i += 1024) {
            memcpy(s, addr + i, 1024);
        }

        read(pipe[0], buf, 1);  // modify now
        for (int i=0; i < GB - 1024; i += 1024) {
            memcpy(addr + i, "bar", 3);
        }

        read(pipe[0], buf, 1);  // end now
    }
}
