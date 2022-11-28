#include <stdio.h>
#include "fish.h"

void catalog(fish f) {
    printf("%s - это %s с %d зубами, ему %d лет\n",
    f.name, f.species, f.teeth, f.age);
}
void label(fish f) {
    printf("Кличка:%s\nРазновидность:%s\n%i года, %i зубов\n",
    f.name, f.species, f.teeth, f.age);
    printf("Давать %2.2f кг %s и разрешать %s на протяжении %2.2f часов\n",
    f.care.food.weight, f.care.food.ingredients,
    f.care.exercise.description, f.care.exercise.duration);
}