
def cadastrar_produto(estoque):

    produto = obter_nome_produto()

    if produto in estoque:
        print("Produto já cadastrado. Digite outro produto. ")

        return 

    preco = obter_preco()
    quantidade = obter_quantidade()

    estoque[produto] = {    
        "preco": preco,
        "quantidade": quantidade
    }
    print("Produto cadastrado com sucesso!")

def obter_nome_produto():
    while True:
        nome_produto = input("Digite o nome do produto: ").strip()

        if nome_produto == "":
            print("Nome do produto inválido. Digite um nome válido. ")

            continue

        return nome_produto

def obter_preco():
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))

            if preco < 0:
                print("Preço inválido. Digite um valor maior ou igual a zero. ")
                continue

            return preco

        except ValueError:
            print("Erro: Por favor, digite um número válido para o preço. ")

def obter_quantidade():           
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))

            if quantidade < 0:
                print("Quantidade inválida. Digite um valor maior ou igual a zero. ")
                continue
            return quantidade
           
            
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido para a quantidade. ")


def listar_produtos(estoque):

    if not estoque:
        print("Nenhum produto no estoque.")
    else:
        for produto, dados in estoque.items():
            print("-------------------------")
            print(f"Produto: {produto}")
            print(f"Preço: {dados['preco']}")
            print(f"Quantidade: {dados['quantidade']}")
            print("------------------------")


def buscar_produto(estoque):
    nome_produto = input("Digite o nome do produto que deseja buscar: ")

    if nome_produto in estoque:
        dados = estoque[nome_produto]
        print("-------------------------")
        print(f"Produto: {nome_produto}")
        print(f"Preço: {dados['preco']}")
        print(f"Quantidade: {dados['quantidade']}")
        print("------------------------")
    else:
        print("Produto não encontrado.")

def alterar_estoque(estoque):
        
    nome_produto = input("Digite o nome do produto que deseja alterar no estoque: ")

    if nome_produto in estoque:
        print(f"Produto encontrado: {nome_produto}")

        nova_quantidade = obter_quantidade()

        estoque[nome_produto]["quantidade"] = nova_quantidade

        print("Quantidade do produto alterada com sucesso! ")
    else:
        print("Produto não encontrado. ")   


def remover_produto(estoque):
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    if nome_produto in estoque:
        del estoque[nome_produto]
        print("Produto removido com sucesso! ")
    else:
        print("Produto não encontrado. ")
