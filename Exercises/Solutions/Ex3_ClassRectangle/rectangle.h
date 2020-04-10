#ifndef __RECTANGLE_H__
#define __RECTANGLE_H__

#include "point.h"

class Rectangle{
public:
    // Ctors:
    Rectangle();
    Rectangle(const Point& p1, const Point& p2);
    Rectangle(const Rectangle& rhs);

    // Dtor:
    ~Rectangle(); // Made non-virtual on purpose

    // Assignment
    const Rectangle& operator =(const Rectangle& rhs);

    // Accesseur(s)
    void afficher_info()const;


    // Modificateur(s)
    void deplacer(float dx, float dy);

private:
    Point p1;
    Point p2;
};

#endif // __RECTANGLE_H__
