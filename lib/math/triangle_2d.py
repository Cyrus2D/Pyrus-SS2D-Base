"""
  \ file triangle_2d.py
  \ brief 2D triangle class File.
"""

from lib.math.segment_2d import *
from lib.math.region_2d import *
from lib.math.ray_2d import *


class Triangle2D(Region2D):
    """
        Len = 3 / Vector2D
      \ brief constructor with  OR def with (0,0) , (0,1) , (1,0)
      \ param v1 first vertex point
      \ param v2 second vertex point
      \ param v3 third vertex point
            Len = 2 / Segment2D
      \ brief constructor with a segment and a point
      \ param seg segment consist of triangle, and second vertex points
      \ param v third vertex point
    """

    def __init__(self, *args):  # , **kwargs):):):
        super().__init__()
        if len(args) == 3 and isinstance(args[0], Vector2D):
            self._a = args[0]
            self._b = args[1]
            self._c = args[2]
        elif len(args) == 2 and isinstance(args[0], Segment2D):
            seg = args[0]
            self._a = seg.origin()
            self._b = seg.terminal()
            self._c = args[1]

    """
        Len = 3 / Vector2d
      \ brief assign vertex points
      \ param v1 first vertex point
      \ param v2 second vertex point
      \ param v3 third vertex point
      \ return  reference to itself
        Len = 2 / Segment2D
      \ brief assign segment and vertex point
      \ param seg segment consist of triangle, and second vertex points
      \ param v third vertex point
      \ return  reference to itself
    """

    def assign(self, *args):  # , **kwargs):):):
        if len(args) == 3 and isinstance(args[0], Vector2D):
            self._a = args[0]
            self._b = args[1]
            self._c = args[2]
        elif len(args) == 2 and isinstance(args[0], Segment2D):
            seg = args[0]
            self._a = seg.origin()
            self._b = seg.terminal()
            self._c = args[1]

    """
      \ brief check if self triangle is valid or not.
      \ return True if triangle is valid.
    """

    def isValid(self):
        return self._a.is_valid() and self._b.is_valid() and self._c.is_valid() and self._a != self._b and self._b != self._c and self._a != self._a

    """
      \ brief get 1st point
      \ return  reference to the member variable
     """

    def a(self):
        return self._a

    """
      \ brief get 2nd point
      \ return  reference to the member variable
     """

    def b(self):
        return self._b

    """
      \ brief get 3rd point
      \ return  reference to the member variable
     """

    def c(self):
        return self._c

    """
      \ brief get the area of self region
      \ return value of the area
     """

    def area(self):
        return math.fabs((self._b - self._a).outerProduct(self._c - self._a)) * 0.5

    """
         \ brief get a signed area. self method is equivalent to signed_area().
         \ return signed area value
         If points a, b, are placed counterclockwise order, positive number.
         If points a, b, are placed clockwise order, negative number.
         If points a, b, are placed on a line, 0.
        """

    def signedArea(self):
        return Triangle2D.signed_area(self._a, self._b, self._c)

    """
      \ brief get a double of signed area value. self method is equivalent to double_signed_area().
      \ return double of signed area value
      If points a, b, are placed counterclockwise order, positive number.
      If points a, b, are placed clockwise order, negative number.
      If points a, b, are placed on a line, 0.
     """

    def doubleSignedArea(self):
        return Triangle2D.double_signed_area(self._a, self._b, self._c)

    """
      \ brief check if self triangle's vertices are placed counterclockwise order.
      \ return checked result
     """

    def ccw(self):
        return Triangle2D.tri_ccw(self._a, self._b, self._c)

    """
      \ brief check if self triangle contains 'point'.
      \ param point considered point
      \ return True or False
    """

    def contains(self, point: Vector2D):
        rel1 = Vector2D(self._a - point)
        rel2 = Vector2D(self._b - point)
        rel3 = Vector2D(self._c - point)

        outer1 = rel1.outerProduct(rel2)
        outer2 = rel2.outerProduct(rel3)
        outer3 = rel3.outerProduct(rel1)

        if outer1 >= 0.0 and outer2 >= 0.0 and outer3 >= 0.0 or (outer1 <= 0.0 and outer2 <= 0.0 and outer3 <= 0.0):
            return True
        return False

    """
      \ brief get the center of gravity(centroid)
      \ return coordinates of gravity center
     """

    def centroid(self):
        return Triangle2D.tri_centroid(self._a, self._b, self._c)

    """
      \ brief get the center of inscribed circle
      \ return coordinates of inner center
    """

    def incenter(self):
        return Triangle2D.tri_incenter(self._a, self._b, self._c)

    """
      \ brief get the center of circumscribed circle
      \ return coordinates of outer center
    """

    def circumcenter(self):
        return Triangle2D.tri_circumcenter(self._a, self._b, self._c)

    """
      \ brief get the orthocenter
      \ return coordinates of orthocenter
    """

    def orthocenter(self):
        return Triangle2D.tri_orthocenter(self._a, self._b, self._c)

    """
        Line2D
      \ brief calculate intersection point with line.
      \ param line considered line.
      \ return number of intersection + sol 1 + sol 2
        Ray2D
      \ brief calculate intersection point with ray.
      \ param ray considered ray line.
      \ return number of intersection + sol 1 + sol 2
        Segment2D
      \ brief calculate intersection point with line segment.
      \ param segment considered line segment.
      \ return number of intersection + sol 1 + sol 2
    """

    def intersection(self, *args):  # , **kwargs):):):
        if len(args) == 1 and isinstance(args[0], Line2D):
            line = args[0]
            n_sol = 0
            t_sol = [Vector2D(), Vector2D()]

            t_sol[n_sol] = Segment2D(self._a, self._b).intersection(line)
            if n_sol < 2 and t_sol[n_sol].is_valid():
                n_sol += 1

            t_sol[n_sol] = Segment2D(self._b, self._c).intersection(line)
            if n_sol < 2 and t_sol[n_sol].is_valid():
                n_sol += 1

            t_sol[n_sol] = Segment2D(self._c, self._a).intersection(line)
            if n_sol < 2 and t_sol[n_sol].is_valid():
                n_sol += 1

            if n_sol == 2 and math.fabs(t_sol[0]._x - t_sol[1]._x) < EPSILON and math.fabs(
                    t_sol[0]._y - t_sol[1]._y) < EPSILON:
                n_sol = 1
            sol_list = [n_sol, t_sol[0], t_sol[1]]

            return sol_list
        elif len(args) == 1 and isinstance(args[0], Ray2D):
            ray = args[0]
            t_sol1 = Vector2D()
            t_sol2 = Vector2D()
            n_sol = Triangle2D.intersection(ray.line(), t_sol1, t_sol2)

            if n_sol[0] > 1 and not ray.inRightDir(t_sol2, 1.0):
                n_sol[0] -= 1

            if n_sol[0] > 0 and not ray.inRightDir(t_sol1, 1.0):
                t_sol1 = t_sol2
                n_sol[0] -= 1

            sol_list = [n_sol[0], t_sol1, t_sol2]

            return sol_list

        elif len(args) == 1 and isinstance(args[0], Segment2D):
            segment = args[0]
            t_sol1 = Vector2D()
            t_sol2 = Vector2D()
            n_sol = Triangle2D.intersection(segment.line(), t_sol1, t_sol2)

            if n_sol > 1 and not segment.contains(t_sol2):
                n_sol -= 1

            if n_sol > 0 and not segment.contains(t_sol1):
                t_sol1 = t_sol2
                n_sol -= 1
            sol_list = [n_sol, t_sol1, t_sol2]

            return sol_list

    """  ----------------- static method  ----------------- """

    """
      \ brief get a double signed area value (== area of parallelogram)
      \ param a 1st input point
      \ param b 2nd input point
      \ param c 3rd input point
      \ return double singed area value.
      If points a, b, are placed counterclockwise order, positive number.
      If points a, b, are placed clockwise order, negative number.
      If points a, b, are placed on a line, 0.
    """

    @staticmethod
    def double_signed_area(a: Vector2D, b: Vector2D, c: Vector2D):
        return ((a._x - c._x) * (b._y - c._y)
                + (b._x - c._x) * (c._y - a._y))

    """
      \ brief get a signed area value
      \ param a 1st input point
      \ param b 2nd input point
      \ param c 3rd input point
      \ return signed area value
      If points a, b, are placed counterclockwise order, positive number.
      If points a, b, are placed clockwise order, negative number.
      If points a, b, are placed on a line, 0.
     """

    @staticmethod
    def signed_area(a: Vector2D, b: Vector2D, c: Vector2D):
        return Triangle2D.double_signed_area(a, b, c) * 0.5

    """
       \ brief check if input vertices are placed counterclockwise order.
       \ param a 1st input point
       \ param b 2nd input point
       \ param c 3rd input point
       \ return checked result
      """

    @staticmethod
    def tri_ccw(a: Vector2D, b: Vector2D, c: Vector2D):
        return Triangle2D.double_signed_area(a, b, c) > 0.0

    """
      \ brief get the center of gravity
      \ param a triangle's 1st vertex
      \ param b triangle's 2nd vertex
      \ param c triangle's 3rd vertex
      \ return coordinates of gravity center

      centroid = (a + b + c) / 3
     """

    @staticmethod
    def tri_centroid(a: Vector2D, b: Vector2D, c: Vector2D):
        return Vector2D(a).add(b).add(c) / 3.0

    """
      \ brief get the incenter point
      \ param a triangle's 1st vertex
      \ param b triangle's 2nd vertex
      \ param c triangle's 3rd vertex
      \ return coordinates of incenter
    """

    @staticmethod
    def tri_incenter(a: Vector2D, b: Vector2D, c: Vector2D):
        ab = b - a
        ac = c - a
        bisect_a = Line2D(a, AngleDeg.bisect(ab.th(), ac.th()))

        ba = a - b
        bc = c - b
        bisect_b = Line2D(b, AngleDeg.bisect(ba.th(), bc.th()))

        return bisect_a.intersection(bisect_b)

    """
      \ brief get the circumcenter point
      \ param a triangle's 1st vertex
      \ param b triangle's 2nd vertex
      \ param c triangle's 3rd vertex
      \ return coordinates of circumcenter
    """

    @staticmethod
    def tri_circumcenter(a: Vector2D, b: Vector2D, c: Vector2D):

        perpendicular_ab = Line2D.perpendicular_bisector(a, b)
        perpendicular_bc = Line2D.perpendicular_bisector(b, c)

        sol = perpendicular_ab.intersection(perpendicular_bc)

        if not sol.is_valid():
            perpendicular_ca = Line2D.perpendicular_bisector(c, a)

            sol = perpendicular_ab.intersection(perpendicular_ca)

            if sol.is_valid():
                return sol

            sol = perpendicular_bc.intersection(perpendicular_ca)

            if sol.is_valid():
                return sol

        ab = b - a
        ca = c - a

        tmp = ab.outerProduct(ca)
        if math.fabs(tmp) < 1.0e-10:  # The area of parallelogram is 0.
            return Vector2D.invalid()

        inv = 0.5 / tmp
        ab_len2 = ab.r2()
        ca_len2 = ca.r2()
        xcc = inv * (ab_len2 * ca.y - ca_len2 * ab.y)
        ycc = inv * (ab.x * ca_len2 - ca.x * ab_len2)

        return Vector2D(a._x + xcc, a._y + ycc)

    """
      \ brief get the orthocenter point
      \ param a triangle's 1st vertex
      \ param b triangle's 2nd vertex
      \ param c triangle's 3rd vertex
      \ return coordinates of orthocenter
    
      orthocenter = a + b + c - 2 * circumcenter
    """

    @staticmethod
    def tri_orthocenter(a: Vector2D, b: Vector2D, c: Vector2D):
        perpend_a = Line2D(b, c).perpendicular(a)
        perpend_b = Line2D(c, a).perpendicular(b)
        return perpend_a.intersection(perpend_b)

    """
      \ brief check if triangle(a,b,c) contains the point 'p'.
      \ param a vertex1
      \ param b vertex2
      \ param c vertex3
      \ param point checked point
      \ return checked result
    """

    @staticmethod
    def tri_contains(a: Vector2D, b: Vector2D, c: Vector2D, point: Vector2D):
        rel1 = Vector2D(a - point)
        rel2 = Vector2D(b - point)
        rel3 = Vector2D(c - point)

        outer1 = rel1.outerProduct(rel2)
        outer2 = rel2.outerProduct(rel3)
        outer3 = rel3.outerProduct(rel1)

        if outer1 >= 0.0 and outer2 >= 0.0 and outer3 >= 0.0 or (outer1 <= 0.0 and outer2 <= 0.0 and outer3 <= 0.0):
            return True
        return False

    """
      \ brief make a logical print.
      \ return print_able str
    """

    def __repr__(self):
        return "{[],[],[]}".format(self._a, self._b, self._c)


def test():
    tri = Triangle2D()
    print(tri)


if __name__ == "__main__":
    test()
