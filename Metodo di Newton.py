import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1. Definisci che 'x' è il tuo simbolo matematico
x = sp.symbols('x')

scf = str(input("Inserisci una funzione: "))

fx = sp.sympify(scf)

fpx = sp.diff(fx, x)

fxn = sp.lambdify(x, fx)
fpxn = sp.lambdify(x, fpx)

scn = float(input("Inserisci x0 per iniziare: "))

epsilon = 1e-10

#range del grafico
x_grafico = np.linspace(-10, 10, 1000)
#y riferita alle x nel range
y_grafico = fxn(x_grafico)
#disegna la funzione
plt.plot(x_grafico, y_grafico, label="f(x)")
#disegna l'asse x
plt.axhline(0, color="black", linewidth=1)

fit = scn - (fxn(scn) / fpxn(scn))

while abs(fxn(fit)) > epsilon:
    # X: [da scn, a scn] -> Rimane fermo sulla verticale
    # Y: [da altezza 0, a altezza funzione] -> Sale su
    plt.plot([scn, scn], [0, fxn(scn)], color='green', linestyle='--')
    # Lista delle X: [da dove parto, dove arrivo]
    # Lista delle Y: [altezza partenza, altezza arrivo (zero)]
    plt.plot([scn, fit], [fxn(scn), 0], color='red', linestyle='--')
    
    scn = fit
    fit = scn - (fxn(scn) / fpxn(scn))
    
print (scn)

plt.legend()  # Mostra le etichette
plt.grid()    # Mette la griglia di sfondo (utile per vedere i numeri)
plt.show()    # Apre la finestra col grafico