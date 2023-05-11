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
    "U001": ["ind", "Maria Bonita"],
    "U003": ["coo", "Associação Itabaiana de Guias de Turismo"]
}

#Definindo reservas
reservas = {
    "M01": [],
    "M02": [],
    "M03": [],
    "M04": []
}

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
                print("Reserva realizado com sucesso")
                print("Nome do usuário:", aux_reservas_nome_usuario)
                print("Modelo Bicicleta:", aux_reservas_modelo_bicicleta)
            else:
                print("Erro: Limite de reservas excedido")
    except IndexError:
        print("Erro: Informações para reserva insuficientes")

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
    operacao = "fim"

print(reservas)