# Definizione della classe "persona" con le sue funzioni
import os
import json
from soldi import Soldi 

class Persona:
    def __init__(self, nome, debiti={}):
        self.nome = nome
        self.debiti = debiti
        # Esempio di debito: {"A.": [2, 89], "X.": [100, 2], ...}

    def LeggiDebiti(self):
        s = ""
        for debito in self.debiti:
            s += f"{debito}: €{self.debiti[debito][0]}.{self.debiti[debito][1]} \n" 
            # NOTA: Questa linea presuppone che il debito sia rappresentato in lista [x, y] da possibilmente interagire con la classe Soldi.
        s += "Per le altre persone non elencate... non ci sono debiti"
        return s

    def LeggiCreditori(self, conto): # Conto viene dato dall'input leggendo la cartella del conto
        
        pass

    def AggiornaDebito(self, debitore, differenza):
        try:
            self.debiti[debitore]

        except:
            return False
        
        else:
            SoldiDebitore = Soldi(self.debiti[debitore][0], self.debiti[debitore][1])
            SoldiDiff = Soldi(differenza[0], differenza[1])
            SoldiTot = SoldiDebitore + SoldiDiff
            self.debiti[debitore] = SoldiTot.RapprLIST()
            return True
    
    def JSONDump(self):
        return json.dumps({"Nome": self.nome, "Conto": self.conto, "Debiti": self.debiti})
            # Esempio di output
            # { "Nome": "S.",
            #   "Debiti": { "M.": [1, 20], "A.": [200, 89], ... }
            # }

