import cvxpy as cp

# Decision variables
y = cp.Variable()  # Number of tables produced
t = cp.Variable()  # Auxiliary variable for sqrt(y^2 + 9)

# Constraints
constraints = [
    y >= 3,                   # Lower bound for y
    y <= 10,                  # Upper bound for y
    cp.SOC(t, cp.hstack([y, 3])),  # Second-order cone constraint: t >= sqrt(y^2 + 9)
]

# Objective function
objective = cp.Minimize(400000 * (10 - y) + 500000 * t)

# Define and solve the problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Output results (handle scalars or arrays)
y_value = y.value if y.value.shape == () else y.value  # Handle scalar or array
t_value = t.value if t.value.shape == () else t.value  # Handle scalar or array
print(f"Status: {problem.status}")
print(f"y = {y_value}, t = {t_value}, Z = {problem.value}")
