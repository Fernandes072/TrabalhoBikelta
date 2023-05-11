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

#Definindo Usuários
usuarios = {

}

#Definindo empréstimos
emprestimos = {

}

# Definindo tipos de usuários
tipo_usuarios = {

}

#Definindo reservas
reservas = {
    "M01": [],
    "M02": [],
    "M03": [],
    "M04": []
}

#Definindo estações
estacao1 = ["B0001", "B0003", "B0005", "B0007"]
estacao2 = ["B0002", "B0004", "B0006", "B0008"]

#Funcão de Cadastramento
def cadastro(dados_cad):
    try:
        aux_teste_existe = 0
        for i in usuarios:
            if i == dados_cad[1]:
                aux_teste_existe = 1
        if aux_teste_existe == 0:
            if (dados_cad[2] == "ind") or (dados_cad[2] == "coo"):
                aux_dados_cadastro = ""
                aux_codigo_usuario = dados_cad[1]
                dados_usuario = []
                for i in range(2, len(dados_cad)):
                    if i == 2:
                        dados_usuario.append(dados_cad[2])
                    else:
                        aux_dados_cadastro = aux_dados_cadastro + dados_cad[i]
                        if i <= (len(dados_cad)-2):
                            aux_dados_cadastro = aux_dados_cadastro + " "
                dados_usuario.append(aux_dados_cadastro)
                tipo_usuarios[dados_cad[1]] = dados_cad[2]
                usuarios[aux_codigo_usuario] = dados_usuario
                emprestimos[dados_cad[1]] = []
                print("Cadastro realizado com sucesso")
            else:
                print("Erro: Tipo de usuário inválido")
        else:
            print("Erro: Código de usuário já cadastrado")
    except IndexError:
        print("Erro: Informações para cadastro insuficientes")

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
                                    if len(aux_emprestimo_reserva2) == 0:
                                        aux_emprestimo_reserva1 = 1
                                    else:
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
                                        if (aux_reserva2 == 1) or (aux_reserva2 == 2):
                                            aux_reserva4 = reservas[aux_reserva3]
                                            try:
                                                aux_reserva4.index(dados_emprestimo[3])
                                                aux_teste_emprestimo4 = 1
                                            except ValueError:
                                                aux_teste_emprestimo4 = 0
                                            if aux_teste_emprestimo4 == 1:
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
                                aux_emprestimo_reserva1 = 0
                                aux_emprestimo_reserva2 = reservas[aux_reserva3]
                                if len(aux_emprestimo_reserva2) == 0:
                                    aux_emprestimo_reserva1 = 1
                                else:
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
                                    if (aux_reserva2 == 1) or (aux_reserva2 == 2):
                                        aux_reserva4 = reservas[aux_reserva3]
                                        try:
                                            aux_reserva4.index(dados_emprestimo[3])
                                            aux_teste_emprestimo4 = 1
                                        except ValueError:
                                            aux_teste_emprestimo4 = 0
                                        if aux_teste_emprestimo4 == 1:
                                            aux_reserva4.remove(dados_emprestimo[3])
                                            reservas.update({aux_reserva3: aux_reserva4})
                                else:
                                    print("Erro: Bicicleta com reserva")
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
                                    aux_emprestimo_reserva1 = 0
                                    aux_emprestimo_reserva2 = reservas[aux_reserva3]
                                    if len(aux_emprestimo_reserva2) == 0:
                                        aux_emprestimo_reserva1 = 1
                                    else:
                                        for f in aux_emprestimo_reserva2:
                                            if (len(aux_emprestimo_reserva2) < 2) or (f == dados_emprestimo[3]):
                                                aux_emprestimo_reserva1 = 1
                                    if aux_emprestimo_reserva1 == 1:
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
                                            try:
                                                aux_reserva4.index(dados_emprestimo[3])
                                                aux_teste_emprestimo4 = 1
                                            except ValueError:
                                                aux_teste_emprestimo4 = 0
                                            if aux_teste_emprestimo4 == 1:
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
                                aux_emprestimo_reserva1 = 0
                                aux_emprestimo_reserva2 = reservas[aux_reserva3]
                                if len(aux_emprestimo_reserva2) == 0:
                                    aux_emprestimo_reserva1 = 1
                                else:
                                    for f in aux_emprestimo_reserva2:
                                        if (len(aux_emprestimo_reserva2) < 2) or (f == dados_emprestimo[3]):
                                            aux_emprestimo_reserva1 = 1
                                if aux_emprestimo_reserva1 == 1:
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
                                        try:
                                            aux_reserva4.index(dados_emprestimo[3])
                                            aux_teste_emprestimo4 = 1
                                        except ValueError:
                                            aux_teste_emprestimo4 = 0
                                        if aux_teste_emprestimo4 == 1:
                                            aux_reserva4.remove(dados_emprestimo[3])
                                            reservas.update({aux_reserva3: aux_reserva4})
                                else:
                                    print("Erro: Bicicleta com reserva")
                        else:
                            print("Erro: Quantidade de reservas maior do que bicicletas disponíveis")
                    else:
                        print("Erro: Usuário devedor de bicicleta")
                except ValueError:
                    print("Erro: Bicicleta indisponível na estação")
    except IndexError:
        print("Erro: Informações para empréstimo insuficientes")

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
                aux_devolucao4 = 0
                for d in estacao1:
                    if d == dados_devolucao[1]:
                        aux_devolucao4 = 1
                for e in estacao2:
                    if e == dados_devolucao[1]:
                        aux_devolucao4 = 1
                if aux_devolucao4 == 0:
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
            else:
                print("Erro: Não há empréstimo da bicileta")
    except IndexError:
        print("Erro: Informações para devolução insuficientes")

#Funcão de Reserva
def reserva(dados_reserva):
    aux_teste_reserva1 = 0
    aux_teste_reserva2 = 0
    try:
        for a in reservas:
            if a == dados_reserva[1]:
                aux_teste_reserva1 = 1
        for b in usuarios:
            if b == dados_reserva[2]:
                aux_teste_reserva2 = 1
        if aux_teste_reserva1 == 0:
            print("Erro: Modelo de bicicleta inválido")
        if aux_teste_reserva2 == 0:
            print("Erro: Código de usuário inválido")
        if (aux_teste_reserva1 == 1) and (aux_teste_reserva2 == 1):
            aux_reserva1 = 0
            for c in reservas:
                aux_reserva2 = reservas[c]
                for d in aux_reserva2:
                    if d == dados_reserva[2]:
                        aux_reserva1 = aux_reserva1 + 1
            if aux_reserva1 < 2:
                aux_reserva3 = reservas[dados_reserva[1]]
                aux_reserva3.append(dados_reserva[2])
                reservas.update({dados_reserva[1]: aux_reserva3})
                aux_reservas_nome_usuario = usuarios[dados_reserva[2]]
                aux_reservas_nome_usuario = aux_reservas_nome_usuario[1]
                aux_reservas_modelo_bicicleta = modelos[dados_reserva[1]]
                aux_reservas_modelo_bicicleta = aux_reservas_modelo_bicicleta[0]
                print("Reserva realizada com sucesso")
                print("Nome do usuário:", aux_reservas_nome_usuario)
                print("Modelo Bicicleta:", aux_reservas_modelo_bicicleta)
            else:
                print("Erro: Limite de reservas excedido")
    except IndexError:
        print("Erro: Informações para reserva insuficientes")

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
    try:
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
        else:
            print("Operação inválida")
    except IndexError:
        print("Erro: Informações insuficientes para operação")
    operacao = input("Operação: ")