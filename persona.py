# Definizione della classe "persona" con le sue funzioni
import os

class Persona:
    def __init__(self, nome, debiti={}):
        self.nome = nome
        self.debiti = debiti

    def LeggiDebiti(self):
        pass

    def LeggiDebitori(self):
        pass

    def AggiornaDebito(self, debitore):
        pass
    
    def JSONDump(self):
        pass
