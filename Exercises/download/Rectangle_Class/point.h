#ifndef __POINT_H__
#define __POINT_H__


class Point{
    public:
    // Fonctions membres spéciales:
    Point(); // Constructeur par défaut
    Point(const Point& rhs); // Constructeur de recopie
    const Point& operator=(const Point& rhs); // Affectation
    ~Point(); // Le destructeur est expressement non-virtuel!

    // Constructeur exaustif
    Point(float x, float y);

    // Accesseurs:
    float getX()const;
    float getY()const;

    private:
    float x, y;
};

#endif // __POINT_H__
