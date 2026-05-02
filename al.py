import pandas as pd
from sqlalchemy import create_engine,text
import streamlit as st
import plotly.express as px
engine = create_engine('sqlite:///ai_jobs.db')
st.title("Análise de Vagas de Emprego em IA")
with engine.connect() as conn:
    # 1. Top 10 cargos mais frequentes
    df1 = pd.read_sql(text("SELECT job_title, COUNT(*) as total FROM ai_jobs GROUP BY job_title ORDER BY total DESC LIMIT 10"), conn)
    st.subheader("Top 10 Cargos Mais Frequentes")
    fig1 = px.bar(df1, x='job_title', y='total', title='Top 10 Cargos Mais Frequentes')
    st.plotly_chart(fig1)

    # 2. Salário médio por país
    df2 = pd.read_sql(text("SELECT country, ROUND(AVG(annual_salary_usd), 2) as salario_medio FROM ai_jobs GROUP BY country ORDER BY salario_medio DESC LIMIT 10"), conn)
    st.subheader("Salário Médio por País")
    fig2 = px.bar(df2, x='country', y='salario_medio', title='Salário Médio por País')
    st.plotly_chart(fig2)

    # 3. Quantidade de vagas remotas vs presencial
    df3 = pd.read_sql(text("SELECT remote_work, COUNT(*) as total FROM ai_jobs GROUP BY remote_work ORDER BY total DESC"), conn)
    st.subheader("Tipo de Trabalho (Remoto vs Presencial)")
    fig3 = px.pie(df3, names='remote_work', values='total', title='Tipo de Trabalho (Remoto vs Presencial)')
    st.plotly_chart(fig3)
    # 4. Salário médio por categoria
    df4 = pd.read_sql(text("SELECT job_category, ROUND(AVG(annual_salary_usd), 2) as salario_medio FROM ai_jobs GROUP BY job_category ORDER BY salario_medio DESC"), conn)
    st.subheader("📂 Salário Médio por Categoria")
    fig4 = px.bar(df4, x='salario_medio', y='job_category', orientation='h', color='salario_medio', color_continuous_scale='reds')
    st.plotly_chart(fig4)