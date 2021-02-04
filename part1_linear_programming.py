from pulp import *

model = LpProblem("profits", LpMaximize)

A = LpVariable('A', lowBound=0)
B = LpVariable('B', lowBound=0)
C = LpVariable('C', lowBound=0)

model += 500*A + 450*B + 600*C
model += 6*A + 5*B + 8*C <= 60
model += 10.5*A + 20*B + 10*C <= 150
model += A <= 10

model.solve()
print("objective is " + str(value(model.objective)))
print("A is " + str(value(A.varValue)))
print("B is " + str(value(B.varValue)))
print("C is " + str(value(C.varValue)))

