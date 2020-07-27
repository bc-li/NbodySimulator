# -----------------------------------------------------------------------
# vector.py
# -----------------------------------------------------------------------

import math
import stdio
import stdarray


# -----------------------------------------------------------------------

class Vector:

    # Construct a new Vector object with numeric Cartesian coordinates
    # 用数值笛卡尔坐标构造一个新的向量对象
    # given in array a.
    def __init__(self, a):
        # Make a defensive copy to ensure immutability.
        self._coords = a[:]  # Cartesian coordinates
        self._n = len(a)  # Dimension.

    # Return the ith Cartesian coordinate of self.
    # 返回self的第i个笛卡尔坐标
    def __getitem__(self, i):
        return self._coords[i]

    # Return the sum of self and Vector object other.
    # 返回self和向量object other的和。
    def __add__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] + other._coords[i]
        return Vector(result)

    # Return the difference of self and Vector object other.
    # 返回自身与向量对象的差值。
    def __sub__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] - other._coords[i]
        return Vector(result)

    # Return the product of self and numeric object alpha.
    # 返回self和数值对象alpha的乘积。
    def scale(self, alpha):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = alpha * self._coords[i]
        return Vector(result)

    # Return the inner product of self and Vector object other.
    # 返回 self 与向量 other 的点积。
    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    # Return the magnitude, that is, the Euclidean norm, of self.
    # 返回向量 self 的模
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Return the unit vector of self.
    # 返回 self 的单位向量。
    def direction(self):
        return self.scale(1.0 / abs(self))

    # Return a string representation of self.
    # 返回一个self的字符串表示。
    def __str__(self):
        return str(self._coords)

    # Return the dimension of self.
    # 返回这个向量是几维的
    def __len__(self):
        return self._n


# -----------------------------------------------------------------------

# For testing.
# Create and use some Vector objects.

def main():
    xCoords = [1.0, 2.0, 3.0, 4.0]
    yCoords = [5.0, 2.0, 4.0, 1.0]

    x = Vector(xCoords)
    y = Vector(yCoords)

    stdio.writeln('x        = ' + str(x))
    stdio.writeln('y        = ' + str(y))
    stdio.writeln('x + y    = ' + str(x + y))
    stdio.writeln('10x      = ' + str(x.scale(10.0)))
    stdio.writeln('|x|      = ' + str(abs(x)))
    stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    stdio.writeln('|x - y|  = ' + str(abs(x - y)))


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------

# python vector.py
# x        = [1.0, 2.0, 3.0, 4.0]
# y        = [5.0, 2.0, 4.0, 1.0]
# x + y    = [6.0, 4.0, 7.0, 5.0]
# 10x      = [10.0, 20.0, 30.0, 40.0]
# |x|      = 5.477225575051661
# <x, y>   = 25.0
# |x - y|  = 5.0990195135927845
