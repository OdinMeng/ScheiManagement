# Interfaccia CLI che interagisce l'utente con i dati
# Uso NUMPY
# Idea per dati su JSON
# Esempio
#
#{
#   "hash": [0: "pinco", 1: "pallino", ...],
#   "table": [[1,-1], ..., [1, -1]]
#}

import persona
import os, sys
import numpy as np
import json

# ============
# LAYER 0
def ElencaConti(): # Elenca i conti presenti nella directory "CONTI"
    path = "./CONTI"
    print("=== Conti presenti ===")
    dir = os.listdir(path)
    for entry in dir:
        print(entry)
    
    return 0

def CreateConto(): # Crea una cartella all'interno della cartella "CONTI". In questo momento vado a creare la tabella di dati
    print("Come vuoi chiamare questo conto? Avvertimeno: Se metti un conto già esistente, esso verrà cancellato permanentamente")
    conto = input("> ")
    filepath = "./CONTI/"+conto
    
    # Ottengo i dati sulle persone
    print("Quante persone vuoi istanziare nel conto?")
    num = input("> ")
    try:
        int(num)
    except Exception:
        print("Errore. Uscita dal programma")
        Exit()

    num = int(num)

    # Ottengo i nomi
    names = {}
    for i in range(0, num):
        print("Nome della persona {i}", end="")
        name = input(": ")
        if name in names:
            print("Warning: Stesso nome trovato nella lista dei nomi.")
        names[i]=name

    # Istanzio la matrice nulla
    null = np.zeros((num,num))
    for i in range(0, num):
        null[i][i] = -1 # Do valori indefiniti per il debito "a sè stessi"

    # Salvo tutto sul json
    with open(filepath, "w") as file:
        data = {"hash": names, "table": null.tolist()}
        json.dump(data, file)
        file.close()

    print("Conto creato. Caricando il conto...")
    return data

def LoadConto(nomeconto): # Carica un conto esistente
    try:
        f = open(f"./CONTI/{nomeconto}.json", "r")
    except Exception:
        print("Errore nell'apertura del file. Controllare se il conto esiste.")
        Exit()
    else:
        data = json.loads(f.read())
        f.close()
    return data

def SaveConto():
    pass

def Exit():
    exit(0)

# ==================
# LAYER 1 => Queste funzioni presuppongono la conoscenza del nome del CONTO
def ListaPersona(conto):
    pass

def LeggiDebiti(conto, persona):
    pass

def LeggiCreditori(conto, persona):
    pass

def AggiornaDebito(conto, persona, quantità): #La quantità verra rappresentata in lista [x, y] da poi interagire col modulo soldi
    pass

def OttimizzaConti(conto): # Ottimizza i conti per tutti
    pass

while 1:
    # Codice principale : Layer 0
    print("Welcome to ScheiManagement! How can I help you?")
    print("1. Create session\n2. Load Session\n3. Exit")
    selector = {"1": CreateConto, "2": LoadConto, "3": Exit}
    choice = input("> ")

    table = selector[choice]()

    while 1:
    # Codice principale: Layer 1
        print("Welcome to the data. Select an operation.")
        print("1. View table\n2. View Debts by Person\n3. View Credits by Person\n4. Update Debt\n5. Optimize Table\n6. Exit")
        n_selector = {"1": ListaPersona, "2": LeggiDebiti, "3": LeggiCreditori, "4": AggiornaDebito, "5": OttimizzaConti, "6":Exit}
        n_choice = input("> ")

        if n_choice in ["1", "5", "6"]: # Operations with no arguments
            n_selector[n_choice]()

        if n_choice in ["2", "3"]: # Operations with 1 argument
            print("Argument: ", end="")
            first_argument = input("")
            if first_argument not in data[hash]:
                print(f"User '{first_argument}' not found. Request ignored")
                continue

            n_selector[n_choice](first_argument)

            # da gestire se i tosi non esistono
            pass #TODO

            