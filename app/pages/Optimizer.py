
# %%
import streamlit as st
from mip import Model, xsum, maximize, BINARY


# %%
st.text_input("Your name", key="capacity")


# %%
p = [10, 13, 18, 31, 7, 15]
w = [11, 15, 20, 35, 10, 33]

capa = int(st.session_state.capacity)
I = range(len(w))

m = Model("knapsack", solver_name="CBC")    # CBC, GRB

x = [m.add_var(var_type=BINARY) for i in I]

m.objective = maximize(xsum(p[i] * x[i] for i in I))

m += xsum(w[i] * x[i] for i in I) <= capa

m.optimize()

selected = [i for i in I if x[i].x >= 0.99]
print("selected items: {}".format(selected))
st.write("selected items: {}".format(selected))