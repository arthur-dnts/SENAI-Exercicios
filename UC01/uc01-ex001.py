class Destino:
    def __init__(self, cidade, clima, local, custo):
        self.cidade = cidade
        self.clima = clima
        self.local = local
        self.custo = custo

    def combina_com(self, cilma, local, orcamento):
        return (
            self.clima == clima and
            self.local == local and
            self.custo <= orcamento
        )

# Lista com os possíveis locais de destino
destinos = [
    Destino("Rio de Janeiro", "quente", "urbano", 2000),
    Destino("Gramado", "frio", "urbano", 2500),
    Destino("Lençóis Maranhenses", "quente", "natureza", 1800),
    Destino("Campos do Jordão", "frio", "natureza", 2500)
]

# Coleta os dados do usuários
print("Sistema de Recomendação de viagens")

clima = input("Qual a sua preferência de clima [quente/frio]? ")
local = input("Qual a sua preferência de local [urbano/natureza]? ")
orcamento = float(input("Qual é o seu orçamento para a viagem (R$)? "))

# Busca o destino com base nas preferências do usuário
encontrado = False
for destino in destinos:
    if destino.combina_com(clima, local, orcamento):
        print(f"\nSugestão: {destino.cidade}")
        print("Destino encontrado! Boa viagem.")
        encontrado = True
        break
    
if not encontrado:
    print("Não foi possível localizar um destino compatível com suas preferências.")
