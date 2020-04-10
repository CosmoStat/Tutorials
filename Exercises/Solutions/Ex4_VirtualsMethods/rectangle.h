#ifndef __RECTANGLE_H__
#define __RECTANGLE_H__

#include <math.h>
#include "point.h"
#include "shape.h"


class Rectangle: public Figure{
public:
    // Ctors:
    Rectangle();
    Rectangle(const Point& p1, const Point& p2);
    Rectangle(const Rectangle& rhs);

    // Dtor:
    virtual ~Rectangle(); // Made non-virtual on purpose

    // Assignment
    const Rectangle& operator =(const Rectangle& rhs);

    // Accesseur(s)
    virtual void afficher_info()const;
    virtual float perimetre()const;
	virtual float surface()const;

    // Modificateur(s)
    void deplacer(float dx, float dy);

private:
    Point p1;
    Point p2;

    float largeur()const {return fabs(p1.getX()-p2.getX());}
    float hauteur()const {return fabs(p1.getY()-p2.getY());}
};

#endif // __RECTANGLE_H__
