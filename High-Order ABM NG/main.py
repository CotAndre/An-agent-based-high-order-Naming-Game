from naming_model import NamingModel
from naming_model import only_one_opinion
from naming_server import width, height
import matplotlib.pyplot as plt
import time

# Values used in the benchmark article
a_val = [327, 0.003, 0.336, width, height, 5]  # n. agents, committed fraction, beta, width, height, group size

my_model = NamingModel(a_val[0], a_val[1], a_val[2], a_val[3], a_val[4], a_val[5])
min_steps = 100
max_steps = 1000000


start_time = time.time()

for i in range(max_steps):
    my_model.step()
    if i % 50000 == 0 and i != 0:
        print(i, "steps done")
    if i >= min_steps and only_one_opinion(my_model):
        break

print("--- %s seconds ---" % (time.time() - start_time))

df = my_model.datacollector.get_model_vars_dataframe()
df.plot()
plt.show()
