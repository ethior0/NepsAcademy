#include <stdio.h>
#include <string.h>

int main() {

    char S[50];
    scanf("%s", S);

    printf("Vogais: ");
    for (int i = 0; i < strlen(S); i++) {

        switch(S[i]) {
        case 'a':
            printf("%c", S[i]);
            break;
        case 'e':
            printf("%c", S[i]);
            break;
        case 'i':
            printf("%c", S[i]);
            break;
        case 'o':
            printf("%c", S[i]);
            break;
        case 'u':
            printf("%c", S[i]);
            break;
        }
    }

    printf("\nConsoantes: ");
    for (int j = 0; j < strlen(S); j++) {
        if (S[j] != 'a') {
            if (S[j] != 'e') {
                if (S[j] != 'i') {
                    if (S[j] != 'o') {
                        if (S[j] != 'u') {
                            printf("%c", S[j]);
                        }
                    }
                }
            }
        }
    }

}
