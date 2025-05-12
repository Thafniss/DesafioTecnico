def desafio4():
    estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total = sum(estados.values())

    for estado, valor in estados.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    desafio4()
