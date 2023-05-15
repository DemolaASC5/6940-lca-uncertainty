import numpy as np
import matplotlib.pyplot as plt

# Define sub-footprints
sub_footprints = [0.0000201, 836, 325, 2.49E+02, 49.3, -0.0113, 0.405, -0.000116, -1600, -1.8, 0.486]

# Define number of iterations
iterations = 1000

# Perform Monte Carlo simulation for each scenario
best_case = np.zeros(len(sub_footprints))
worst_case = np.zeros(len(sub_footprints))
stochastic_case = np.zeros(len(sub_footprints))
average_case = np.zeros(len(sub_footprints))
for i in range(iterations):
    # Generate random values for each sub-footprint
    sub_values = [np.random.uniform(sub * 0.95, sub * 1.05) for sub in sub_footprints]

    # Update best case, worst case, and average scenarios
    if i == 0:
        best_case = np.array(sub_values)
        worst_case = np.array(sub_values)
    else:
        for j in range(len(sub_values)):
            if sub_values[j] < best_case[j]:
                best_case[j] = sub_values[j]
            if sub_values[j] > worst_case[j]:
                worst_case[j] = sub_values[j]
    average_case += np.array(sub_values)
    
    # Generate random values from normal distribution for the stochastic scenario
    stochastic_values = [np.random.normal(sub, abs(sub) * 0.05) for sub in sub_values]
    stochastic_case += np.array(stochastic_values)

stochastic_case /= iterations
average_case /= iterations

# Define labels
labels = ['Stainless Steel', 'MnMo Electrode', 'Hydrochloric acid', 'Sodium hydroxide', 'Sodium Chloride',
          'Deionised Water', 'Electricity', 'Recycled Steel', 'Sodium Hydroxide Produced', 'Hydrogen Gas',
          'Chlorine Gas']

# Calculate the sum of values for each bar
best_case_sum = np.sum(best_case)
worst_case_sum = np.sum(worst_case)
average_case_sum = np.sum(average_case)
stochastic_case_sum = np.sum(stochastic_case)

# Create the stacked bar chart
x = np.arange(4)
width = 0.8
bottom = np.zeros(4)

fig, ax = plt.subplots()
fig.suptitle('Monte Carlo Uncertainty Analysis')

for i, label in enumerate(labels):
    print(stochastic_case[i])
    ax.bar(x, [best_case[i], worst_case[i], average_case[i], stochastic_case[i]], width, bottom=bottom, label=label)
    bottom += [best_case[i], worst_case[i], average_case[i], stochastic_case[i]]

# Add labels to each bar
ax.text(x[0], best_case_sum + 0.5, round(best_case_sum), ha='center', weight='bold', color='black')
ax.text(x[1], worst_case_sum + 0.5, round(worst_case_sum), ha='center', weight='bold', color='black')
ax.text(x[2], average_case_sum + 0.5, round(average_case_sum), ha='center', weight='bold', color='black')
ax.text(x[3], stochastic_case_sum + 0.5, round(stochastic_case_sum), ha='center', weight='bold', color='black')

ax.set_ylabel('Carbon Footprint')
ax.set_xlabel('Scenarios')
ax.set_title('Monte Carlo Uncertainty Analysis')
ax.set_xticks(x)
ax.set_xticklabels(['Best Case', 'Worst Case', 'Average Case', 'Stochastic Case'])

ax.legend()
plt.tight_layout()
plt.show()