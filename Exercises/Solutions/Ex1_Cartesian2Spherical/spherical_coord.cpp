#include <cmath>
#include <iostream>
#include <complex>

using namespace std;

const double PI = 3.1415926535897931;

const double RAD2DEG = 180.0/PI;

// Convert Cartesian coordinates to spherical coordinates
int main()
{
  // Declaration of Coordinates to be converted
  double x, y, z;

  //print message on the screen
  std::cout << "Enter Value of X coordinate: " ;
  // to store user entered value for x coordinate
  std::cin >> x;

  //print message on the screen
  std::cout << "Enter Value of Y coordinate: " ;
  // to store user entered value for y coordinate
  std::cin >> y;

  //print message on the screen
  std::cout << "Enter Value of Z coordinate: " ;
  // to store user entered value for z coordinate
  std::cin >> z;

  // Norm
  double r = sqrt(x*x + y*y + z*z);

  // Longitude
  double phi = atan2(y, x);
  phi = phi < 0 ? phi + 2*PI : phi;

  // Colatitude
  double theta = acos(z/r);

  cout << "Longitude = " << phi*RAD2DEG << " deg, Colatitude = "
       << theta*RAD2DEG << " deg, Radius = " << r << endl;

  return 0;
}
