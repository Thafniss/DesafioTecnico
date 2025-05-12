import json
import xml.etree.ElementTree as ET

def processar_dados(dados):
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

def ler_json(caminho):
    with open(caminho, 'r') as arquivo:
        bruto = json.load(arquivo)
        return [{'dia': item['dia'], 'valor': item['valor']} for item in bruto]

def ler_xml(caminho):
    tree = ET.parse(caminho)
    root = tree.getroot()
    return [{'dia': int(row.find('dia').text), 'valor': float(row.find('valor').text)} for row in root.findall('row')]

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
        dados = ler_xml("dados.xml")
        print("\n📊 Resultados para XML:")
        processar_dados(dados)
    else:
        print("Opção inválida.")
