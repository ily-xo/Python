import numpy as np
import matplotlib.pyplot as plt
from math import log, sin, cos

def m_dist(a, b):
    return np.linalg.norm(a - b)

def m_stress(p):
    stress = 0
    for row in range(0, 21):
        for col in range(0, 21):
            if col > row:
                stress += (distances[row, col] - m_dist(p[row], p[col])) ** 2
    return stress

def computing_full_gradient(p):
    i, d = p.shape
    gradient_matrix = np.zeros([i, d])
    for a in range(0, i):
        for b in range(0, d):
            gradient_matrix[a, b] = (m_stress(add_delta(p, a, b, 0.001)) - m_stress(add_delta(p, a, b, -0.001))) / (2 * 0.001)
    return gradient_matrix

def steps_run(p, iterations):
    for steps in range(iterations):
        learning_rate = 0.001
        p = p - learning_rate * computing_full_gradient(p)
        individual_stress = m_stress(p) / (21 * 10)
    return individual_stress, p

# All possible pairs of sports excluding duplicates from the CSV
def pairing_gen(names):
    paired_names = []
    for row in range(0, 21):
        for col in range(0, 21):
            if col > row:
                paired_names.append([names[row], names[col]])
    return paired_names

# Pairwise distances for psychological dist & mds dist
def pair_w_distances(distances, p):
    psychological_distances = []
    mds_distances = []
    for row in range(0, 21):
        for col in range(0, 21):
            if col > row:
                psychological_distances.append(distances[row, col])
                mds_distances.append(m_dist(p[row], p[col]))
    return psychological_distances, mds_distances

# positions 
def generating_positions(N, D):
    positions = np.zeros((N, D))
    for i in range(N):
        for d in range(D):
            positions[i, d] = sin(i + d) + cos(i - d)
    return positions

# Main
names = ["football", "baseball", "basketball", "tennis", "softball", "canoeing", "handball", "rugby", "hockey", "ice hockey", "swimming", "track", "boxing", "volleyball", "lacrosse", "skiing", "golf", "polo", "surfing", "wrestling", "gymnastics"]

similarities = np.loadtxt(open("simil.csv", "rb"), delimiter=",", skiprows=1)
distances = 1 - similarities

D = 2
N = distances.shape[0]
assert(distances.shape[1] == N and N == len(names))

pos = generating_positions(N, D)

individual_stress, final_position_matrix = steps_of_runner(pos.copy(), 8)

x, y = [each[0] for each in final_position_matrix], [each[1] for each in final_position_matrix]
fig, ax = plt.subplots()
ax.scatter(x, y, color='purple')

for i, txt in enumerate(names):
    ax.annotate(txt, (x[i], y[i]))

plt.xlabel('x-axis coordinate for psychological map position of sports')
plt.ylabel('y-axis coordinate for psychological map position of sports')
plt.title('Mental location of each sport in the psychological map')

plt.savefig('sports_h.png')
plt.show()
