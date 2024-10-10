faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estado.values())

percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estado.items()}

print(f"Faturamento total: R${faturamento_total:.2f}")
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
