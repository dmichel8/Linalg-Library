#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 23:20:19 2025

@author: John Doe
"""

# Linalg Lib

PI = 3.1415926535897932384626433

class Linvec:
    def __init__(self, *args):
        self.vec = args[0]
        
    def __add__(self, otherVec):
        if len(self.vec) != len(otherVec.vec):
            raise Exception("Vectors not of same length")
        f = []
        for i in range(len(self.vec)):
            f.append(self.vec[i] + otherVec.vec[i])
        return Linvec(f)
    
    def __radd__(self, otherVec):
        if len(self.vec) != len(otherVec.vec):
            raise Exception("Vectors not of same length")
        f = []
        for i in range(len(self.vec)):
            f.append(self.vec[i] + otherVec.vec[i])
        return Linvec(f)
    
    def __len__(self):
        return len(self.vec)
    
    def __str__(self):
        return str(self.vec)
    
    def __sub__(self, otherVec):
        if type(self) == type(otherVec):
            if len(self) != len(otherVec):
                raise Exception("Vectors not of same length")
            f = []
            for i in range(len(self)):
                f.append(self.vec[i] - otherVec.vec[i])
            return Linvec(f)
        elif type(otherVec) == int:
            None
        else:
            raise Exception("Unknown type error")
            
    def __rsub__(self, otherVec):
        if type(self) == type(otherVec):
            if len(self) != len(otherVec):
                raise Exception("Vectors not of same length")
            f = []
            for i in range(len(self)):
                f.append(self.vec[i] - otherVec.vec[i])
            return Linvec(f)
        elif type(otherVec) == int:
            None
        else:
            raise Exception("Unknown type error")
            
    def __mul__(self, other):
        if type(self) == type(other):
            None
        elif type(other) == int or type(self) == int:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]*other)
            return Linvec(f)
        elif type(other) == float or type(self) == float:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]*other)
            return Linvec(f)
        else:
            raise Exception("Unknown Type Error")
    
    def __rmul__(self, other):
        if type(self) == type(other):
            None
        elif type(other) == int or type(self) == int:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]*other)
            return Linvec(f)
        elif type(other) == float or type(self) == float:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]*other)
            return Linvec(f)
        else:
            raise Exception("Unknown Type Error")
            
    def __truediv__(self, other):
        if type(self) == type(other):
            None
        elif type(other) == int or type(self) == int:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]/other)
            return Linvec(f)
        elif type(other) == float or type(self) == float:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]/other)
            return Linvec(f)
        else:
            raise Exception("Unknown Type Error")
            
    def __rtruediv__(self, other):
        if type(self) == type(other):
            None
        elif type(other) == int or type(self) == int:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]/other)
            return Linvec(f)
        elif type(other) == float or type(self) == float:
            f = []
            for i in range(len(self)):
                f.append(self.vec[i]/other)
            return Linvec(f)
        else:
            raise Exception("Unknown Type Error")
    
    def test(self, otherVec):
        if type(otherVec) == type(self):
            return "hey girl"
    
    def dot(self, otherVec):
        if len(self.vec) != len(otherVec.vec):
            raise Exception("Vectors not of same length")
        prod = 0
        for i in range(len(self.vec)):
            prod += self.vec[i] * otherVec.vec[i]
        return prod
    
    def norm(self):
        f = 0
        for i in range(len(self.vec)):
            f += (self.vec[i])**2
        return f**0.5
    
    def explain_norm(self, **kwargs):
        longv = False
        if len(self) > 6:
            longv = True
        
        nopretext = kwargs.get("nopretext", False)
        
        if nopretext != True:
            text = ""
            text += "\nThe vector norm (or sometimes the length) of a vector is function" + \
                " that acts very much like the distance from the origin, especially in" + \
                    " 2-D and 3-D space.\n In the case of this program, we take the Euclidean" + \
                        "norm specifically, which is ||vector(u)|| = sqrt(u1**2 + u2**2 + ...)" + \
                            " where u1, u2, ... represent the values of the vector. A good way" + \
                                " to remember this is SRSS (Square Root of the Sum of Squares)."
            text += "\n\nThere are other norms which you can explore in this program (soon) such" + \
                " as the taxicab norm, absolute-value norm, p-norms, maximum norms, etc.\n\n"
        
        if longv:
            text += "In the case of your vector, u = [" + str(self.vec[0]) + ", " + str(self.vec[1]) + \
                ", " + str(self.vec[2]) + ", ...]"
        else:
            text += "In the case of your vector, u = " + str(self)
            
        text += ", we will start the process of first adding up all components squared.\n\n"
        
        sumval = 0
        for i in range(len(self)):
            sumval += self.vec[i]**2
            text += "u1**2 = " + str(self.vec[i]) + "**2 = " + str(self.vec[i]**2) + ". The sum is currently "+ str(sumval) +". \n"
        
        text += "\nNow that that is done, we just need to square root this sum." 
        
        text += "\n\n" + str(sumval) + " square rooted is " + str(sumval**0.5) + ".\n"
        
        text += "\nSo, ||u|| = " + str(sumval**0.5) + ".\n"
        
        return text
    
    def normalize(self):
        f = 0
        for i in range(len(self.vec)):
            f += (self.vec[i])**2
         
        return self/(f**0.5)
    
    def verify_Cauchy_Schwarz(self, other):
        if type(self) != type(other):
            raise Exception("Both must be Linvec objects!")
        dotval = abs(self.dot(other))
        norm1 = self.norm()
        norm2 = other.norm()
        if dotval <= norm1*norm2:
            return "\n|u • v| ≤ ||u|| ||v|| \nu = " + str(self) + "\nv = " \
                + str(other) + "\n|u • v| = " + str(dotval) + \
                    "\n||u|| ||v|| = " + str(norm1*norm2) + "\n" + str(dotval) + \
                        " ≤ " + str(norm1*norm2) + "\nThus, Cauchy-Schwarz Inequality is upheld.\n"
        else:
            raise Exception("how.")
            
    def verify_Triangle_Inequality(self, other):
        if type(self) != type(other):
            raise Exception("Both must be Linvec objects!")
        comb_norm = (self + other).norm()
        norm1 = self.norm()
        norm2 = other.norm()
        if comb_norm <= norm1 + norm2:
            return "\n||u + v|| ≤ ||u|| + ||v|| \nu = " + str(self) + "\nv = " \
                + str(other) + "\n||u + v|| = " + str(comb_norm) + \
                    "\n||u|| + ||v|| = " + str(norm1 + norm2) + "\n" + str(comb_norm) + \
                        " ≤ " + str(norm1+norm2) + "\nThus, Triangle Inequality is upheld.\n"
        else:
            raise Exception("how.")
            
    def distance(self, other):
        if len(self.vec) != len(other.vec):
            raise Exception("Vectors not of same length")
        return (self - other).norm()
    
    def angle_between(self, other):
        """
        Quickly determines the angle between 2 vectors. May not be super precise.
        Will fix. This is because I use an approx for the inverse cos function.

        Returns
        -------
        float

        """
        numerator = self.dot(other)
        denominator = self.norm() * other.norm()
        f = numerator/denominator
        return PI/2 - (f + ((f*f*f)/6) + ((3*(f**5))/(40)))
    
    def isOrthogonal(self, other):
        if self.dot(other) == 0:
            return True
        else:
            return False
        
    def pythagorasProof(self, other):
        pass
    
    def proj(self, other):
        return ((self.dot(other))/(self.dot(self)))*self

    def pointDist(self, other):
        pass
        
    
        

class dMat:
    def __init__(self, *args):
        self.matrix = args[0]
        self.rowCount = len(args[0])
        for i in range(len(args[0])):
            if len(args[0][i]) != len(args[0][0]):
                raise Exception("Invalid Matrix (flesh out the matrix)")
        self.colCount = len(args[0][0])
    
        
    






