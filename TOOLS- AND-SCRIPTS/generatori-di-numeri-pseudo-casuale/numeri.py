import ctypes
import time


sacrificio = 0                             #dichiaro il contenitore ""sacrificio" con valore 0

# Carico la libreria C che genera un seme casuale dal tempo (millisecondi)
try:
    tempo_C = ctypes.WinDLL("C:\\Users\\gianl\\Desktop\\c e python\\seed_generator.dll")  #la varibiale tempo_C assumera il valore della libreria prima codice
except OSError as f:
    print(f"ci sta un errore{f}")
    exit(1)      

get_seme = tempo_C.seed_tempo
get_seme.restype = ctypes.c_int    

tot = 0  

# Ciclo principale - ripeto 5 volte la generazione e analisi del numero
while sacrificio < 5:  

    c = get_seme()   

    d = str(c)   

    primo = int(d[0])   # assocciazione primo array alla variabile primo
    secondo =  int(d[1])  #assocciazizone secondo array alla variabile seconod
    terzo = int(d[2])   # assocciazione 3 array alla varibaile terzo

    r = primo+secondo+terzo   

# confronto della somma fatta prima. se il numero è magiore di 10 significa ceh è a due cifre se no è a una cifra
    if r >= 10:  
        
        print("deduco che ha 2 cifre") 
        w = str(r)  

        primoprimo = int(w[0])  
        secondosecondo = int(w[1])

        totale = primoprimo + secondosecondo   

        tot = totale                

    else:  #se il blocco if non parte signfica che è a una cifra quindi uso direttamente al varibile r per scegliere i  numeri
        print("deduco che ha una cifra")
  
    
 

    if r == 1 or tot == 1:       
        print("1")                #stampatura per in caso un debuggin ecaprie cos asta succededno
        sacrificio = sacrificio +1    #conteggio del contatore cosi da poter usare il valore come confronto


    elif r == 2 or tot == 2:    # ragionamento uguale per ogni blocco di elif 
        print("2")
        sacrificio += 1

 
    elif r == 3 or tot == 3:
        print("3")
        sacrificio += 1


    elif r == 4 or tot == 4:
        print("4")
        sacrificio += 1


    elif r == 5 or tot == 5:
        print("5")
        sacrificio += 1



    elif r == 6 or tot == 6:
        print("6")
        sacrificio += 1

 

    elif r == 7 or tot == 7: 
        print("7")
        sacrificio +=1


    elif r == 8 or tot == 8:
        print("8")
        sacrificio +=1



    elif r == 9 or tot == 9:
        print("9")
        sacrificio += 1


    else:             #finale che se nessun funziona ilnumero puo essere 0.
        print("0")    

        
    
print(sacrificio)    #stampa il risultato del contneitore finale