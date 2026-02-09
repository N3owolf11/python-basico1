# Mini sistema em Python: Cadastro de Contatos (CLI)
# Arquivo: cadastro_contatos.py

contatos = []

def mostrar_menu():
    print("\n=== MENU ===")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Remover contato")
    print("4 - Sair")

def adicionar_contato():
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()

    if nome == "" or telefone == "":
        print(" Nome e telefone não podem ficar vazios.")
        return

    contatos.append({"nome": nome, "telefone": telefone})
    print(" Contato adicionado com sucesso!")

def listar_contatos():
    if len(contatos) == 0:
        print(" Nenhum contato cadastrado.")
        return

    print("\n--- Contatos ---")
    for i, c in enumerate(contatos, start=1):
        print(f"{i}. {c['nome']} - {c['telefone']}")

def remover_contato():
    listar_contatos()
    if len(contatos) == 0:
        return

    try:
        indice = int(input("Digite o número do contato para remover: "))
        if indice < 1 or indice > len(contatos):
            print(" Número inválido.")
            return
        removido = contatos.pop(indice - 1)
        print(f" Contato removido: {removido['nome']}")
    except ValueError:
        print(" Digite um número válido.")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print(" Saindo... até mais!")
        break
    else:
        print(" Opção inválida. Tente novamente.")
