#ifndef __FISH_H
#define __FISH_H


typedef struct exercise {
    const char *description;
    float duration;
} cise;

typedef struct meal {
    const char *ingredients;
    float weight;
} meal;

typedef struct preferensec {
    struct meal food;
    struct exercise exercise;
} preferensec;

typedef struct fish {
    const char *name;    
    const char *species;
    int teeth;
    int age;
    struct preferensec care;
} fish;

void catalog(fish);
void label(fish);

#endif
