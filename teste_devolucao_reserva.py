#Definindo as bicicletas
bicicletas = {
    "B0001": ["M01", "C3C00010", "E01", "Disponível"],
    "B0002": ["M01", "C3C00018", "E02", "Disponível"],
    "B0003": ["M02", "C1E00002", "E01", "Disponível"],
    "B0004": ["M02", "C1E00027", "E02", "Disponível"],
    "B0005": ["M03", "S5E000010", "E01", "Disponível"],
    "B0006": ["M03", "S5E000011", "E02", "Disponível"],
    "B0007": ["M04", "K11C00046", "E01", "Disponível"],
    "B0008": ["M04", "K11C00057", "E02", "Disponível"]
}

#Definindo os modelos de bicicleta
modelos = {
    "M01": ["Caloi Vulcan Aro 29 com 21 Velocidades", "Caloi", "Comum", "21", "2021"],
    "M02": ["Caloi E-Vibe City", "Caloi", "Elétrica", "0", "2020"],
    "M03": ["Sense Bike Impulse E Trail Comp 2021/22", "Sense", "Elétrica", "0", "2022"],
    "M04": ["MTB KLS Sport Gold Aro 29 Freio Disco 21 Marchas", "KLS", "Comum", "21", "2019"]
}

#Definindo Usuários
usuarios = {
    "U001": ["ind", "Maria Bonita"],
    "U003": ["coo", "Associação Itabaiana de Guias de Turismo"]
}

#Definindo empréstimos
#"U003": ["M01"]
emprestimos = {
    "U001": ["M01"],
    "U003": []
}

#Definindo estações
estacao1 = ["B0003", "B0005", "B0007"]
estacao2 = ["B0002", "B0004", "B0006", "B0008"]

#Funcão de Devolucão
def devolucao(dados_devolucao):
    aux_teste_devolucao1 = 0
    aux_teste_devolucao2 = 0
    aux_teste_devolucao3 = 0
    try:
        for a in bicicletas:
            if a == dados_devolucao[1]:
                aux_teste_devolucao1 = 1
        if (dados_devolucao[2] == "E01") or (dados_devolucao[2] == "E02"):
            aux_teste_devolucao2 = 1
        for b in usuarios:
            if b == dados_devolucao[3]:
                aux_teste_devolucao3 = 1
        if aux_teste_devolucao1 == 0:
            print("Erro: Código de bicicleta inválido")
        if aux_teste_devolucao2 == 0:
            print("Erro: Código de estação inválido")
        if aux_teste_devolucao3 == 0:
            print("Erro: Código de usuário inválido")
        if (aux_teste_devolucao1 == 1) and (aux_teste_devolucao2 == 1) and (aux_teste_devolucao3 == 1):
            aux_devolucao1 = emprestimos[dados_devolucao[3]]
            aux_devolucao2 = 0
            if (dados_devolucao[1] == "B0001") or (dados_devolucao[1] == "B0002"):
                aux_devolucao3 = "M01"
            elif (dados_devolucao[1] == "B0003") or (dados_devolucao[1] == "B0004"):
                aux_devolucao3 = "M02"
            elif (dados_devolucao[1] == "B0005") or (dados_devolucao[1] == "B0006"):
                aux_devolucao3 = "M03"
            else:
                aux_devolucao3 = "M04"
            for c in aux_devolucao1:
                if c == aux_devolucao3:
                    aux_devolucao2 = 1
            if aux_devolucao2 == 1:
                if (dados_devolucao[1] == "B0001") or (dados_devolucao[1] == "B0002"):
                    aux_devolucao1.remove("M01")
                    aux_devolucao3 = "M01"
                elif (dados_devolucao[1] == "B0003") or (dados_devolucao[1] == "B0004"):
                    aux_devolucao1.remove("M02")
                    aux_devolucao3 = "M02"
                elif (dados_devolucao[1] == "B0005") or (dados_devolucao[1] == "B0006"):
                    aux_devolucao1.remove("M03")
                    aux_devolucao3 = "M03"
                else:
                    aux_devolucao1.remove("M04")
                    aux_devolucao3 = "M04"
                emprestimos.update({dados_devolucao[3]: aux_devolucao1})
                aux_devolucao_nome_usuario = usuarios[dados_devolucao[3]]
                aux_devolucao_nome_usuario = aux_devolucao_nome_usuario[1]
                aux_devolucao_modelo_bicicleta = modelos[aux_devolucao3]
                aux_devolucao_modelo_bicicleta = aux_devolucao_modelo_bicicleta[0]
                print("Devolução realizada com sucesso")
                print("Nome do usuário:", aux_devolucao_nome_usuario)
                print("Modelo Bicicleta:", aux_devolucao_modelo_bicicleta)
                if dados_devolucao[2] == "E01":
                    estacao1.append(dados_devolucao[1])
                else:
                    estacao2.append(dados_devolucao[1])
            else:
                print("Erro: Não há empréstimo da bicileta")
    except IndexError:
        print("Erro: Informações para devolução insuficientes")

#Início do programa
operacao = input("Operação: ")
while operacao != "fim":
    dados_operacao = operacao.split()
    if dados_operacao[0] == "cdu":
        cadastro(dados_operacao)
    elif dados_operacao[0] == "emb":
        emprestimo(dados_operacao)
    elif dados_operacao[0] == "dvb":
        devolucao(dados_operacao)
    operacao = "fim"

print(emprestimos)
print(estacao1)
print(estacao2)