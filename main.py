# Interfaccia CLI che interagisce l'utente con i dati
# Uso NUMPY
# Idea per dati su JSON
# Esempio
#
#{
#   "hash": [0: "pinco", 1: "pallino", ...],
#   "table": [[1,-1], ..., [1, -1]]
#}

"""
Convention:

x 0 1 2 3
0 - b c d
1 x - y z
2 f g - h
3 p q r -

means

0 owes 1: b
0 owes 2: c
0 owes 3: d

so line: guy who owes
column: owed guy

so table[0] returns EVERY debt of person 0

"""


import os
import numpy as np
import json
from soldi import Soldi

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

    # Ottengo i nomi: creo l'hash
    names = {}
    for i in range(0, num):
        print(f"Nome della persona {i}", end="")
        name = input(": ")
        if name in names:
            print("Warning: Stesso nome trovato nella lista dei nomi.")
        names[str(i)]=name

    # Istanzio la matrice dei debiti, con i valori numerici rappresentati in coppie di soldi
    null = []
    for i in range(1, 10):
        newnull = []
        for j in range(1, 10):
            if i == j:
                newnull.append([-1, -1]) # non ha senso!
            else:
                newnull.append([0,0])
        null.append(newnull)

    # Salvo tutto sul json
    with open(filepath, "w") as file:
        data = {"hash": names, "table": null}
        json.dump(data, file)
        file.close()

    print("Conto creato. Caricando il conto...")
    return data

def LoadConto(nomeconto): # Carica un conto esistente
    try:
        f = open(f"./CONTI/{nomeconto}", "r")
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
    exit()

# ==================
# LAYER 1 => Queste funzioni presuppongono la conoscenza del nome del CONTO
def ListaPersona(data):
    # 1. print debts person by person (format: x owes y value)
    table = data["table"]
    hash = data["hash"]
    table_np = np.array(table)
    num = len(hash)

    print("Direct Mode")
    for i in range(num):
        for j in range(num):
            value = table_np[i][j]
            if value[0] == -1 and value[1] == -1:
                continue

            else:
                soldo = Soldi(value[0], value[1])
                debt = soldo.RapprSTR()
                print(f"{hash[str(i)]} owes {hash[str(j)]} €{debt}")
    print("="*15)
    print("Tabular Mode")
    # header

    # n = 3
    print("\t", end="")
    for i in range(num):
        nome = hash[str(i)]

        if len(nome)>6:
            nome = hash[str(i)][0:6]+"."

        print(nome, end="\t")

    print()

    for i in range(num):
        nome = hash[str(i)]

        if len(nome)>6:
            nome = hash[str(i)][0:6]+"."

        print(nome, end="\t")
        for j in range(num):
            value = table_np[i][j]
            soldo = Soldi(value[0], value[1])
            s = soldo.RapprSTR()

            if s=="-1.-1":
                s="NULL"

            print(s, end="\t")
        print()

    return None

def AggiornaDebito(data, debtor, creditor, quantity): # La quantità verra rappresentata in lista [x, y] da poi interagire col modulo soldi
    # NOTA: Ignoro quantità negative, avverto e sarà forse il caso di spezzare l'aggiornamento del debito in più parti
    # cerco il numero associato al tizio

    # get and convert data
    table = data["table"]
    hash = data["hash"]
    table_np = np.array(table)
    num = len(hash)

    quantity_vec = list(map(int, quantity.split("."))) # magic!
    quantity_value = Soldi(quantity_vec[0], quantity_vec[1])

    i = -1
    j = -1

    for number in hash:
        if hash[number] == debtor:
            i = number

        if hash[number] == creditor:
            j = number

    if i == -1 or j == -1:
        print("This should not happen.")
        return None # Errore
    
    # Acess array in ij position and attempt to sum
    i = int(i)
    j = int(j)
    access = table_np[i][j]
    if access[0] == -1 and access[1] == -1:
        print("Error: debtor and creditor is same.")
        return -1 # shouldn't happen tbh

    original_value = Soldi(access[0], access[1])
    new_value = original_value + quantity_value

    if new_value.centesimi < 0 or new_value.interi < 0:
        print("Error: Sum becomes negative. Consider breaking the repayment into two parts.")
        return None
    
    else:
        print(f"{debtor}'s debt of {creditor}: from €{original_value.RapprSTR()} to €{new_value.RapprSTR()}")
        table_np[i][j] = new_value.RapprLIST()

        return table_np.tolist()

