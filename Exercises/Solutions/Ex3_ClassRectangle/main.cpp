#include <iostream>
#include "rectangle.h"

using namespace std;

void fonction1(Rectangle r){
    r.afficher_info();
}

void fonction2(const Rectangle& r){
    r.afficher_info();
}

int main()
{
    Point p1(1,2);
    Point p2(2,3);
    Rectangle r1;
    Rectangle r2(p1,p2);
    Rectangle r3=r2;
    r1=r2;
    fonction1(r2);
    fonction2(r2);
    return 0;
}
