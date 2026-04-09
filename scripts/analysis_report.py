import os
import numpy as np
import pandas as pd
import argparse
from datetime import datetime
from sklearn.metrics import cohen_kappa_score, roc_auc_score

from sklearn.preprocessing import MinMaxScaler
import yaml

from .plot import plot_distribuicao_notas, plot_eval_human_num_errors, plot_eval_human_scores, plot_val_error, plot_error_heatmap
from .utils import get_mean

def print_full(df):
    pd.set_option('display.max_rows', len(df))
    pd.set_option('display.max_columns', len(df.columns))
    pd.set_option('display.expand_frame_repr', False)
    print(df)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.expand_frame_repr')

def main(num_runs, eval_path, human_path, model, model_version, year):
    pd.set_option('future.no_silent_downcasting', True)
    root_path = os.getcwd()
    output_path = os.path.join(root_path, "prompt_testing", "reports", f"{model}-{model_version}_{year}_{num_runs}_runs")
    os.makedirs(output_path, exist_ok=True)

    # Carregando dados
    df_eval = get_mean(eval_path, num_runs)

    #Tratando apenas hiperparâmetros desejáveis
    df_eval["prompt"] = df_eval["prompt"].astype(int)
    #df_eval = df_eval[(df_eval["prompt"] != 10) & (df_eval["prompt"] != 7) & (df_eval["prompt"] != 13)]
    df_eval["temp"] = df_eval["temp"].astype(float)
    #df_eval = df_eval[df_eval["temp"] != 0.9]

    df_human = pd.read_csv(human_path)
    df_human.drop(columns=["versao", "prompt", "temp", "faixa"], inplace=True)

    # Calculando métricas adicionais
    df_merged = df_eval.merge(
    df_human[["redacao", "nota_final", "num_errors"]].rename(columns={"nota_final": "nota_humana", "num_errors": "erros_humano"}), on="redacao")
    df_merged["val_error"] =  abs(df_merged["nota_humana"] - df_merged["nota_final"])
    df_merged["val_error_squared"] = df_merged["val_error"] ** 2

    df_notas = pd.DataFrame()
    df_notas['redacao'] = df_merged["redacao"].unique()
    df_notas = df_notas.set_index('redacao')
    df_notas['human'] = df_human["nota_final"].values

    areas = {}
    for (prompt, temp), group in df_merged.groupby(["prompt", "temp"]):
        area = np.trapezoid(group["val_error"], group["redacao"])
        mae = group['val_error'].mean()
        rmse = np.sqrt((group['val_error'] ** 2).mean())
        # qwk = cohen_kappa_score(np.round(group["nota_humana"]).astype(int), np.round(group["nota_final"]).astype(int))
        # auc_roc = roc_auc_score(np.round(group["nota_humana"]).astype(int), np.round(group["nota_final"]).astype(int))
        areas[(prompt, temp)] = prompt, temp, area.round(4), mae.round(4), rmse.round(4) #, qwk.round(4), auc_roc.round(4)
        df_notas[f"p{prompt}, t{temp}"] = group["nota_final"].values
    
    df_area_sob_grafico = pd.DataFrame.from_dict(areas, orient='index', columns=['prompt', 'temp', 'area_sob_curva', 'mae', 'rmse']).reset_index(drop=True)
    scaler = MinMaxScaler()
    df_notas_normalizado = scaler.fit_transform(df_notas)
    df_notas_normalizado = pd.DataFrame(df_notas_normalizado, columns=df_notas.columns, index=df_notas.index)

    # Gerando gráficos
    # 1. Distribuição de Notas
    with open(os.path.join(root_path, "prompt_testing", "prompts.yaml"), 'r', encoding='utf-8') as file:
        prompts_yaml = yaml.safe_load(file)
        prompts = prompts_yaml['prompts']

    plot_error_heatmap(df_merged, output_path)

    plot_distribuicao_notas(df_eval, df_human, prompts, output_path)

    # 2. Comparação entre Notas Geradas e Humanas
    plot_eval_human_scores(df_merged, output_path)

    # 3. Erro de Validação
    plot_val_error(df_merged, output_path)

    # 4. Comparação entre Números de Erros Gerados e Humanos
    plot_eval_human_num_errors(df_merged, df_human, output_path)
    
    df_human_aligned = df_human.reindex(columns=df_merged.columns)

		# 5. Avaliaação por Temperatura
    for temperatura in df_merged["temp"].unique():
      temppaths = os.path.join(output_path, "temps", f"temp {str(temperatura)}")
      os.makedirs(temppaths, exist_ok=True)
      df_per_temp = df_merged[df_merged["temp"] == temperatura]
    
      plot_val_error(df_per_temp, temppaths, temp=temperatura)
      
      df_per_temp = pd.concat([df_per_temp, df_human_aligned], ignore_index=True)
      df_per_temp["prompt"] = df_per_temp["prompt"].fillna("Humano")
      df_per_temp["num_errors"] = df_per_temp["num_errors"].replace("-", 0)

      plot_eval_human_scores(df_per_temp, temppaths, temp=temperatura)

      plot_eval_human_num_errors(df_per_temp, df_human, temppaths, temp=temperatura)

    # 6. Avaliação por Prompt
    for prompt in df_merged["prompt"].unique():
      promptpaths = os.path.join(output_path, "prompts", f"prompt {str(prompt)}")
      os.makedirs(promptpaths, exist_ok=True)
      df_per_prompt = df_merged[df_merged["prompt"] == prompt]
    
      plot_val_error(df_per_prompt, promptpaths, prompt=prompt)
      
      df_per_prompt = pd.concat([df_per_prompt, df_human_aligned], ignore_index=True)
      df_per_prompt["prompt"] = df_per_prompt["prompt"].fillna("Humano")
      df_per_prompt["num_errors"] = df_per_prompt["num_errors"].replace("-", 0)

      plot_eval_human_scores(df_per_prompt, promptpaths, prompt=prompt)

      plot_eval_human_num_errors(df_per_prompt, df_human, promptpaths, prompt=prompt)
      
    # Gerando resumo em markdown
    md_content = f"""# Relatório de Avaliação: {model}-{model_version} - {num_runs} execuções
**Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}**

## 1. Distribuição de Notas
Nesta seção comparamos as notas atribuídas pelo modelo {model} em diferentes prompts/temperaturas versus a correção humana.

![Distribuição de Notas](distribuicao_notas.png)

## 2. Comparação de Notas Geradas e Humanas
Nesta seção, apresentamos a comparação entre as notas finais geradas pelo modelo e as notas dadas por avaliadores humanos.

![Comparação Notas](comparacao_notas.png)

## 3. Análise de Erro Absoluto de Validação

<table>
  <tr>
    <td>
      <img src="area_val_error.png" width="700">
    </td>
    <td>
      {df_area_sob_grafico.to_html(index=False, justify="center")}
    </td>
  </tr>
</table>

## 4. Análise de Erros Gramaticais
Comparação da sensibilidade do modelo na detecção/geração de erros em relação ao padrão humano.

![Comparação de Número de Erros](comparacao_num_erros.png)

## 5. Correlação de Pearson
{df_notas_normalizado.corr(method='pearson').to_markdown()}

## 6. Correlação de Spearman
{df_notas_normalizado.corr(method='spearman').to_markdown()}

## Estatísticas Descritivas
### Modelo {model}-{model_version}
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
    parser.add_argument("--year", required=True, type=str)
    args = parser.parse_args()
    main(args.num_runs, args.eval_path, args.human_path, args.model, args.model_version, args.year)