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
    "U002": ["ind", "Maria"],
    "U003": ["ind", "Joao"],
    "U004": ["coo", "Associação Itabaiana de Guias de Turismo"]
}

#Definindo empréstimos
#"U003": ["M01"]
emprestimos = {
    "U001": [],
    "U002": [],
    "U003": [],
    "U004": []
}

# Definindo tipos de usuários
tipo_usuarios = {
    "U001": "ind",
    "U002": "ind",
    "U003": "ind",
    "U004": "coo"
}

#Definindo estações
estacao1 = ["B0001", "B0003", "B0005", "B0007"]
estacao2 = ["B0002", "B0004", "B0006", "B0008"]

#Definindo reservas
#"M01": ["U001"]
reservas = {
    "M01": ["U001", "U001"],
    "M02": ["U002", "U002"],
    "M03": [],
    "M04": []
}

#Funcão de Empréstimo
def emprestimo(dados_emprestimo):
    aux_teste_emprestimo1 = 0
    aux_teste_emprestimo2 = 0
    aux_teste_emprestimo3 = 0
    try:
        for a in bicicletas:
            if a == dados_emprestimo[1]:
                aux_teste_emprestimo1 = 1
        for b in usuarios:
            if b == dados_emprestimo[3]:
                aux_teste_emprestimo2 = 1
        if aux_teste_emprestimo1 == 0:
            print("Erro: Código de bicicleta inválido")
        if aux_teste_emprestimo2 == 0:
            print("Erro: Código de usuário inválido")
        if (dados_emprestimo[2] == "E01") or (dados_emprestimo[2] == "E02"):
            aux_teste_emprestimo3 = 1
        else:
            print("Erro: Código de estação inválido")
        if (aux_teste_emprestimo1 == 1) and (aux_teste_emprestimo2 == 1) and (aux_teste_emprestimo3 == 1):
            if dados_emprestimo[2] == "E01":
                try:
                    estacao1.index(dados_emprestimo[1])
                    if (tipo_usuarios[dados_emprestimo[3]] == "ind") and (len(emprestimos[dados_emprestimo[3]]) == 0) or (tipo_usuarios[dados_emprestimo[3]] == "coo") and (len(emprestimos[dados_emprestimo[3]]) <=2):
                        soma_reservas = 0
                        aux_reserva2 = 0
                        for c in reservas:
                            soma_reservas = soma_reservas + len(reservas[c])
                            aux_reserva1 = reservas[c]
                            for d in aux_reserva1:
                                if d == dados_emprestimo[3]:
                                    aux_reserva2 = aux_reserva2 + 1
                        if (soma_reservas < (len(estacao1) + len(estacao2))) or (aux_reserva2 == 1) or (aux_reserva2 == 2):
                            lista_aux_emprestimo = emprestimos[dados_emprestimo[3]]
                            aux_emprestimo1 = 0
                            if tipo_usuarios[dados_emprestimo[3]] == "coo":
                                if dados_emprestimo[1] == "B0001" or dados_emprestimo[1] == "B0002":
                                    for e in lista_aux_emprestimo:
                                        if e == "M01":
                                            aux_emprestimo1 = 1
                                elif dados_emprestimo[1] == "B0003" or dados_emprestimo[1] == "B0004":
                                    for e in lista_aux_emprestimo:
                                        if e == "M02":
                                            aux_emprestimo1 = 1
                                elif dados_emprestimo[1] == "B0005" or dados_emprestimo[1] == "B0006":
                                    for e in lista_aux_emprestimo:
                                        if e == "M03":
                                            aux_emprestimo1 = 1
                                else:
                                    for e in lista_aux_emprestimo:
                                        if e == "M04":
                                            aux_emprestimo1 = 1
                                if aux_emprestimo1 == 0:
                                    if dados_emprestimo[1] == "B0001" or dados_emprestimo[1] == "B0002":
                                        lista_aux_emprestimo.append("M01")
                                        aux_reserva3 = "M01"
                                    elif dados_emprestimo[1] == "B0003" or dados_emprestimo[1] == "B0004":
                                        lista_aux_emprestimo.append("M02")
                                        aux_reserva3 = "M02"
                                    elif dados_emprestimo[1] == "B0005" or dados_emprestimo[1] == "B0006":
                                        lista_aux_emprestimo.append("M03")
                                        aux_reserva3 = "M03"
                                    else:
                                        lista_aux_emprestimo.append("M04")
                                        aux_reserva3 = "M04"
                                    aux_emprestimo_reserva1 = 0
                                    aux_emprestimo_reserva2 = reservas[aux_reserva3]
                                    for f in aux_emprestimo_reserva2:
                                        if (len(aux_emprestimo_reserva2) < 2) or (f == dados_emprestimo[3]):
                                            aux_emprestimo_reserva1 = 1
                                    if aux_emprestimo_reserva1 == 1:
                                        emprestimos.update({dados_emprestimo[3]: lista_aux_emprestimo})
                                        estacao1.remove(dados_emprestimo[1])
                                        print("Empréstimo realizado com sucesso")
                                        aux_emprestimo_nome_usuario = usuarios[dados_emprestimo[3]]
                                        aux_emprestimo_nome_usuario = aux_emprestimo_nome_usuario[1]
                                        aux_emprestimo_modelo_bicicleta = modelos[aux_reserva3]
                                        aux_emprestimo_modelo_bicicleta = aux_emprestimo_modelo_bicicleta[0]
                                        print("Nome do usuário:", aux_emprestimo_nome_usuario)
                                        print("Modelo Bicicleta:", aux_emprestimo_modelo_bicicleta)
                                        if (aux_reserva2 == 1) or (aux_reserva2 ==2):
                                            aux_reserva4 = reservas[aux_reserva3]
                                            aux_reserva4.remove(dados_emprestimo[3])
                                            reservas.update({aux_reserva3: aux_reserva4})
                                    else:
                                        print("Erro: Bicicleta com reserva")
                                else:
                                    print("Erro: Empréstimo ativo de um mesmo modelo de bicicleta")
                            else:
                                if dados_emprestimo[1] == "B0001" or dados_emprestimo[1] == "B0002":
                                    lista_aux_emprestimo.append("M01")
                                    aux_reserva3 = "M01"
                                elif dados_emprestimo[1] == "B0003" or dados_emprestimo[1] == "B0004":
                                    lista_aux_emprestimo.append("M02")
                                    aux_reserva3 = "M02"
                                elif dados_emprestimo[1] == "B0005" or dados_emprestimo[1] == "B0006":
                                    lista_aux_emprestimo.append("M03")
                                    aux_reserva3 = "M03"
                                else:
                                    lista_aux_emprestimo.append("M04")
                                    aux_reserva3 = "M04"
                                emprestimos.update({dados_emprestimo[3]: lista_aux_emprestimo})
                                estacao1.remove(dados_emprestimo[1])
                                print("Empréstimo realizado com sucesso")
                                aux_emprestimo_nome_usuario = usuarios[dados_emprestimo[3]]
                                aux_emprestimo_nome_usuario = aux_emprestimo_nome_usuario[1]
                                aux_emprestimo_modelo_bicicleta = modelos[aux_reserva3]
                                aux_emprestimo_modelo_bicicleta = aux_emprestimo_modelo_bicicleta[0]
                                print("Nome do usuário:", aux_emprestimo_nome_usuario)
                                print("Modelo Bicicleta:", aux_emprestimo_modelo_bicicleta)
                                if (aux_reserva2 == 1):
                                    aux_reserva4 = reservas[aux_reserva3]
                                    aux_reserva4.remove(dados_emprestimo[3])
                                    reservas.update({aux_reserva3: aux_reserva4})
                        else:
                            print("Erro: Quantidade de reservas maior do que bicicletas disponíveis")
                    else:
                        print("Erro: Usuário devedor de bicicleta")
                except ValueError:
                    print("Erro: Bicicleta indisponível na estação")
            else:
                try:
                    estacao2.index(dados_emprestimo[1])
                    if (tipo_usuarios[dados_emprestimo[3]] == "ind") and (len(emprestimos[dados_emprestimo[3]]) == 0) or (tipo_usuarios[dados_emprestimo[3]] == "coo") and (len(emprestimos[dados_emprestimo[3]]) <=2):
                        soma_reservas = 0
                        aux_reserva2 = 0
                        for c in reservas:
                            soma_reservas = soma_reservas + len(reservas[c])
                            aux_reserva1 = reservas[c]
                            for d in aux_reserva1:
                                if d == dados_emprestimo[3]:
                                    aux_reserva2 = aux_reserva2 + 1
                        if (soma_reservas < (len(estacao1) + len(estacao2))) or (aux_reserva2 == 1) or (aux_reserva2 == 2):
                            lista_aux_emprestimo = emprestimos[dados_emprestimo[3]]
                            aux_emprestimo1 = 0
                            if tipo_usuarios[dados_emprestimo[3]] == "coo":
                                if dados_emprestimo[1] == "B0001" or dados_emprestimo[1] == "B0002":
                                    for e in lista_aux_emprestimo:
                                        if e == "M01":
                                            aux_emprestimo1 = 1
                                elif dados_emprestimo[1] == "B0003" or dados_emprestimo[1] == "B0004":
                                    for e in lista_aux_emprestimo:
                                        if e == "M02":
                                            aux_emprestimo1 = 1
                                elif dados_emprestimo[1] == "B0005" or dados_emprestimo[1] == "B0006":
                                    for e in lista_aux_emprestimo:
                                        if e == "M03":
                                            aux_emprestimo1 = 1
                                else:
                                    for e in lista_aux_emprestimo:
                                        if e == "M04":
                                            aux_emprestimo1 = 1
                                if aux_emprestimo1 == 0:
                                    if dados_emprestimo[1] == "B0001" or dados_emprestimo[1] == "B0002":
                                        lista_aux_emprestimo.append("M01")
                                        aux_reserva3 = "M01"
                                    elif dados_emprestimo[1] == "B0003" or dados_emprestimo[1] == "B0004":
                                        lista_aux_emprestimo.append("M02")
                                        aux_reserva3 = "M02"
                                    elif dados_emprestimo[1] == "B0005" or dados_emprestimo[1] == "B0006":
                                        lista_aux_emprestimo.append("M03")
                                        aux_reserva3 = "M03"
                                    else:
                                        lista_aux_emprestimo.append("M04")
                                        aux_reserva3 = "M04"
                                    emprestimos.update({dados_emprestimo[3]: lista_aux_emprestimo})
                                    estacao2.remove(dados_emprestimo[1])
                                    print("Empréstimo realizado com sucesso")
                                    aux_emprestimo_nome_usuario = usuarios[dados_emprestimo[3]]
                                    aux_emprestimo_nome_usuario = aux_emprestimo_nome_usuario[1]
                                    aux_emprestimo_modelo_bicicleta = modelos[aux_reserva3]
                                    aux_emprestimo_modelo_bicicleta = aux_emprestimo_modelo_bicicleta[0]
                                    print("Nome do usuário:", aux_emprestimo_nome_usuario)
                                    print("Modelo Bicicleta:", aux_emprestimo_modelo_bicicleta)
                                    if (aux_reserva2 == 1) or (aux_reserva2 == 2):
                                        aux_reserva4 = reservas[aux_reserva3]
                                        aux_reserva4.remove(dados_emprestimo[3])
                                        reservas.update({aux_reserva3: aux_reserva4})
                                else:
                                    print("Erro: Empréstimo ativo de um mesmo modelo de bicicleta")
                            else:
                                if dados_emprestimo[1] == "B0001" or dados_emprestimo[1] == "B0002":
                                    lista_aux_emprestimo.append("M01")
                                    aux_reserva3 = "M01"
                                elif dados_emprestimo[1] == "B0003" or dados_emprestimo[1] == "B0004":
                                    lista_aux_emprestimo.append("M02")
                                    aux_reserva3 = "M02"
                                elif dados_emprestimo[1] == "B0005" or dados_emprestimo[1] == "B0006":
                                    lista_aux_emprestimo.append("M03")
                                    aux_reserva3 = "M03"
                                else:
                                    lista_aux_emprestimo.append("M04")
                                    aux_reserva3 = "M04"
                                emprestimos.update({dados_emprestimo[3]: lista_aux_emprestimo})
                                estacao2.remove(dados_emprestimo[1])
                                print("Empréstimo realizado com sucesso")
                                aux_emprestimo_nome_usuario = usuarios[dados_emprestimo[3]]
                                aux_emprestimo_nome_usuario = aux_emprestimo_nome_usuario[1]
                                aux_emprestimo_modelo_bicicleta = modelos[aux_reserva3]
                                aux_emprestimo_modelo_bicicleta = aux_emprestimo_modelo_bicicleta[0]
                                print("Nome do usuário:", aux_emprestimo_nome_usuario)
                                print("Modelo Bicicleta:", aux_emprestimo_modelo_bicicleta)
                                if (aux_reserva2 == 1):
                                    aux_reserva4 = reservas[aux_reserva3]
                                    aux_reserva4.remove(dados_emprestimo[3])
                                    reservas.update({aux_reserva3: aux_reserva4})
                        else:
                            print("Erro: Quantidade de reservas maior do que bicicletas disponíveis")
                    else:
                        print("Erro: Usuário devedor de bicicleta")
                except ValueError:
                    print("Erro: Bicicleta indisponível na estação")
    except IndexError:
        print("Erro: Informações para empréstimo insuficientes")

#Início do programa
operacao = input("Operação: ")
while operacao != "fim":
    dados_operacao = operacao.split()
    if dados_operacao[0] == "cdu":
        cadastro(dados_operacao)
    elif dados_operacao[0] == "emb":
        emprestimo(dados_operacao)
    operacao = "fim"
    print(reservas)
    print(estacao1)
    print(estacao2)
    operacao = input("Operação: ")