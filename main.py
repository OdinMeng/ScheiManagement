# Interfaccia CLI che interagisce l'utente con i dati

import os
import persona

# Funzioni (?)
# LAYER 0
def LoadConto(): # Prendi input, verifica se esiste cartella -> se sì, accetta e prosegui al LAYER 1; -> se no, CreateConto(nomeConto)
    pass

def SaveConto():
    pass

def CreateConto(nomeConto=""): # Crea una cartella all'interno della cartella "SESSIONI"
    pass

def Exit():
    pass

# LAYER 1 => Queste funzioni presuppongono la conoscenza del nome del CONTO
def ListaPersona(conto):
    pass

def LeggiDebiti(conto, persona):
    pass

def LeggiCreditori(conto, persona):
    pass

def AggiornaDebito(conto, persona, quantità): #La quantità verra rappresentata in lista [x, y] da poi interagire col modulo soldi
    pass

def CreaTabella(conto):
    pass

def CreaUtente(conto, nome): # Crea un file JSON del toso
    pass

def DelUtente(conto, nome):
    pass

def OttimizzaConti(conto): # Ottimizza i conti per tutti
    pass

# Codice principale
print("Welcome to ScheiManagement! How can I help you?")
print("1. Create session\n2. Load Session\n3. Exit")
selector = {"1": CreateConto, "2": LoadConto, "3": Exit}
choice = input("> ")
