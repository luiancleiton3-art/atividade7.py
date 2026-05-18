import pandas as pd

# 1. Carrega os dados do arquivo CSV
dados = pd.read_csv("academia.csv")

# ==========================================
# ATIVIDADE 7 — Filtragem de Dados
# ==========================================
print("--- ATIVIDADE 7 ---")

# Aplica o filtro para alunos com mais de 5 horas de treino
alunos_focados = dados[dados["Horas_Treino"] > 5]

# Exibe o resultado filtrado na tela
print("Alunos que treinam mais de 5 horas por semana:")
print(alunos_focados)
print("\n" + "=" * 50 + "\n")
