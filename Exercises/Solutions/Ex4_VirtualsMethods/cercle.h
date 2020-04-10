#ifndef __CERCLE_H__
#define __CERCLE_H__

#include "shape.h"
#include "point.h"

class Cercle: public Figure{
public:
    // Fonctions membres spéciales:
    Cercle();
    Cercle(const Cercle& rhs);
    const Cercle& operator=(const Cercle& rhs);
    virtual ~Cercle();

    Cercle(Point centre, float rayon);

    virtual void afficher_info()const;
    virtual float perimetre()const;
    virtual float surface()const;
private:
    Point centre;
    float rayon;
};

#endif//__CERCLE_H__

