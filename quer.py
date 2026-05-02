import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///ai_jobs.db')

with engine.connect() as conn:

    # 1. Top 10 cargos mais frequentes
    print("=== TOP 10 CARGOS ===")
    df1 = pd.read_sql(text("SELECT job_title, COUNT(*) as total FROM ai_jobs GROUP BY job_title ORDER BY total DESC LIMIT 10"), conn)
    print(df1)

    # 2. Salário médio por país
    print("\n=== SALÁRIO MÉDIO POR PAÍS ===")
    df2 = pd.read_sql(text("SELECT country, ROUND(AVG(annual_salary_usd), 2) as salario_medio FROM ai_jobs GROUP BY country ORDER BY salario_medio DESC LIMIT 10"), conn)
    print(df2)

    # 3. Quantidade de vagas remotas vs presencial
    print("\n=== TIPO DE TRABALHO ===")
    df3 = pd.read_sql(text("SELECT remote_work, COUNT(*) as total FROM ai_jobs GROUP BY remote_work ORDER BY total DESC"), conn)
    print(df3)