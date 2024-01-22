#include <stdio.h>

int main() {

    int L, C;
    scanf("%d%d", &L, &C);

    if (L == C) {
        printf("1");
    } else if (L % 2 == 0 && C % 2 == 0) {
        printf("1");
    } else if (L % 2 != 0 && C % 2 != 0) {
        printf("1");
    } else if (L % 2 == 0 && C % 2 != 0) {
        printf("0");
    } else if (L % 2 != 0 && C % 2 == 0) {
        printf("0");
    }
}
