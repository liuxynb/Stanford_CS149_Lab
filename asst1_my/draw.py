import matplotlib.pyplot as plt

# Data
configurations = ["Serial", "2 Threads", "3 Threads", "4 Threads", "5 Threads", "6 Threads", "7 Threads", "8 Threads"]
times = [568.760, 287.111, 287.111, 236.096, 229.175, 175.183, 156.044, 139.662]
speedups = [1.0] + [times[0] / time for time in times[1:]]

# Plotting
plt.plot(configurations, speedups, marker='o', linestyle='-', color='b')
plt.title('Speedup vs. Configurations')
plt.xlabel('Configurations')
plt.ylabel('Speedup')
plt.grid(True)
plt.show()
