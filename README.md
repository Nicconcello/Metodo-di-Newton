# Metodo-di-Newton

## 📋 Descrizione

Il software permette all'utente di inserire una qualsiasi funzione matematica (in formato simbolico) e un punto di partenza. Lo script calcola automaticamente la derivata simbolica, esegue l'algoritmo di Newton e genera un grafico interattivo che illustra geometricamente come la soluzione viene approssimata.

### Caratteristiche Principali
* **Input Simbolico:** Grazie a `SymPy`, l'utente può inserire funzioni come `x**2 - 2`, `cos(x) - x`, o `exp(x) - 4` senza dover modificare il codice.
* **Derivata Automatica:** Il programma calcola analiticamente la derivata $f'(x)$ necessaria per l'algoritmo.
* **Visualizzazione Grafica:** Utilizza `Matplotlib` per tracciare la funzione, le linee verticali di proiezione e le rette tangenti per ogni iterazione.
* **Safety Checks:** Include controlli per prevenire loop infiniti e gestire errori di divisione per zero.

## 🧮 Cenni Teorici

Il metodo di Newton-Raphson è un algoritmo iterativo per trovare le radici di una funzione differenziabile $f(x)$ (ovvero le soluzioni a $f(x) = 0$).

La formula ricorsiva utilizzata è:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Geometricamente, $(x_{n+1})$ è l'intersezione dell'asse delle x con la tangente al grafico di $f$ nel punto $(x_n, f(x_n))$.
