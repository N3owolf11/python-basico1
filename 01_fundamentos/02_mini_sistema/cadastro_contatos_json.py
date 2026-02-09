# Mini sistema em Python: Cadastro de Contatos (CLI) com JSON
# Arquivo: cadastro_contatos_json.py

import json
import os

ARQUIVO = "contatos.json"

def carregar_contatos():
    """Carrega contatos do arquivo JSON, se existir."""
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)

        # Garante que seja uma lista de dicionários válidos
        if isinstance(dados, list):
            contatos_validos = []
            for item in dados:
                if isinstance(item, dict) and "nome" in item and "telefone" in item:
                    contatos_validos.append(item)
            return contatos_validos

        return []
    except (json.JSONDecodeError, OSError):
        # Arquivo corrompido ou erro de leitura
        return []

def salvar_contatos(contatos):
    """Salva a lista de contatos no arquivo JSON."""
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(contatos, f, ensure_ascii=False, indent=2)
    except OSError:
        print(" Erro ao salvar o arquivo. Verifique permissões.")

def mostrar_menu():
    print("\n=== MENU ===")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Remover contato")
    print("4 - Buscar contato")
    print("5 - Sair")

def adicionar_contato(contatos):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()

    if not nome or not telefone:
        print(" Nome e telefone não podem ficar vazios.")
        return

    contatos.append({"nome": nome, "telefone": telefone})
    salvar_contatos(contatos)
    print(" Contato adicionado e salvo!")

def listar_contatos(contatos):
    if not contatos:
        print(" Nenhum contato cadastrado.")
        return

    print("\n--- Contatos ---")
    for i, c in enumerate(contatos, start=1):
        print(f"{i}. {c['nome']} - {c['telefone']}")

def remover_contato(contatos):
    listar_contatos(contatos)
    if not contatos:
        return

    try:
        indice = int(input("Digite o número do contato para remover: "))
        if indice < 1 or indice > len(contatos):
            print(" Número inválido.")
            return

        removido = contatos.pop(indice - 1)
        salvar_contatos(contatos)
        print(f" Contato removido e alterações salvas: {removido['nome']}")
    except ValueError:
        print(" Digite um número válido.")

def buscar_contato(contatos):
    termo = input("Buscar por nome ou telefone: ").strip().lower()
    if not termo:
        print(" Digite algo para buscar.")
        return

    encontrados = []
    for c in contatos:
        nome = c.get("nome", "").lower()
        telefone = c.get("telefone", "").lower()
        if termo in nome or termo in telefone:
            encontrados.append(c)

    if not encontrados:
        print("🔎 Nenhum contato encontrado.")
        return

    print("\n--- Resultados ---")
    for i, c in enumerate(encontrados, start=1):
        print(f"{i}. {c['nome']} - {c['telefone']}")

def main():
    contatos = carregar_contatos()
    print(" Sistema iniciado. Contatos carregados:", len(contatos))

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            remover_contato(contatos)
        elif opcao == "4":
            buscar_contato(contatos)
        elif opcao == "5":
            print(" Saindo... até mais!")
            break
        else:
            print(" Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
