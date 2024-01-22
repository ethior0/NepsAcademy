#include <stdio.h>

int main() {

    int A, B, C;
    scanf("%d%d%d", &A, &B, &C);

    if ( (A == 0 && B == 0 && C == 0) || (A == 1 && B == 1 && C == 1) ) {
        printf("*");
    } else {
        if (A == B) {
            printf("C");
        } else if (B == C) {
            printf("A");
        } else if (C == A) {
            printf("B");
        }
    }
}
