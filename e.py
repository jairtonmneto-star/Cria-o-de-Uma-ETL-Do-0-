import pandas as pd
from sqlalchemy import create_engine

tab = pd.read_csv('ai_jobs_market_2025_2026.csv')

# Exploração
print(tab.head())
tab.info()

# Limpeza
tab = tab.drop_duplicates()
tab['country'] = tab['country'].str.strip()
tab['remote_work'] = tab['remote_work'].str.strip()
tab['job_category'] = tab['job_category'].str.strip()

# ⚠️ NÃO converte required_skills para lista aqui
# Mantém como texto para salvar no banco

# Exportar para SQLite
engine = create_engine('sqlite:///ai_jobs.db')
tab.to_sql('ai_jobs', engine, if_exists='replace', index=False)
print("Dados exportados com sucesso!")