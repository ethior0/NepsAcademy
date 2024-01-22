#include <stdio.h>
#include <string.h>

int main() {

    int cc = 0;
    char S[50];
    char C;

    scanf("%s %c", S, &C);

    for (int i = 0; i < strlen(S); i++) {
        if (S[i] == C) cc++;
    }

    printf("%d", cc);
}
