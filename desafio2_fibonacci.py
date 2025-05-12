def desafio2(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b

    if numero == b or numero == 0:
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))
    desafio2(numero)
3