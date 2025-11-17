# Random Seed Generator (C)

Generatore di numeri pseudo-casuali scritto in C.  
Il programma utilizza la funzione `time(NULL)` per estrarre un seed variabile in base al momento dell’esecuzione e genera una sequenza di numeri pseudo-casuali tramite il PRNG standard della libreria C.

---

## 🔧 Obiettivo
Capire come funziona la generazione di numeri casuali a basso livello e come il *seed* influenza completamente la sequenza prodotta.  
È un esercizio utile per imparare:

- come inizializzare un PRNG in C  
- come usare il tempo come seed  
- come gestire sequenze casuali e riproducibilità  
- differenza tra casuale “vero” e pseudo-casuale

---

## 🚀 Come funziona
1. Legge il tempo corrente tramite `time(NULL)`  
2. Usa quel valore come seed per `srand()`  
3. Genera numeri con `rand()` in sequenza  
4. Ogni esecuzione produce risultati diversi (dipendenti dal seed)
