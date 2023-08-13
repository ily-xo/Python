import matplotlib.pyplot as plt

def m_Vx(alpha, beta, lambdah, initial):
    change_Vx = alpha * beta * (lambdah - initial)
    return initial + change_Vx

def trial_run(alpha, beta, lambdah, initial, num_trials):
    index = 1
    association_list = [initial]
    while index < num_trials:
        next_value = m_Vx(alpha, beta, lambdah, initial)
        initial = next_value
        association_list.append(initial)
        index += 1
    return association_list

x_values = list(range(0, 21))
y_values = list(trial_run(0.75, 0.1, 1.0, 0.05, 21))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(1, 21)
ax.set_ylim(0, 1)
plt.plot(x_values, y_values, color='red', linestyle='--', linewidth=3)
plt.xlabel('Amount of Trials')
plt.ylabel('Strength')
plt.title('Relationship between Association Strength and Amount of Trials')
ax.xaxis.set(ticks=range(0, 22, 2))
ax.yaxis.set(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('m_plot.png')
plt.show()
