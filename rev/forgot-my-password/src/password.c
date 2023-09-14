#include <stdio.h>
#include <string.h>

int main() {
    char inputPassword[100];  // Assuming the password won't exceed 100 characters

    // Prompt the user for input
    printf("Enter the password: ");
    fgets(inputPassword, sizeof(inputPassword), stdin);

    // Trim newline off the end
    for (int i = 0; i < sizeof(inputPassword); i++) {
        if (inputPassword[i] == '\n') {
            inputPassword[i] = '\0';
            break;
        }
    }

    // Reverse the input password
    int length = strlen(inputPassword);
    char temp;

    for (int i = 0; i < length / 2; i++) {
        temp = inputPassword[i];
        inputPassword[i] = inputPassword[length - i - 1];
        inputPassword[length - i - 1] = temp;
    }

    // Check if the reversed password matches the predefined password
    if (strcmp(inputPassword, "}gn15r3v3r_Desr3vEr{FTCBNU") == 0) {
        printf("That is my password! :)\n");
    } else {
        printf("That's not the password :(\n");
    }

    return 0;
}
