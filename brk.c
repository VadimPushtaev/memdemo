#define _XOPEN_SOURCE 500
#include <features.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

#define GB 1024*1024*1024



int main() {
    char s[1024];

    printf("Press any key to allocate 1GB\n");
    getchar();

    void* addr = sbrk(GB);
    printf("Address: %p\n", addr);
    
    printf("Press any key to touch 1GB\n");
    getchar();

    for (int i=0; i < GB - 1024; i += 1024) {
        memcpy(s, addr + i, 1024);
    }

    printf("Press any key to modify 1GB\n");
    getchar();

    for (int i=0; i < GB - 1024; i += 1024) {
        memcpy(addr + i, "foo", 1024);
    }

    printf("Press any key to touch beyond program break\n");
    getchar();

    memcpy(s, addr + GB, 1024);
}
