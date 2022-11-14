#include <stdio.h>

void fortune_cookie(char msg[]) {
    printf("Сообщение гласит: %s\n", msg);
    printf("Длинна сообщения: %lu\n", sizeof(msg));
}

int main() {
    char quotes[] = "Печенье вас полнит";
    fortune_cookie(quotes);

    return 0;
}