def OttimizzaConti(data): # Ottimizza i conti per tutti
    hash = data["hash"]
    table = data["table"]
    table_np = np.array(table)
    num = len(hash)

    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            else:
                access_ij = table_np[i][j]
                value_ij = Soldi(access_ij[0], access_ij[1])

                access_ji = table_np[j][i]
                value_ji = Soldi(access_ji[0], access_ji[1])

                cfr = value_ij.cfr(value_ji)

                if cfr == 0:
                    print(f"{hash[str(i)]} and {hash[str(j)]} have same debts. Both of the debts will be simultaneously cancelled")
                    table_np[i][j] = [0,0]
                    table_np[j][i] = [0,0]

                elif cfr<0:
                    # Caso ji > ij => ji-ij > 0
                    print(f"{hash[str(i)]}'s debt to {hash[str(j)]}: €{value_ij.RapprSTR()} to €0.00")
                    table_np[i][j] = [0,0]

                    # calcolo la differenza
                    new = value_ji + value_ij.minus()
                    print(f"{hash[str(j)]}'s debt to {hash[str(i)]}: €{value_ji.RapprSTR()} to €{new.RapprSTR()}")
                    table_np[j][i] = new.RapprLIST()

                elif cfr>0:
                    # Caso ij > ji => ij-ji > 0
                    print(f"{hash[str(j)]}'s debt to {hash[str(i)]}: €{value_ji.RapprSTR()} to €0.00")
                    table_np[j][i] = [0,0]

                    # calcolo la differenza
                    new = value_ij + value_ji.minus()
                    print(f"{hash[str(i)]}'s debt to {hash[str(j)]}: €{value_ij.RapprSTR()} to €{new.RapprSTR()}")
                    table_np[i][j] = new.RapprLIST()

    return table_np.tolist()

# funzioni di ottimizzazione
def is_in_hash(argument, data):
    n = -1
    hash = data["hash"]

    for number in hash:
        if hash[number] == argument:
            n = number

    if n == -1:
        print(f"User '{argument}' not found. Request ignored")
        return 0
    
    else:
        return 1

# Main code
# =======================
while 1:
    # Codice principale : Layer 0
    print("Welcome to ScheiManagement! How can I help you?")
    print("1. Create session\n2. Load Session\n3. Exit")
    selector = {"1": CreateConto, "2": LoadConto, "3":Exit}
    choice = input("> ")
    data = None

    if choice not in selector:
        print ("Invalid argument: request ignored.")
        continue
    
    if choice in ["1", "3"]:
        data = selector[choice]() # DATA IS RAW!!!

    fn = ""
    if choice in ["2"]:
        print("Name: ", end="")
        filename = input("")
        fn = filename
        data = selector[choice](filename)

    print("Welcome to the data. Select an operation.")

    print(data)
    while 1:
    # Codice principale: Layer 1
        print("1. View Table \n2. Update Debt\n3. Optimize Table\n4. Exit")
        n_selector = {"1": ListaPersona, "2": AggiornaDebito, "3": OttimizzaConti, "4":Exit}
        n_choice = input("> ")

        if n_choice == "4":
            with open(f"./CONTI/{fn}", "w") as f:
                json.dump(data, f)
                f.close()

            print("Files saved. Exiting...")
            break # exit


        if n_choice in ["1", "3"]: # Operations with no arguments
            result = n_selector[n_choice](data)

            if type(result) != type(None):
                data["table"] = result

            print("Done")

        elif n_choice in ["2"]: # operations with 3 arguments
            print("Argument (debtor): ", end="")
            first_argument = input("")

            if not is_in_hash(first_argument, data):
                continue

            print("Second Argument (creditor): ", end="")
            second_argument = input("")

            if not is_in_hash(second_argument, data):
                continue
                
            if first_argument == second_argument:
                print("Error: debtor and creditor are the same. Ignored.")
                continue

            print("Second Argument (quantity, rounded to format x.xx): ", end="")
            third_argument = input("")

            try:
                third_argument = float(third_argument)
                third_argument = round(third_argument, 2)
                third_argument = str(third_argument)
            except:
                print("Value (quantity) not convertible to integer. Request ignored")
                continue

            esito = n_selector[n_choice](data, first_argument, second_argument, third_argument)
            data["table"] = esito

            print(f"Done\n")
            pass

        else:
            print("Command not recognized. Request ignored.")
            continue


# BUG NOTI
# 1. 0.20 viene riconosciuto come 0.02. Fix temporaneo: inserire 0.199 che viene arrotondato a 0.20
