from datetime import datetime

def novo_orçamento():
    numero_orcamento = 1

    print("\n--- NOVO ORÇAMENTO ---")
    print(f"Orçamento N° {numero_orcamento}")

    print("\nDADOS DO CLIENTE")

    dados_cliente = {

        "cliente" : input("Cliente: "),
        "endereco" : input("Endereço: "),
        "telefone" : input("Telefone: "),
        "email" : input("E-mail: "),
        "contato" : input("Contato: "),
        "cep" : input("CEP: "),
        "cidade" : input("Cidade: "),
        "bairro" : input("Bairro: "),
        "cnpj" : input("CNPJ: "),
        "ie" : input("IE: ")
    }

    print("\nDADOS DO ORÇAMENTO")

    dados_orcamento = {

        "servico": input("Serviço: "),
        "descricao": input("Descrição: "),
        "quantidade": int(input("Quantidade: ")),
        "valor_unitario": float(input("Valor Unitário: ")),
        "desconto": float(input("Desconto (%): "))
    }

    total = dados_orcamento["quantidade"] * dados_orcamento["valor_unitario"]

    valor_desconto = total * (dados_orcamento["desconto"] / 100)
    total_final = total - valor_desconto 


    print("\n" + "=" * 40)
    print("        RESUMO DO ORÇAMENTO")
    print("=" * 40)

    print(f"Serviço: {dados_orcamento['servico']}") 
    print(f"Descrição: {dados_orcamento['descricao']}")
    print(f"Quantidade: {dados_orcamento['quantidade']}")
    print(f"Valor Unitário: R$ {dados_orcamento['valor_unitario']:.2f}")

    print("-" * 40)

    print(f"Subtotal: R$ {total:.2f}")
    print(f"Desconto ({dados_orcamento['desconto']}%): R$ {valor_desconto:.2f}")
    print(f"TOTAL FINAL: R$ {total_final:.2f}")

    print("-" * 40)

    print("\nCONDIÇÕES DO ORÇAMENTO")

    prazo = input("Prazo de Execução: ")
    validade = input("Validade da Proposta: ")
    forma_pagamento = input("Forma de Pagamento: ")

    print("\nFINALIZAÇÃO")

    data_emissao = datetime.now().strftime("%d/%m/%Y")
    assinatura = input("Assinatura: ")

    print(f"Data da Emissão: {data_emissao}")

    
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