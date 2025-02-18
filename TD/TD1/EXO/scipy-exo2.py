import numpy as np
from scipy.optimize import minimize

def cost(y):
    return 400000 * (10 - y) + 500000 * np.sqrt(y**2 + 3**2)

bounds = [(3, 10)]
result = minimize(cost, x0=3, bounds=bounds)

print("y optimal: ", result.x[0])
print("Cost optimal: ", result.fun)
