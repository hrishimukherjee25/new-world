import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Payoff matrices for Nash and Naash equilibrium
nash_payoffs = {
    'Nationalism (N)': [[3, 3], [0, 5], [5, 0], [1, 1]],
    'Continentalism (C)': [[3, 3], [0, 5], [5, 0], [1, 1]],
    'Globalism (G)': [[3, 3], [0, 5], [5, 0], [1, 1]],
    'Universalism (U)': [[3, 3], [0, 5], [5, 0], [1, 1]],
    'Multiversalism (M)': [[3, 3], [0, 5], [5, 0], [1, 1]]
}

naash_payoffs = {
    'Nationalism (N)': [[0, 0], [-3, 2], [2, -3], [-2, -2]],
    'Continentalism (C)': [[-1, -1], [-4, 1], [1, -4], [-3, -3]],
    'Globalism (G)': [[-2, -2], [-5, 0], [0, -5], [-4, -4]],
    'Universalism (U)': [[-3, -3], [-6, -1], [-1, -6], [-5, -5]],
    'Multiversalism (M)': [[-4, -4], [-7, -2], [-2, -7], [-6, -6]]
}

# Plotting Nash and Naash equilibrium payoffs
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
fig.suptitle('Comparison of Nash and Naash Equilibrium Payoffs for Different Levels')

for i, (level, matrix) in enumerate(nash_payoffs.items()):
    ax = axes[0, i]
    nash_matrix = np.array(matrix).reshape(2, 2, 2)
    nash_data = np.sum(nash_matrix, axis=2)
    sns.heatmap(nash_data, annot=np.sum(nash_matrix, axis=2), fmt="d", cmap='coolwarm', ax=ax, cbar=False)
    ax.set_title(f'Nash: {level}')
    ax.set_xticks([0.5, 1.5])
    ax.set_yticks([0.5, 1.5])
    ax.set_xticklabels(['C', 'D'])
    ax.set_yticklabels(['C', 'D'])
    ax.set_xlabel('Player B')
    ax.set_ylabel('Player A')

for i, (level, matrix) in enumerate(naash_payoffs.items()):
    ax = axes[1, i]
    naash_matrix = np.array(matrix).reshape(2, 2, 2)
    naash_data = np.sum(naash_matrix, axis=2)
    sns.heatmap(naash_data, annot=np.sum(naash_matrix, axis=2), fmt="d", cmap='coolwarm', ax=ax, cbar=False)
    ax.set_title(f'Naash: {level}')
    ax.set_xticks([0.5, 1.5])
    ax.set_yticks([0.5, 1.5])
    ax.set_xticklabels(['C', 'D'])
    ax.set_yticklabels(['C', 'D'])
    ax.set_xlabel('Player B')
    ax.set_ylabel('Player A')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
