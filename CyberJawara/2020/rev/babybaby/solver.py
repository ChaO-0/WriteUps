from z3 import *

def solvePram():
    x = Int('x')
    y = Int('y')
    z = Int('z')

    s = Solver()

    s.add(x > 0)
    s.add(y > 0)
    s.add(z > 0)
    s.add(x + y == x * z)
    s.add(y / z == 20)
    s.add(y / x == 3)

    s.check()
    print s.model()


if __name__ == "__main__":
    solvePram()