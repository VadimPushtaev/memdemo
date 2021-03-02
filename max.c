#include <stdbool.h>


int max(int *array, int len) {
    int m;

    bool first = true;
    for (int i = 0; i < len; i++) {
        if (first || array[i] > m) {
            m = array[i];
        }
        first = false;
    }

    return m;
}
