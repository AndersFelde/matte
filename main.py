import numpy as np
import math
import sympy


class CalcDistance():
    def __init__(self, A, B, C, point):
        self.A = list(A)
        self.B = list(B)
        self.C = list(C)
        self.point = point

        self.alpha = Plan(A, B, C)

    def distancePointToPlan(self, point, plan):
        r = plan.retningsVektor
        absOfPlan = abs(r[0]*point[0]+r[1]*point[1]+r[2]*point[2])
        lengthOfRetning = math.sqrt(r[0]**2+r[1]**2+r[2]**2)
        return absOfPlan/lengthOfRetning

    def movePoint(self, point, direction, distance):
        t = (distance**2)/(direction[0]**2 + direction[1]**2 + direction[2]**2)
        movingVector = [direction[0]*t, direction[1]*t, direction[2]*t]

        movedPoint = (
            point[0] + movingVector[0], point[1] + movingVector[1], point[2] + movingVector[2])
        return movedPoint

    def checkCrossingLine(self, lineA, lineB):
        # [A.A[0]+A.r[0]*t, A.A[1]+A.r[1]*t, A.A[2]+A.r[2]*t] = [B.A[0]+B.r[0]*s, B.A[1]+B.r[1]*s, B.A[2]+B.r[2]*s]
        # A.A[0]+A.r[0]*t = B.A[0]+B.r[0]*s v A.A[1]+A.r[1]*t = B.A[1]+B.r[1]*s v A.A[2]+A.r[2]*t = B.A[2]+B.r[2]*s
        # t = (B.A[0]+B.r[0]*s-A.A[0])/A.r[0]
        # yu
        A = lineA
        B = lineB
        print(A.A[0] + A.r[0] - B.A[0] - B.r[0])
        print(type(A.A[0]))
        s, t = sympy.symbols("s t")

        eq1 = sympy.Eq(A.A[0] + A.r[0]*t - B.A[0] - B.r[0]*s, 0)
        eq2 = sympy.Eq(A.A[1] + A.r[1]*t - B.A[1] - B.r[1]*s, 0)

        sol = sympy.solve((eq1, eq2), (s, t))
        print(sol)
        for key in sol:
            t = sol[key]

        return (A.A[0] + A.r[0]*t, A.A[1] + A.r[1]*t, A.A[2] + A.r[2]*t)

    def isInsideTriangle(self, A, B, C):
        lineAB = Line(A, B)
        lineBC = Line(B, C)
        lineAC = Line(A, C)

        sides = [lineAB, lineBC, lineAC]

        lineAP = Line(A, self.point)

        crossings = 0

        for line in sides:
            crossPoint = self.checkCrossingLine(lineAP, line)
            if isBetweenPoints(line.A, line.B, crossPoint):
                crossings += 1

        if crossings == 2:
            return True

        return False

    def calcDistance(self, A, B, C):
        self.distances = []

        lineAB = Line(A, B)
        lineBC = Line(B, C)
        lineAC = Line(A, C)

        sides = [lineAB, lineBC, lineAC]

        for line in sides:
            crossingPoint = line.closestPointOnLine(self.point)
            if isBetweenPoints(A, B, crossingPoint):
                self.distances.append(
                    distanceBetweenPoints(self.point, crossingPoint))
            else:
                distanceA = distanceBetweenPoints(line.A, self.point)
                distanceB = distanceBetweenPoints(line.B, self.point)

                if distanceB < distanceA:
                    self.distances.append(distanceB)
                else:
                    self.distances.append(distanceA)

        self.distances.sort()

        xDistance = self.distances[0]
        yDistance = self.distancePointToPlan(self.point, self.alpha)

        distance = math.sqrt(xDistance**2 + yDistance**2)

        return distance


class Plan():
    def __init__(self, A, B, C):
        self.A = list(A)
        self.B = list(B)
        self.C = list(C)

        self.AB = vektorMellomPunkt(self.A, self.B)
        self.AC = vektorMellomPunkt(self.A, self.C)
        self.BC = vektorMellomPunkt(self.B, self.C)

        self.numpyRetningsVektor = np.cross(self.AB, self.AC)
        self.retningsVektor = []
        for x in self.numpyRetningsVektor:
            self.retningsVektor.append(int(x))


class Line():
    def __init__(self, A, B):
        self.A = A
        self.B = B

        self.r = vektorMellomPunkt(A, B)

    def closestPointOnLine(self, point):
        A = point
        r = self.r

        t = sympy.symbols("t")
        eq = sympy.Eq(((A[0]+r[0]*t)*r[0]) +
                      ((A[1]+r[1]*t)*r[1])+((A[2]+r[2]*t)*r[2]), 0)
        sol = sympy.solve((eq), (t))

        t = sol[0]
        # AP * retningsvektor = 0
        # ((A[0]+r[0]*t)*r[0])+((A[1]+r[1]*t)*r[1])+((A[2]+r[2]*t)*r[2]) = 0
        # A[0]*r[0]+(r[0]**2)*t+A[1]*r[1]+(r[1]**2)*t+A[2]*r[2]+(r[2]**2)*t = 0
        # t = -A[0]*r[0]+(r[0]**2)-A[1]*r[1]+(r[1]**2)-A[2]*r[2]+(r[2]**2)

        AP = [A[0]+r[0]*t, A[1]+r[1]*t, A[2]+r[2]*t]

        return (A[0]+AP[0], A[1]+AP[1], A[2]+AP[2])


def vektorMellomPunkt(a, b):
    return [b[0]-a[0], b[1]-a[1], b[2]-a[2]]


def isBetweenPoints(a, b, point):
    lengthAP = distanceBetweenPoints(a, point)
    lengthBP = distanceBetweenPoints(b, point)

    lengthAB = distanceBetweenPoints(a, b)

    if lengthAP <= lengthAB and lengthBP <= lengthAB:
        return True

    return False


def distanceBetweenPoints(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)


def main():
    punkt = (5, 6, 7)
    A = (1, 2, 3)
    B = (3, 2, 1)
    C = (4, 3, 2)
    calc = CalcDistance(A, B, C, punkt)

    alpha = Plan(A, B, C)

    distansePunktTilAlpha = calc.distancePointToPlan(punkt, alpha)

    nyA = calc.movePoint(A, alpha.retningsVektor, distansePunktTilAlpha)
    nyB = calc.movePoint(B, alpha.retningsVektor, distansePunktTilAlpha)
    nyC = calc.movePoint(C, alpha.retningsVektor, distansePunktTilAlpha)

    if calc.isInsideTriangle(nyA, nyB, nyC):
        print(calc.distancePointToPlan(punkt, alpha))
        return

    distance = calc.calcDistance(nyA, nyB, nyC)
    print(distance)
    return


if __name__ == "__main__":
    main()
