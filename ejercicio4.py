import numpy as np
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# tablero
BOARD_SIZE = 10

# prior uniforme
belief = np.ones((BOARD_SIZE, BOARD_SIZE))
belief = belief / belief.sum()

# leer csv
df = pd.read_csv("Sensor_Color_Distribution.csv")

# colores
colors = ["rojo", "naranja", "amarillo", "verde", "azul"]

# convertir csv a diccionario
sensor_distribution = {}

for i in range(len(df)):

    distance = int(df.iloc[i, 0])

    probs = [
        df.iloc[i, 1],
        df.iloc[i, 2],
        df.iloc[i, 3],
        df.iloc[i, 4],
        df.iloc[i, 5]
    ]

    sensor_distribution[distance] = probs

# distancia Manhattan
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# probabilidad del sensor
def sensor_probability(distance, observed_color):

    if distance > max(sensor_distribution.keys()):
        distance = max(sensor_distribution.keys())

    probs = sensor_distribution[distance]

    color_index = colors.index(observed_color)

    return probs[color_index]

# actualizar belief
def update_belief(belief, sensor_x, sensor_y, observed_color):

    new_belief = np.zeros_like(belief)

    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):

            d = manhattan_distance(x, y, sensor_x, sensor_y)

            likelihood = sensor_probability(d, observed_color)

            new_belief[x, y] = belief[x, y] * likelihood

    new_belief = new_belief / new_belief.sum()

    return new_belief

# mostrar y guardar plot
def plot_belief(belief, title, filename):

    plt.figure(figsize=(7, 7))

    plt.imshow(belief, cmap="viridis")

    plt.colorbar(label="Probabilidad")

    plt.title(title)

    plt.xticks(range(BOARD_SIZE))
    plt.yticks(range(BOARD_SIZE))

    plt.savefig(filename)

    plt.show()

# prior
plot_belief(
    belief,
    "Prior uniforme",
    "prior.png"
)

# evidencia 1
belief = update_belief(
    belief,
    2,
    3,
    "rojo"
)

plot_belief(
    belief,
    "Sensor (2,3) = rojo",
    "evidencia_1.png"
)

# evidencia 2
belief = update_belief(
    belief,
    7,
    8,
    "azul"
)

plot_belief(
    belief,
    "Nueva evidencia",
    "evidencia_2.png"
)

# MAP
max_pos = np.unravel_index(
    np.argmax(belief),
    belief.shape
)

print("Celda mas probable:")
print(max_pos)

print("Probabilidad:")
print(belief[max_pos])