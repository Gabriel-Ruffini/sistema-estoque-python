from estoque import (
    cadastrar_produto,
    listar_produtos,
    buscar_produto,
    alterar_estoque,
    remover_produto
)

estoque = {}

opcao = 0

while opcao != 6:
    print("========== SISTEMA DE ESTOQUE ==========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produtos")
    print("4 - Alterar estoque")
    print("5 - Remover produto")
    print("6 - Sair")

    try:
        opcao = int(input("Digite a opção desejada: "))

    except ValueError:
        print("Erro: Por favor, digite um número válido para a opção. ")

    if opcao == 6:
        print("Programa encerrado.")

    elif opcao == 1:
        cadastrar_produto(estoque)

    elif opcao == 2:
        listar_produtos(estoque)

    elif opcao == 3:
        buscar_produto(estoque)

    elif opcao == 4:
        alterar_estoque(estoque)
       
    elif opcao == 5:
        remover_produto(estoque)
