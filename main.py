import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
# indepencent = unabhängige Variable - wird beobachtet
# dependent = abhängige Variable - wird erklärt

# Fehlerfunktion - wird nach allen Parametern abgeleitet (mean squared error)
def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].independent
        y = points.iloc[i].dependent
        total_error += (y - (m * x + b) ** 2)
    total_error / float(len(points))

# Gradientenabstiegsfunktion
def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].independent
        y = points.iloc[i].dependent

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now)) # partielle Ableitung Fehlerfunktion nach m
        b_gradient += -(2/n) * (y - (m_now * x + b_now)) # partielle Ableitung Fehlerfunktion nach b

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.0001 # Lernrate
epochs = 1000 # Anzahl Durchläufe

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, data, L)

print(m, b)

# Zeichnen der Datenpunkte + Funktion
plt.scatter(data.independent, data.dependent, color="black")
plt.plot(list(range(20, 80)), [m * x + b for x in range(20, 80)], color="red")
plt.show()


