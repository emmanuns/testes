import json

dados_faturamento = '''
{
    "faturamento": {
        "1": 1500.0,
        "2": 2000.0,
        "3": 1800.0,
        "4": 2200.0,
        "5": 1700.0,
        "6": 0.0,
        "7": 0.0,
        "8": 2500.0,
        "9": 2100.0,
        "10": 1900.0,
        "11": 2300.0,
        "12": 2000.0,
        "13": 1600.0,
        "14": 2400.0,
        "15": 2200.0,
        "16": 2100.0,
        "17": 2500.0,
        "18": 3000.0,
        "19": 2600.0,
        "20": 2800.0,
        "21": 2900.0,
        "22": 3000.0,
        "23": 3200.0,
        "24": 3400.0,
        "25": 3300.0,
        "26": 3100.0,
        "27": 2800.0,
        "28": 2700.0,
        "29": 2500.0,
        "30": 2300.0,
        "31": 2200.0
    }
}
'''

dados = json.loads(dados_faturamento)
faturamento_diario = list(dados['faturamento'].values())

faturamento_filtrado = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_filtrado) if faturamento_filtrado else 0
maior_faturamento = max(faturamento_filtrado) if faturamento_filtrado else 0

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado) if faturamento_filtrado else 0

dias_superior_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

print(f"O menor valor de faturamento: {menor_faturamento:.2f}")
print(f"O maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_superior_media}")
