
   
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
