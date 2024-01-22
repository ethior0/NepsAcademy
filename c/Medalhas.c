#include <stdio.h>

int main() {

    int t1, t2, t3;
    scanf("%d%d%d", &t1, &t2, &t3);

    if (t1 < t2 && t1 < t3) {
        printf("%d\n", 1);
        if (t2 < t3) {
            printf("%d\n", 2);
            printf("%d\n", 3);
        } else {
            printf("%d\n", 3);
            printf("%d\n", 2);
        }
    } else if (t2 < t1 && t2 < t3) {
        printf("%d\n", 2);
        if (t1 < t3) {
            printf("%d\n", 1);
            printf("%d\n", 3);
        } else {
            printf("%d\n", 3);
            printf("%d\n", 1);
        }
    } else if (t3 < t1 && t3 < t2) {
        printf("%d\n", 3);
        if (t1 < t2) {
            printf("%d\n", 1);
            printf("%d\n", 2);
        } else {
            printf("%d\n", 2);
            printf("%d\n", 1);
        }
    }
}
