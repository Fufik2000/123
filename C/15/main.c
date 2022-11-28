#include <stdio.h>
#include "fish.h"

int main() {
    fish snappy = {"Зубастик", "Пиранья", 69, 6, {{"Мясо",0.2}, {"Платят", 7.5}}};
    label(snappy);
    return 0;
}
