#include <stdio.h>
int main(int argc, char *argv[]) {
    char *feeds[] = {"http://wsasddsasdd/adssa/asdasd.xml","http://wsasddsasadd/adfssa/asdasd.xml","http://wssasddsasdd/adssa/asdasd.xml"};
    
    int times = 3;
    char *pharase = argv[1];
    int i;
    for (i = 0; i < times; i++) {
        char var[255];
        sprintf(var, "RSS_FEED=%s", feeds[i]);
        char *vars[] = {var, NULL};
        pid_t pid = fork();
        if (pid == -1) {
            fprintf(stderr, "Не могу клонировать процесс: %s\n", strerror(errno));
            return 1;
        }
        if (!pid) {
            if (execle("/usr/bin/python", "/usr/bin/python", "./rssgossip.py", phrase, NULL, vars) == -1) {
            fprintf(stderr, "Не могу запустить скрипт: %s\n", strerror(errno));
            return 1;
         }
        }
    }
}