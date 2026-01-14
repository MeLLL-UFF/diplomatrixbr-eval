import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from datetime import datetime

from utils import get_mean

def main(num_runs, eval_path, human_path, report_filename):
    root_path = os.getcwd()
    output_path = os.path.join(root_path, "prompt_testing", "reports", "t")
    os.makedirs(output_path)

    # Carregando dados
    df_eval = get_mean(eval_path, num_runs)

    df_human = pd.read_csv(human_path)
    df_human.drop(columns=["versao", "prompt", "temp", "faixa"], inplace=True)

    # Gerando gráficos
    plt.style.use('seaborn-v0_8') # Estilo similar ao notebook
    
    # Gráfico 1: Distribuição de Notas
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Lógica de plotagem baseada no snippet do notebook
    sns.lineplot(data=df_eval, x="redacao", y="nota_final", hue="temp", marker="o", ax=axes[0])
    axes[0].set_title("Análise de Notas Finais (Sabiá)")
    
    sns.lineplot(data=df_human, x="redacao", y="nota_final", marker="o", ax=axes[1], color='green')
    axes[1].set_title("Notas Humanas (Referência)")
    
    img_notas_path = os.path.join(output_path, "distribuicao_notas.png")
    plt.savefig(img_notas_path)
    plt.close()

    # Gráfico 2: Análise de Erros
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.lineplot(data=df_eval, x="redacao", y="num_errors", hue="temp", marker="o", ax=axes[0])
    axes[0].set_title("Média de Erros Gerados por Redação")
    
    sns.lineplot(data=df_human, x="redacao", y="num_errors", marker="o", ax=axes[1], color='red')
    axes[1].set_title("Erros Humanos (Referência)")
    
    img_erros_path = os.path.join(output_path, "analise_erros.png")
    plt.savefig(img_erros_path)
    plt.close()

    # Gerando resumo em markdown
    md_content = f"""# Relatório de Avaliação Sabiá 3.1
Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

## 1. Visão Geral dos Dados (Amostra Sabiá)
{df_eval.head(10).to_markdown()}

## 2. Comparativo de Notas
Nesta seção comparamos as notas atribuídas pelo modelo Sabiá em diferentes temperaturas versus a correção humana.

![Distribuição de Notas](distribuicao_notas.png)

## 3. Análise de Erros Gramaticais e Ortográficos
Comparação da sensibilidade do modelo na detecção/geração de erros em relação ao padrão humano.

![Análise de Erros](analise_erros.png)

## 4. Estatísticas Descritivas
### Sabiá (Geral)
{df_eval.describe().to_markdown()}

### Humano
{df_human.describe().to_markdown()}
"""

    # Salva apenas o arquivo .md
    report_path = os.path.join(output_path, report_filename)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Relatório '{report_filename}' gerado com sucesso!")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_runs", type=int, required=True)
    parser.add_argument("--eval_path", required=True)
    parser.add_argument("--human_path", required=True)
    parser.add_argument("--report_filename", required=True)
    args = parser.parse_args()
    main(args.num_runs, args.eval_path, args.human_path, args.report_filename)