class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10,36) if i % 2 == 0] #cria lista de peso de halteres de 10 - 36 com apenas numeros pares
        self.porta_halteres = {i: i for i in range(10,36) if i % 2 == 0}#cria dicionário com lugar do peso e qual peso está neste lugar (ex: lugar do peso 14 e peso 12 está neste)
        self.halter_em_utilizacao = []
        self.reinicia_organizacao()
        
    def reinicia_organizacao(self):
        self.porta_halteres =  {i: i for i in range(10,36) if i % 2 == 0}
        
    def listar_halter_disponivel(self):
        return self.halteres
    
    def listar_porta_halteres(self):
        return self.porta_halteres
    
    def usar_halter(self, halter_utilizacao):
        if halter_utilizacao in self.halteres:
            for chave, valor in self.porta_halteres.items():
                if valor == halter_utilizacao:
                    self.porta_halteres[chave] = None
                    self.halteres.remove(halter_utilizacao)
                    self.halter_em_utilizacao.append(halter_utilizacao)
                    break
        else:
            print("VALOR NÃO EXISTENTE")
                
    def devolver_halter(self, halter_devolvido, posicao):
        if halter_devolvido in self.halter_em_utilizacao:
            for chave, valor in self.porta_halteres.items():
                if chave == posicao:
                    self.porta_halteres[chave] = halter_devolvido
                    self.halter_em_utilizacao.remove(halter_devolvido)
                    
                    break
        else:
            print("VALOR NÃO EXISTENTE")


        
        
        
    
    
    
    
            
        
        



        