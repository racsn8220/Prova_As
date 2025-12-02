#1 
preco = float(input("Digite o preco do produto: "))
if preco < 0:
    print("Valor invalido! O preco nao pode ser negativo.")
elif preco < 50:
    print("Barato")
elif preco <= 199:
    print ("Medio")
else:
    print("caro")
#2
pacotes_comprados = 8
consumo_diario = 35
consumo_mensal = consumo_diario * 30
peso_total_disponivel = pacotes_comprados * 500 
cafe_sobrando = peso_total_disponivel - consumo_mensal
print("Cafe sobrando no final do mes:", cafe_sobrando, "gramas")

#3 
servicos = ["consultoria", "manutencao", "suporte" , "treinamento", "limpeza"]

lista_premium = ["consultoria", "treinamento"]
lista_basica = ["manutencao", "suporte",]
lista_terceirizada = ["limpeza"]

for servico in servicos:
    if servico in lista_premium:
        print(servico, "e um servico premium.")
    elif servico in lista_basica:
        print(servico, "e um servico basico.")
    elif servico in lista_terceirizada:
        print(servico, "e um servico terceirizado.")

#4 
produtos = {
    101: "caderno",
    102: "caneta",
    103: "lapis",
    104: "marca-texto",
    105: "borracha"
}
codigo = int(input("Digite o codigo do produto: "))
if codigo in produtos:
    print("O produto correspondente ao codigo", codigo, "e:", produtos[codigo])
else:
    print("coidigo invalido")
#5
def calcular_juros_simples(investimento_inicial, taxa_juros_mensal, numero_meses):
    juros = investimento_inicial * (taxa_juros_mensal / 100) * numero_meses
    valor_final = investimento_inicial + juros
    return valor_final
investimento_inicial = float(input("Digite o valor de investimento inicial: "))
taxa_juros_mensal = float(input("Digite a taxa de juros mensal : "))
numero_meses = int(input("Digite o numero de meses: "))
valor_final = calcular_juros_simples(investimento_inicial, taxa_juros_mensal, numero_meses)
print("O valor final apos", numero_meses, "meses e:", valor_final)

   
    


    



