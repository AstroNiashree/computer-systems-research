import pandas as pd
import matplotlib.pyplot as plt

std = {'2':0 , '3': 0, '4': 0, '5': 0}
mean = {'2':0 , '3': 0, '4': 0, '5': 0}
for i in range(2, 6):
    df = pd.read_csv(f'variability2agents{i}.csv')
    std[str(i)] = df.iloc[:, 10:11].std()[0]
    mean[str(i)] = df.iloc[:, 10:11].mean()[0]

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Variability Plots')
fig.tight_layout(pad=2.0)

ax1.bar(list(std.keys()), list(std.values()))
ax1.set_title('')
ax1.set_xlabel('Variability')
ax1.set_ylabel('Standard Deviation')

ax2.bar(list(mean.keys()), list(mean.values()))
ax2.set_title('')
ax2.set_xlabel('Variability')
ax2.set_ylabel('Mean')

plt.show()