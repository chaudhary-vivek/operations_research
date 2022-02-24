# Impoting pulp library
from pulp import *


#%%

# Transportation problem ######################################################
# Supply chain analytics - T.A.S. Vijayraghavan pg.156 ########################


# Source list
src = ['A', 'B', 'C']

# Destination list
dest = ['D', 'E', 'F', 'G']

# Supply from each source
supply = {'A' : 35, 'B' : 50, 'C' : 40}

# Demand at each destination
demand = {'D' : 45, 'E' : 20, 'F' : 30, 'G' : 30 }

# Transport cost from each source to destination
cost = {'A': {'D' : 8, 'E' : 6, 'F' : 10, 'G' : 9},
       'B': {'D' : 9, 'E' : 12, 'F' : 13, 'G' : 7},
       'C': {'D' : 14, 'E' : 9, 'F' : 16, 'G' : 5},
       }

# Creating instance of LpProblem
prob = LpProblem("Transportation", LpMinimize)

# Creating routes
routes = [(i,j) for i in src for j in dest]

# Defining decision variables
shipping_quantity = LpVariable.dicts("shipping_quantity" , (src, dest), 0)

# Defining objective function
prob += lpSum(shipping_quantity[i][j]*cost[i][j] for (i,j) in routes)

# Adding demand constraint
for j in dest:
    prob += lpSum(shipping_quantity[i][j] for i in src) == demand [j]
    
# Adding supply constraint
for i in src:
    prob += lpSum(shipping_quantity[i][j] for j in dest) <= supply[i]
    
# We can print the problem summary like this
print(prob)

# Solving the problem
prob.solve()

# Print the status
print("Status:", LpStatus[prob.status])

# Printing the shipping quantities
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)
        
# Printing the objective
print("Total transportation cost = ", value(prob.objective))















