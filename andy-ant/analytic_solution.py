import numpy as np

# Variable order: [t0, x1, x2, x3, x4, t2, t3, t5]
#
# Each equation must be in the form:
#   a*t0 + b*x1 + c*x2 + d*x3 + e*x4 + f*t2 + g*t3 + h*t5 = k
#
# Each row of A holds the 8 coefficients [a, b, c, d, e, f, g, h].
# The corresponding entry in b holds the constant k.

A = np.array([
    # t0   x1   x2   x3   x4   t2   t3   t5
    [  1,  -1,   0,   0,   0,   0,   0,   0],  # equation t0
    [  0,   4,  -1,   0,   0,  -2,   0,   0],  # equation x1
    [  0,  -1,   6,  -2,   0,  -2,  -1,   0],  # equation x2
    [  0,   0,  -2,   6,  -1,  -1,  -2,   0],  # equation x3
    [  0,   0,   0,  -1,   4,   0,  -2,  -1],  # equation x4
    [  0,  -2,  -2,  -1,   0,   5,   0,   0],  # equation t2
    [  0,   0,  -1,  -2,  -2,   0,   5,   0],  # equation t3
    [  0,   0,   0,   0,  -1,   0,   0,   1],  # equation t5
], dtype=float)

b = np.array([1, 6, 6, 6, 6, 5, 5, 1], dtype=float)

solution = np.linalg.solve(A, b)
t0, x1, x2, x3, x4, t2, t3, t5 = solution
print(f"{t0=} {x1=} {x2=} {x3=} {x4=} {t2=} {t3=} {t5=}")
