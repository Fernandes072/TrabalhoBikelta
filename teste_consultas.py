#Definindo os modelos de bicicleta
modelos = {
    "M01": ["Caloi Vulcan Aro 29 com 21 Velocidades", "Caloi", "Comum", "21", "2021"],
    "M02": ["Caloi E-Vibe City", "Caloi", "Elétrica", "0", "2020"],
    "M03": ["Sense Bike Impulse E Trail Comp 2021/22", "Sense", "Elétrica", "0", "2022"],
    "M04": ["MTB KLS Sport Gold Aro 29 Freio Disco 21 Marchas", "KLS", "Comum", "21", "2019"]
}

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

#Definindo reservas
reservas = {
    "M01": ["U001"],
    "M02": [],
    "M03": [],
    "M04": []
}

#Definindo Usuários
usuarios = {
    "U001": ["ind", "Maria Bonita"],
    "U003": ["coo", "Associação Itabaiana de Guias de Turismo"]
}

#Definindo empréstimos
#"U003": ["M01"]
emprestimos = {
    "U001": [],
    "U003": []
}

#Definindo estações
estacao1 = ["B0001", "B0003", "B0005", "B0007"]
estacao2 = ["B0002", "B0004", "B0006", "B0008"]

#Funcão de Consulta
def consulta(dados_consulta):
    try:
        if dados_operacao[1] == "*":
            for a in modelos:
                aux_exibicao_modelo = modelos[a]
                print("Código:", a + ",", "Descrição:", aux_exibicao_modelo[0] + ",", "Marca:", aux_exibicao_modelo[1] + ",", "Categoria:", aux_exibicao_modelo[2]+ ",", "Marchas:", aux_exibicao_modelo[3] + ",", "Ano:", aux_exibicao_modelo[4])
        elif dados_operacao[1] == "M01" or dados_operacao[1] == "M02" or dados_operacao[1] == "M03" or dados_operacao[1] == "M04":
            aux_consulta1 = modelos[dados_consulta[1]]
            print("Descrição:", aux_consulta1[0])
            aux_consulta2 = reservas[dados_consulta[1]]
            if len(aux_consulta2) != 0:
                print("Quantidade de reservas:", len(aux_consulta2))
                aux_consulta3 = reservas[dados_consulta[1]]
                for b in usuarios:
                    for c in aux_consulta3:
                        if b == c:
                            aux_consulta4 = usuarios[b]
                            print("Usuário com reserva:", aux_consulta4[1])
            else:
                print("Quantidade de reservas: 0")
            if dados_consulta[1] == "M01":
                aux_codigo_bicicleta1 = "B0001"
                aux_codigo_bicicleta2 = "B0002"
            elif dados_consulta[1] == "M02":
                aux_codigo_bicicleta1 = "B0003"
                aux_codigo_bicicleta2 = "B0004"
            elif dados_consulta[1] == "M03":
                aux_codigo_bicicleta1 = "B0005"
                aux_codigo_bicicleta2 = "B0006"
            else:
                aux_codigo_bicicleta1 = "B0007"
                aux_codigo_bicicleta2 = "B0008"
            print("Código da bicicleta modelo", dados_consulta[1] + ":", aux_codigo_bicicleta1)
            print("Código da bicicleta modelo", dados_consulta[1] + ":", aux_codigo_bicicleta2)
            aux_consulta5 = 0
            aux_consulta6 = 0
            for d in estacao1:
                if aux_codigo_bicicleta1 == d:
                    print("Bicicleta", aux_codigo_bicicleta1,"disponível na estação 1")
                    aux_consulta5 = 1
                if aux_codigo_bicicleta2 == d:
                    print("Bicicleta", aux_codigo_bicicleta2,"disponível na estação 1")
                    aux_consulta6 = 1
            for e in estacao2:
                if aux_codigo_bicicleta1 == e:
                    print("Bicicleta", aux_codigo_bicicleta1,"disponível na estação 2")
                    aux_consulta5 = 1
                if aux_codigo_bicicleta2 == e:
                    print("Bicicleta", aux_codigo_bicicleta2,"disponível na estação 2")
                    aux_consulta6 = 1
            aux_consulta9 = 0
            if aux_consulta5 == 0:
                for f in emprestimos:
                    aux_consulta7 = emprestimos[f]
                    for g in aux_consulta7:
                        if g == dados_consulta[1]:
                            aux_consulta8 = usuarios[f]
                            if aux_consulta9 == 1:
                                print("Bicicleta", aux_codigo_bicicleta2, "emprestada para", aux_consulta8[1])
                            else:
                                print("Bicicleta", aux_codigo_bicicleta1, "emprestada para", aux_consulta8[1])
                                aux_consulta9 = 1
            if aux_consulta6 == 0:
                if aux_consulta9 == 0:
                    for f in emprestimos:
                        aux_consulta7 = emprestimos[f]
                        for g in aux_consulta7:
                            if g == dados_consulta[1]:
                                aux_consulta8 = usuarios[f]
                                print("Bicicleta", aux_codigo_bicicleta2, "emprestada para", aux_consulta8[1])
        else:
            print("Informações para consulta inválidas")
    except IndexError:
        print("Erro: Informações para consulta insuficientes")

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
    elif dados_operacao[0] == "reb":
        reserva(dados_operacao)
    elif dados_operacao[0] == "bik":
        consulta(dados_operacao)
    operacao = "fim"
