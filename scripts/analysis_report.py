import os
import numpy as np
import pandas as pd
import argparse
from datetime import datetime

import yaml

from plot import plot_distribuicao_notas, plot_eval_human_num_errors, plot_eval_human_scores, plot_val_error
from utils import get_mean

def main(num_runs, eval_path, human_path, model, model_version):
    root_path = os.getcwd()
    output_path = os.path.join(root_path, "prompt_testing", "reports", f"{model}_v{model_version}_{num_runs}_runs")
    os.makedirs(output_path, exist_ok=True)

    # Carregando dados
    df_eval = get_mean(eval_path, num_runs)
    df_human = pd.read_csv(human_path)
    df_human.drop(columns=["versao", "prompt", "temp", "faixa"], inplace=True)

    # Calculando métricas adicionais
    df_merged = df_eval.merge(
    df_human[["redacao", "nota_final"]].rename(columns={"nota_final": "nota_humana"}), on="redacao")
    df_merged["val_error"] =  abs(df_merged["nota_humana"] - df_merged["nota_final"])

    areas = {}
    for (prompt, temp), group in df_merged.groupby(["prompt", "temp"]):  
        area = np.trapezoid(group["val_error"], group["redacao"])
        areas[(prompt, temp)] = prompt, temp, area.round(4)
    df_area_sob_grafico = pd.DataFrame.from_dict(areas, orient='index', columns=['prompt', 'temp', 'area_val_error']).reset_index(drop=True)

    # Gerando gráficos
    # 1. Distribuição de Notas
    with open(os.path.join(root_path, "prompt_testing", "prompts.yaml"), 'r', encoding='utf-8') as file:
        prompts_yaml = yaml.safe_load(file)
        prompts = prompts_yaml['prompts']

    plot_distribuicao_notas(df_eval, df_human, prompts, output_path)

    # 2. Comparação entre Notas Geradas e Humanas
    plot_eval_human_scores(df_merged, output_path)

    # 3. Erro de Validação
    plot_val_error(df_merged, output_path)

    # 4. Comparação entre Números de Erros Gerados e Humanos
    plot_eval_human_num_errors(df_merged, df_human, output_path)

    # Gerando resumo em markdown
    md_content = f"""# Relatório de Avaliação: {model} v{model_version} - {num_runs} execuções
**Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo {model} em diferentes prompts/temperaturas versus a correção humana.

![Distribuição de Notas](distribuicao_notas.png)

## 2. Comparação de Notas Geradas e Humanas
Nesta seção, apresentamos a comparação entre as notas finais geradas pelo modelo e as notas dadas por avaliadores humanos.

![Comparação Notas](comparacao_notas.png)

## 3. Análise de Erro de Validação

<table>
  <tr>
    <td>
      <img src="area_val_error.png" width="700">
    </td>
    <td>
      {df_area_sob_grafico.to_html()}
    </td>
  </tr>
</table>

## 4. Análise de Erros Gramaticais
Comparação da sensibilidade do modelo na detecção/geração de erros em relação ao padrão humano.

![Comparação de Número de Erros](comparacao_num_erros.png)

## 4. Estatísticas Descritivas
### Modelo {model} v{model_version}
{df_eval.describe().to_markdown()}

### Humano
{df_human.describe().to_markdown()}
"""

    # Salva apenas o arquivo .md
    report_path = os.path.join(output_path, "report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Relatório gerado com sucesso em: {output_path}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_runs", type=int, required=True)
    parser.add_argument("--eval_path", required=True)
    parser.add_argument("--human_path", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--model_version", required=True)
    args = parser.parse_args()
    main(args.num_runs, args.eval_path, args.human_path, args.model, args.model_version)