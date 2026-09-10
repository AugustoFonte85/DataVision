def novo_orçamento():
    numero_orcamento = 1

    print("\n--- NOVO ORÇAMENTO ---")
    print(f"Orçamento N° {numero_orcamento}")

    print("\nDADOS DO CLIENTE")

    cliente = input("Cliente: ")
    endereço = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    contato = input("Contato: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    cnpj = input("CNPJ: ")
    inscrição = input("IE: ")

    print("\nDADOS DO ORÇAMENTO")

    servico = input("\nServiço: ")
    descricao = input("Descrição: ")
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(input("Valor Unitário: "))

    total = quantidade * valor_unitario
    desconto = float(input("Desconto (%): "))

    valor_desconto = total * (desconto /100)
    total_final = total - valor_desconto

    print(f"Desconto: R$ {valor_desconto:.2f}")

    print(f"Total Final: R$ {total_final:.2f}") 

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