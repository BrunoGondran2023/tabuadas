def calcular_tabuada(numero):
    """
    Função para calcular e imprimir a tabuada de um número.
    """
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero:2d} X {i:2d} = {resultado:3d}")
    print()


def main():
    """
    Função principal do programa.
    """
    for num in range(1, 11):
        calcular_tabuada(num)


if __name__ == "__main__":
    main()
