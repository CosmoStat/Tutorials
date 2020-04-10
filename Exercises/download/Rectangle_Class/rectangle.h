#ifndef __RECTANGLE_H__
#define __RECTANGLE_H__

#include "point.h"

class Rectangle{
public:
    Rectangle(const Point& p1, const Point& p2);

    // Accesseur(s)
    void afficher_info()const;

    // Modificateur(s)
    void deplacer(float dx, float dy);

private:
    Point p1;
    Point p2;
};

#endif // __RECTANGLE_H__
