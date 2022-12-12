#ifndef __FIND_H
#define __FIND_H

#include <stdio.h>
#include <string.h>


void find(int(*match)(char*));
int sports_no_bieber(char*);
int sports_or_workingout(char*);
int ns_theater(char*);
int arts_theater_or_dining(char*);

#endif