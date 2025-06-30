import requests

def menu():
    print("escolha a opção:")
    print("1 - listar veículos")
    print("2 - criar veículos")
    print("3 - deletar veículos")
    print("4 - Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"

    while True:
        opcao = menu()

        # Listar todos os livros
        if opcao == "1":
            r = requests.get(f"{url}/veiculos")
            if r.status_code == 200:
                print("\ lista de veículos:")
                print(r.json())

        elif opcao == "2":
            # Cadastrar um livro
            nome = input("Digite o nome do veículo: ")
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            placa = int(input("Digite a placa do veículo: "))

            veiculo = {
                "nome": nome,
                "marca": marca,
                "modelo": modelo,
                "placa": placa
            }
            r = requests.post(f"{url}/veiculos", json=veiculo)
            if r.status_code == 200 or r.status_code == 201:
                print("\veículo cadastrado com sucesso!")
                print(r.json())

        elif opcao == "3":
            # Deletar um veiculo
            nome = input("Digite o nome do veiculo que deseja deletar: ")
            r = requests.delete(f"{url}/veiculos/{nome}")
            if r.status_code == 200:
                print("\n veiculo deletado com sucesso!")
                print(r.json())
            else:
                print("veiculo não encontrado para deletar!")

        elif opcao == "4":
            # Sair
            print("sair")
            break