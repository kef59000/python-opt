
# %%
import gurobipy as gp
from gurobipy import GRB


# %%
try:
    m = gp.Model("mip1")

    # Create variables
    x = m.addVar(vtype=GRB.BINARY, name="x")
    y = m.addVar(vtype=GRB.BINARY, name="y")
    z = m.addVar(vtype=GRB.BINARY, name="z")

    m.setObjective(x + y + 2 * z, GRB.MAXIMIZE)

    m.addConstr(x + 2 * y + 3 * z <= 4, "c0")

    m.addConstr(x + y >= 1, "c1")

    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.VarName, v.X))

    print('Obj: %g' % m.ObjVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')


# %%
p = [10, 13, 18, 31, 7, 15]
w = [11, 15, 20, 35, 10, 33]
c, I = 47, range(len(w))

m = gp.Model("knapsack")

x = m.addVars(I, vtype=GRB.BINARY, name="x")

goal = gp.quicksum(p[i] * x[i] for i in I)
m.setObjective(goal, GRB.MAXIMIZE)

Ct_Cap = m.addConstr(gp.quicksum(w[i] * x[i] for i in I) <= c)

m.optimize()

selected = [i for i in I if x[i].x >= 0.99]
print("selected items: {}".format(selected))


# %%
