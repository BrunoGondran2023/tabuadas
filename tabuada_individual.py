def obter_numero():
    """
    Função para obter um número do usuário.
    """
    while True:
        try:
            num = int(input("Digite o número: "))
            return num
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def calcular_tabuada(numero):
    """
    Função para calcular e imprimir a tabuada de um número.
    """
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


def main():
    """
    Função principal do programa.
    """
    numero = obter_numero()
    calcular_tabuada(numero)


if __name__ == "__main__":
    main()
