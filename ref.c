#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define GB 1024*1024*1024


int main() {
    void *a, *b, *c;

    printf("Press any key to allocate 3*1GB\n");
    getchar();

    a = malloc(GB);
    b = malloc(GB);
    c = malloc(GB);

    printf("Press any key to copy memory\n");
    getchar();
    memcpy(b, a, GB);
    
    printf("Press any key to copy memory back\n");
    getchar();
    memcpy(a, b, GB);

    printf("Press any key to copy memory back\n");
    getchar();
    memcpy(c, b, GB);

    printf("Press any key to finish\n");
    getchar();
}
