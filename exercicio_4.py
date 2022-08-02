# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

fat_SP = 67836.43
fat_RJ = 36678.66
fat_MG = 29229.88
fat_ES = 27165.48
fat_Outros = 19849.53

total = fat_SP + fat_RJ + fat_MG + fat_ES + fat_Outros

def porcentagem(fat_estado):
    return round(fat_estado/total * 100, 2)

print("""
SP - {}%,
RJ - {}%,
MG - {}%,
ES - {}%,
Outros - {}%,
""".format(
porcentagem(fat_SP),
porcentagem(fat_RJ),
porcentagem(fat_MG),
porcentagem(fat_ES),
porcentagem(fat_Outros)
))