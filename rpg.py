class servivo():
    def __init__(self , hp , atack):
         self.hp = hp
         self.atack = atack        

class pessoa(servivo):
    def __init__(self,hp ,atack, nome):       
        super().__init__(hp , atack)
        self.nome = nome
        print("Pessoa:")
        print("nome:............" + self.nome)
        print("pontos de vida:.." + str(self.hp))
        print("pontos de atack:." + str(self.atack))
        print("---------------------------------------")

class monstro(servivo):
    def __init__(self, hp, atack):
         self.hp = hp
         self.atack = atack
         super().__init__(hp, atack)

class goblin(monstro):
    def __init__(self, hp, atack, inteligencia):
        self.inteligencia = inteligencia
        super().__init__(hp, atack) 
        print("goblin:") 
        print("pontos de vida:.." + str(self.hp))
        print("pontos de atack:." + str(self.atack))
        print("inteligencia:...." + str(self.inteligencia))
        print("---------------------------------------")

class lobo(monstro):
    def __init__(self, hp, atack, forca):
        self.forca = forca
        super().__init__(hp, atack) 
        print("lobo:")  
        print("pontos de vida:.." + str(self.hp))
        print("pontos de atack:." + str(self.atack))
        print("força:..........." + str(self.forca))  
        print("---------------------------------------")         
        



s2=pessoa(500, 50, "francinaldo")
s4=goblin(200, 100, 600)
s5=lobo(400, 250, 800)