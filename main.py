import numpy as np
import math
import sympy


class CalcDistance():
    def __init__(self, A, B, C, point):
        self.A = set(A)
        self.B = set(B)
        self.C = set(C)
        self.point = point

        self.alpha = Plan(A, B, C)

    def distancePointToPlan(self, point, plan):
        r = plan.retningsVektor
        absOfPlan = abs(r[0]*point[0]+r[1]*point[1]+r[2]*point[2])
        lengthOfRetning = math.sqrt(r[0]**2+r[1]**2+r[2**2])
        return absOfPlan/lengthOfRetning

    def movePoint(self, point, direction, distance):
        t = (distance**2)/(direction[0]**2 + direction[1]**2 + direction[2]**2)
        movingVector = [direction[0]*t, direction[1]*t, direction[2]*t]

        movedPoint = (
            point + movingVector[0], point + movingVector[1], point + movingVector[2])
        return movedPoint
    
    def isBetweenPoints(self, A, B):
        pass

    def checkCrossingLine(self, lineA, lineB):
        # [A.A[0]+A.r[0]*t, A.A[1]+A.r[1]*t, A.A[2]+A.r[2]*t] = [B.A[0]+B.r[0]*s, B.A[1]+B.r[1]*s, B.A[2]+B.r[2]*s]
        # A.A[0]+A.r[0]*t = B.A[0]+B.r[0]*s v A.A[1]+A.r[1]*t = B.A[1]+B.r[1]*s v A.A[2]+A.r[2]*t = B.A[2]+B.r[2]*s
        # t = (B.A[0]+B.r[0]*s-A.A[0])/A.r[0]
        # yu
        A = lineA
        B = lineB
        s, t = sympy.symbols("s t")
        eq1 = sympy.Eq(A.A[0] + A.r[0]*t - B.A[0] - B.r[0]*s, 0)
        eq2 = sympy.Eq(A.A[1] + A.r[1]*t - B.A[1] - B.r[1]*s, 0)

        sol = sympy.solve((eq1, eq2), (s, t))
        t = sol[t]

        return (A.A[0] + A.r[0]*t, A.A[1] + A.r[1]*t, A.A[2] + A.r[2]*t)



class Plan():
    def __init__(self, A, B, C):
        self.A = set(A)
        self.B = set(B)
        self.C = set(C)

        self.AB = vektorMellomPunkt(self.A, self.B)
        self.AC = vektorMellomPunkt(self.A, self.C)
        self.BC = vektorMellomPunkt(self.B, self.C)

        self.retningsVektor = np.cross(self.AB, self.AC)


class Line():
    def __init__(self, A, B):
        self.A = A
        self.B = B

        self.r = vektorMellomPunkt(A, B)

    def pointOnLine(self, point):
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
