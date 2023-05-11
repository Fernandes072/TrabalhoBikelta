# Definindo Usuários
usuarios = {
    "U003": ["coo", "Associação Itabaiana de Guias de Turismo", "N"]
}

# Definindo tipos de usuários
tipo_usuarios = {

}

#Definindo empréstimos
emprestimos = {

}

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

#Início do programa
operacao = input("Operação: ")
while operacao != "fim":
    dados_operacao = operacao.split()
    if dados_operacao[0] == "cdu":
        cadastro(dados_operacao)
    operacao = "fim"
print(usuarios)
print(tipo_usuarios)