# Definisce la classe "Soldi" per evitare dei casini con i float... grr grr
# Rappresentazione in JSON: [interi, centesimi] dev'essere possibile
# Ogni soldo viene rappresentato come una coppia di numeri: interi e centesimi

class Soldi:
    def __init__(self, interi, centesimi): #NOTA: interi, centesimi >= 0 e ∈ ℕ (NO FLOAT!)
        self.interi = interi
        if centesimi >= 100:
            self.interi += centesimi//100
            self.centesimi = centesimi%100

        else:
            self.centesimi = centesimi

    def __add__(self, other):
        TOTinteri = self.interi + other.interi
        TOTcentesimi = self.centesimi + other.centesimi

        # Caso 1: TOTc >= 100
        if TOTcentesimi >= 100:
            TOTinteri += TOTcentesimi//100
            TOTcentesimi %= 100

        # Caso 2: TOTc < 0:
        elif -100 < TOTcentesimi < 0:
            TOTinteri += -(-1 * TOTcentesimi // 100)
            if (-1 * TOTcentesimi % 100)!=0:
                TOTinteri -= 1
                TOTcentesimi = 100-(-TOTcentesimi%100)

        return Soldi(TOTinteri, TOTcentesimi)
    
    def RapprSTR(self):
        return f"{self.interi}.{self.centesimi}" # Rappresentazione in stringa (discutibilmente utile)

    def RapprLIST(self):
        return [self.interi, self.centesimi] # Rappresentazione in lista (molto utile!)