def novo_orçamento():
    numero_orcamento = 1

    print("\n--- NOVO ORÇAMENTO ---")
    print(f"Orçamento N° {numero_orcamento}")
    
    cliente = input("Cliente: ")
    endereço = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    contato = input("Contato: ")
    cep = input("CEP:")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    cnpj = input("CNPJ: ")
    inscrição = input("IE: ")

def main():
    while True:

        print("=" * 40)
        print("           DATAVISION")
        print("   Sistema de Orçamentos de Dados")
        print("=" * 40)

        print("\n1 - Novo Orçamento")
        print("2 - Consultar Orçamentos")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            novo_orçamento()
        elif opcao == "2":
            print("Consultar Orçamento Selecionado")
        elif opcao == "3":
            print("Encerrando")
            break
        else:
            print("Opção Inválida!")
    
if __name__ == "__main__":
    main()