import json
import xml.etree.ElementTree as ET

# ----- Função para processar os dados (JSON ou XML) -----
def processar_dados(dados):
    # Filtra valores maiores que zero
    valores = [item['valor'] for item in dados if item['valor'] > 0]

    if not valores:
        print("Nenhum valor válido encontrado.")
        return

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    acima_da_media = len([v for v in valores if v > media])

    print("Menor faturamento:", round(menor, 2))
    print("Maior faturamento:", round(maior, 2))
    print("Média:", round(media, 2))
    print("Dias com faturamento acima da média:", acima_da_media)

# ----- Lê dados do JSON -----
def ler_json(caminho):
    with open(caminho, 'r') as arquivo:
        bruto = json.load(arquivo)
        return [{'dia': item['dia'], 'valor': item['valor']} for item in bruto]

# ----- Lê dados do XML -----
def ler_xml(caminho):
    tree = ET.parse(caminho)
    root = tree.getroot()
    return [{'dia': int(row.find('dia').text), 'valor': float(row.find('valor').text)} for row in root.findall('row')]

# ----- Menu para escolher qual arquivo processar -----
if __name__ == "__main__":
    print("Escolha o arquivo para processar:")
    print("1 - dados.json")
    print("2 - dados.xml")
    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        dados = ler_json("dados.json")
        print("\n📊 Resultados para JSON:")
        processar_dados(dados)
    elif opcao == "2":
        dados = ler_xml("dados (2).xml")
        print("\n📊 Resultados para XML:")
        processar_dados(dados)
    else:
        print("Opção inválida.")
import os

def menu():
    print("\n=== DESAFIO TÉCNICO ===")
    print("Escolha o desafio que deseja executar:")
    print("1 - Soma com loop (desafio 1)")
    print("2 - Verificar número na sequência de Fibonacci (desafio 2)")
    print("3 - Faturamento mensal (desafio 3)")
    print("4 - Percentual por estado (desafio 4)")
    print("5 - Inverter string (desafio 5)")
    print("0 - Sair")

def executar_opcao(opcao):
    if opcao == "1":
        os.system("python desafio1_soma.py")
    elif opcao == "2":
        os.system("python desafio2_fibonacci.py")
    elif opcao == "3":
        os.system("python desafio3_faturamento.py")
    elif opcao == "4":
        os.system("python desafio4_percentual.py")
    elif opcao == "5":
        os.system("python desafio5_inverter.py")
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    while True:
        menu()
        escolha = input("Digite a opção desejada: ")
        if escolha == "0":
            break
        executar_opcao(escolha)
