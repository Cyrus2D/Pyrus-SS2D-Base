"""
  \ file segment_2d.py
  \ brief 2D segment line File.
"""

from lib.math.triangle_2d import *
from lib.math.line_2d import *

CALC_ERROR = 1.0e-9


class Segment2D:
    """
        LEN = 2
      \ brief construct from 2 points
      \ param origin 1st point of segment edge
      \ param terminal 2nd point of segment edge
        LEN = 3
      \ brief construct using origin, and length
      \ param origin origin point
      \ param length length of line segment
      \ param direction line direction from origin point
        LEN = 4
      \ brief construct directly using raw coordinate values
      \ param origin_x 1st point x value of segment edge
      \ param origin_y 1st point x value of segment edge
      \ param terminal_x 2nd point y value of segment edge
      \ param terminal_y 2nd point y value of segment edge
        Len = none
        Default
    """

    def __init__(self, *args):  # , **kwargs):
        if len(args) == 2 and isinstance(args[0], Vector2D) and isinstance(args[1], Vector2D):
            self._origin = args[0]
            self._terminal = args[1]
        elif len(args) == 3 and isinstance(args[0], Vector2D) and isinstance(args[2], AngleDeg):
            self._origin = args[0]
            self._terminal = args[0] + Vector2D.from_polar(args[1], args[2])
        elif len(args) == 4:
            self._origin = Vector2D(args[0], args[1])
            self._terminal = Vector2D(args[2], args[3])
        else:
            self._origin = Vector2D(0, 0)
            self._terminal = Vector2D(0, 0)

    """
        LEN = 2
      \ brief construct from 2 points
      \ param origin first point
      \ param terminal second point
        LEN = 3
      \ brief construct using origin, and length
      \ param origin origin point
      \ param length length of line segment
      \ param direction line direction from origin point
        LEN = 4
      \ brief construct directly using raw coordinate values
      \ param origin_x 1st point x value of segment edge
      \ param origin_y 1st point x value of segment edge
      \ param terminal_x 2nd point y value of segment edge
      \ param terminal_y 2nd point y value of segment edge
        """

    def assign(self, *args):  # **kwargs):
        if len(args) == 2 and isinstance(args[0], Vector2D) and isinstance(args[1], Vector2D):
            self._origin = args[0]
            self._terminal = args[1]
        elif len(args) == 3 and isinstance(args[0], Vector2D) and isinstance(args[2], AngleDeg):
            self._origin = args[0]
            self._terminal = args[0] + Vector2D.from_polar(args[1], args[2])
        elif len(args) == 4:
            self._origin = Vector2D(args[0], args[1])
            self._terminal = Vector2D(args[2], args[3])
        else:
            self._origin = Vector2D(0, 0)
            self._terminal = Vector2D(0, 0)

    """
      \ brief check if self line segment is valid or not.
      origin's coordinates value have to be different from terminal's one.
      \ return checked result.
    """

    def isValid(self):
        return not self._origin.equalsWeakly(self._terminal)

    """
      \ brief get 1st point of segment edge
      \ return  reference to the vector object
    """

    def origin(self):
        return self._origin

    """
      \ brief get 2nd point of segment edge
      \ return  reference to the vector object
    """

    def terminal(self):
        return self._terminal

    """
      \ brief get line generated from segment
      \ return line object
    """

    def line(self):
        return Line2D(self._origin, self._terminal)

    """
      \ brief get the length of self segment
      \ return distance value
    """

    def length(self):
        return self._origin.dist(self._terminal)

    """
      \ brief get the direction angle of self line segment
      \ return angle object
    """

    def direction(self):
        return (self._terminal - self._origin).th()

    """
      \ brief swap segment edge point
      \ return  reference to self object
    """

    def swap(self):
        tmp = self._origin
        self._origin = self._terminal
        self._terminal = tmp

    """
      \ brief swap segment edge point. This method is equivalent to swap(), for convenience.
      \ return  reference to self object
    """

    def reverse(self):
        return self.swap()

    """
      \ brief get the reversed line segment.
      \ return  reference to self object
    """

    def reversedSegment(self):
        return Segment2D(self._origin, self._terminal).reverse()

    """
      \ brief make perpendicular bisector line from segment points
      \ return line object
    """

    def perpendicularBisector(self):
        return Line2D.perpendicular_bisector(self._origin, self._terminal)

    """
      \ brief check if the point is within the rectangle defined by self segment as a diagonal line.
      \ return True if rectangle contains p
    """

    def contains(self, p: Vector2D):
        return ((p._x - self._origin._x) * (p._x - self._terminal._x) <= CALC_ERROR and (p._y - self._origin._y) * (
                p._y - self._origin._y) <= CALC_ERROR)

    """
      \ brief check if self line segment has completely same value as input line segment.
      \ param other compared object.
      \ return checked result.
    """

    def equals(self, other):
        return self._origin.equals(other.self.origin) and self._terminal.equals(other.self.terminal)

    """
     \ brief check if self line segment has weakly same value as input line segment.
     \ param other compared object.
     \ return checked result.
    """

    def equalsWeakly(self, other):
        return self._origin.equalsWeakly(other.self.origin) and self._terminal.equalsWeakly(other.self.terminal)

    """
      \ brief calculates projection point from p
      \ param p input point
      \ return projection point from p. if it does not exist, the invalidated value vector is returned.
    """

    def projection(self, p: Vector2D):
        direction = self._terminal - self._origin
        length = direction.r()

        if length < EPSILON:
            return self._origin

        direction /= length  # normalize

        d = direction.innerProduct(p - self._origin)
        if -EPSILON < d < length + EPSILON:
            direction *= d
            tmp_vec = Vector2D(self._origin)
            tmp_vec += direction
            return tmp_vec

        return Vector2D.invalid()

    """
        LEN = 1
      \ brief check & get the intersection point with other line
      \ param l checked line object
      \ return intersection point. if it does not exist, the invalidated value vector is returned.
        LEN = 2
      \ brief check & get the intersection point with other line segment
      \ param other checked line segment
      \ param allow_end_point if self value is False, end point is disallowed as an intersection.
      \ return intersection point. if it does not exist, the invalidated value vector is returned.
    """

    def intersection(self, *args):  # **kwargs):
        if len(args) == 1 and isinstance(args[0], Line2D):
            line = args[0]
            tmp_line = self.line()
            sol = tmp_line.intersection(line)
            if not sol.is_valid() or not self.contains(sol):
                return Vector2D.invalid()
            return sol

        elif len(args) == 2 and isinstance(args[1], bool):
            other = args[0]
            sol = self.line().intersection(other.line())
            if not sol.is_valid() or not self.contains(sol) or not other.contains(sol):
                return Vector2D.invalid()
            if not args[1] and not self.existIntersectionExceptEndpoint(other):
                return Vector2D.invalid()
            return sol
        else:
            return Vector2D.invalid()

    """
        Segment2D:
      \ brief check if segments cross each other or not.
      \ param other segment for cross checking
      \ return True if self segment crosses, returns False.
        Line2D:
      \ brief check if self line segment intersects with target line.
      \ param l checked line
      \ return checked result
    """

    def existIntersection(self, *args):  # **kwargs):
        if len(args) == 1 and isinstance(args[0], Segment2D):
            other = args[0]
            a0 = Triangle2D.double_signed_area(self._origin, self._terminal, other.origin())
            a1 = Triangle2D.double_signed_area(self._origin, self._terminal, other.terminal())
            b0 = Triangle2D.double_signed_area(other.origin(), other.terminal(), self._origin)
            b1 = Triangle2D.double_signed_area(other.origin(), other.terminal(), self._terminal)

            if a0 * a1 < 0.0 and b0 * b1 < 0.0:
                return True

            if self._origin == self._terminal:
                if other.origin() == other.terminal():
                    return self._origin == other.origin()

                return b0 == 0.0 and other.checkIntersectsOnLine(self._origin)

            elif other.origin() == other.terminal():
                return a0 == 0.0 and self.checkIntersectsOnLine(other.origin())

            if a0 == 0.0 and self.checkIntersectsOnLine(other.origin()) or (
                    a1 == 0.0 and self.checkIntersectsOnLine(other.terminal())) or (
                    b0 == 0.0 and other.checkIntersectsOnLine(self._origin)) or (
                    b1 == 0.0 and other.checkIntersectsOnLine(self._terminal)):
                return True

            return False

        if len(args) == 1 and isinstance(args[0], Line2D):
            line = args[0]
            a0 = line.a() * self._origin._x + line.b() * self._origin._y + line.c()
            a1 = line.a() * self._terminal._x + line.b() * self._terminal._y + line.c()
            return a0 * a1 <= 0.0

    """
        \ brief check is that point Intersects On Line
        \ param p Vector2D for that point 
        \ return True and False :D
    """

    def checkIntersectsOnLine(self, p: Vector2D):
        if self._origin._x == self._terminal._x:
            return (self._origin._y <= p._y <= self._terminal._y) or (
                    self._terminal._y <= p._y <= self._origin._y)
        else:
            return (self._origin._x <= p._x <= self._terminal._x) or (
                    self._terminal._x <= p._x <= self._origin._x)

    """
        This method is equivalent to existIntersection(), for convenience. .
      \ brief check if segments cross each other or not / check if self line segment intersects with target line 
      \ param other/l segment for cross checking / checked line
      \ return True if self segment crosses, returns False / checked result
     """

    def intersects(self, other):
        return self.existIntersection(other)

    """
      \ brief check if segments intersect each other on non terminal point.
      \ param other segment for cross checking
      \ return True if segments intersect and intersection point is not a
      terminal point of segment.
      False if segments do not intersect or intersect on terminal p oint of segment.
    """

    def existIntersectionExceptEndpoint(self, other):
        return (Triangle2D.double_signed_area(self._origin, self._terminal,
                                              other.origin()) * Triangle2D.double_signed_area(self._origin,
                                                                                              self._terminal,
                                                                                              other.terminal() < 0.0) and (
                        Triangle2D.double_signed_area(other.self.origin, other.terminal(),
                                                      self._origin) * Triangle2D.double_signed_area(other.origin(),
                                                                                                    other.terminal(),
                                                                                                    self._terminal) < 0.0))

    """
      \ brief check if segments intersect each other on non terminal point. This method is equivalent to existIntersectionExceptEndpoint(), for convenience.
      \ param other segment for cross checking
      \ return True if segments intersect and intersection point is not a
      terminal point of segment.
      False if segments do not intersect or intersect on terminal point of segment.
    """

    def intersectsExceptEndpoint(self, other):
        return self.existIntersectionExceptEndpoint(other)

    """
      \ brief get a point on segment where distance of point is minimal.
      \ param p point
      \ return nearest point on segment. if multiple nearest points found.
       returns one of them.
    """

    def nearestPoint(self, p: Vector2D):
        vec_tmp = self._terminal - self._origin

        len_square = vec_tmp.r2()

        if len_square == 0.0:
            return self._origin

        inner_product = vec_tmp.innerProduct((p - self._origin))

        if inner_product <= 0.0:
            return self._origin

        elif inner_product >= len_square:
            return self._terminal

        return self._origin + vec_tmp * inner_product / len_square

    """
        Line2D:
      \ brief get minimum distance between self segment and point
      \ param p point
      \ return minimum distance between self segment and point
        Segment2D:
      \ brief get minimum distance between 2 segments
      \ param seg segment
      \ return minimum distance between 2 segments
    """

    def dist(self, *args):  # **kwargs):
        if len(args) == 1 and isinstance(args[0], Line2D):
            vec = args[0]
            length = self.length()
            if length == 0.0:
                return self._origin.dist(vec)
            tmp_vec = self._terminal - self._origin
            prod = tmp_vec.innerProduct(vec - self._origin)
            if 0.0 <= prod <= length * length:
                return math.fabs(Triangle2D.double_signed_area(self._origin, self._terminal, vec) / length)
            return math.sqrt(min(self._origin.dist2(vec),
                                 self._terminal.dist2(vec)))

        if len(args) == 1 and isinstance(args[0], Segment2D):
            seg = args[0]
            if self.existIntersection(seg):
                return 0.0
            return min(self.dist(seg.self.origin), self.dist(seg.self.terminal), seg.dist(self._origin),
                       seg.dist(self._terminal))

    """
      \ brief get maximum distance between self segment and point
      \ param p point
      \ return maximum distance between self segment and point
    """

    def farthestDist(self, p: Vector2D):
        return math.sqrt(max(self._origin.dist2(p), self._terminal.dist2(p)))

    """
      \ brief strictly check if point is on segment or not
      \ param p checked point
      \ return True if point is on self segment
    """

    def onSegment(self, p: Vector2D):
        return Triangle2D.double_signed_area(self._origin, self._terminal, p) == 0.0 and self.checkIntersectsOnLine(p)

    """
      \ brief weakly check if point is on segment or not
      \ param p checked point
      \ return True if point is on self segment
    """

    def onSegmentWeakly(self, p: Vector2D):
        projection = self.projection(p)
        return projection.is_valid() and p.equalsWeakly(projection)

    """
      \ brief make a logical print.
      \ return print_able str
    """

    def __repr__(self):
        return "[{},{}]".format(self._origin, self._terminal)


def test():
    origin = Vector2D(0, 0)
    terminal = Vector2D(10, 10)
    seg = Segment2D(origin, terminal)
    print(seg)
    seg.assign(1.0, 2.0, 3, 4)
    print(seg)
    seg.assign(origin, 10, AngleDeg(53.1301023541559835905))
    print(seg)


if __name__ == "__main__":
    test()
