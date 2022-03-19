from numpy import exp
import pygal
import pandas as pd
import matplotlib.pyplot as plt

# Visualize the runtime distribution

bar_chart = pygal.Bar()
bar_chart.title = 'Runtime Distribution'

explorations = pd.read_csv("./output_data/explorations2agents.csv")
print(explorations['time'])
plt.hist(explorations['time'], range=(0, 20), bins=50)
plt.show()
