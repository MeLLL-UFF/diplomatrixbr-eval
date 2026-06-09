import os
import pandas as pd
from sklearn.metrics import cohen_kappa_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
from sklearn.preprocessing import MinMaxScaler
import math

from .utils import get_mean, print_full

def quadratic_weighted_kappa(df: pd.DataFrame, bin_div: int = 1):
    prompts = df["prompt"].unique()
    years = sorted(df["ano"].unique())

    cohen_df = pd.DataFrame(index=prompts)

    for year in years:
        cohen_ano = []
        for prompt in prompts:
            df_format = df[(df["ano"] == year) & (df["prompt"] == prompt)]
            notas_modelos = df_format["nota_final_model"].astype(int).to_list()
            notas_humanos = df_format["nota_final_human"].astype(int).to_list()

            notas_modelos = list(map(lambda x: x//bin_div, notas_modelos))
            notas_humanos = list(map(lambda x: x//bin_div, notas_humanos))

            nota_max = 60 if year != "2024" else 70
            labels_kappa = [x//bin_div for x in range(0, nota_max, bin_div)]

            cohen_ano.append(cohen_kappa_score(notas_humanos, notas_modelos, weights='quadratic', labels=labels_kappa))
        cohen_df.insert(len(cohen_df.columns), year, cohen_ano)

    return cohen_df

def plot_qwk(df, model, path):
    fig, axes = plt.subplots(1, figsize=(12,6))

    axes = sns.heatmap(df, annot=True, vmax=1, vmin=-1, cmap="RdYlGn")
    axes.set_title(f"QWK \n {model}")
    axes.set_xlabel("anos")
    axes.set_ylabel("prompts")

    plt.savefig(f"{path}/QWK.png")

def plot_RMSE(df, model, path):
    fig, axes = plt.subplots(1, figsize=(12,6))

    df = df[["prompt", "ano", "val_squared_error"]]

    df = df.groupby(["prompt", "ano"]).mean()
    df["val_squared_error"] = df["val_squared_error"] ** 0.5
    df = df.reset_index()
    df = df.pivot(index="prompt", columns="ano")
    df = df.droplevel(0, axis=1)

    axes = sns.heatmap(df, annot=True, cmap="RdYlGn_r", vmin=0, vmax=10)

    axes.set_title(f"RMSE \n {model}")
    axes.set_xlabel("anos")
    axes.set_ylabel("prompts")

    plt.savefig(f"{path}/RMSE.png")

def plot_corr(df, model, path):
    prompts = list(df["prompt"].unique())

    df_normalizado = pd.DataFrame(df.loc[:, ["nota_final_human", "redacao", "ano"]])
    df_normalizado = df_normalizado.groupby(["ano", "redacao"]).mean().reset_index(level=1, drop=True)
    
    index_anos = df_normalizado.index

    for prompt in prompts:
        temp = df[df["prompt"] == prompt]
        temp = pd.Series(temp["nota_final_model"].reset_index(drop=True))
        temp.index = index_anos

        df_normalizado.insert(len(df_normalizado.columns), str(prompt), temp)

    scaler = MinMaxScaler()

    df_normalizado.index = index_anos
    anos = list(df_normalizado.index.unique())

    df_corr_pearson = pd.DataFrame()
    df_corr_spearman = pd.DataFrame()
    for ano in anos:
        temp = df_normalizado.loc[ano]
        transform_temp = scaler.fit_transform(temp)
        transform_temp = pd.DataFrame(transform_temp, columns=df_normalizado.columns)

        df_corr_pearson.insert(len(df_corr_pearson.columns), ano, transform_temp.corr(method="pearson")["nota_final_human"])
        df_corr_spearman.insert(len(df_corr_spearman.columns), ano, transform_temp.corr(method="spearman")["nota_final_human"])

    df_corr_pearson = df_corr_pearson.loc[str(prompts[0]):]
    df_corr_spearman = df_corr_spearman.loc[str(prompts[0]):]

    fig, axes = plt.subplots(2, 1, figsize=(12,10))

    axes[0] = sns.heatmap(df_corr_pearson, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".4f", ax=axes[0])
    axes[0].set_title("Correlação de Pearson")
    axes[1] = sns.heatmap(df_corr_spearman, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".4f", ax=axes[1])
    axes[1].set_title("Correlação de Spearman")

    axes[0].set_xlabel("anos")
    axes[0].set_ylabel("prompts")
    axes[1].set_xlabel("anos")
    axes[1].set_ylabel("prompts")
    plt.suptitle(f"Correlações \n {model}")

    plt.savefig(f"{path}/Correlacoes.png")

def plot_comparacao_notas(df_plot, model_name, output_path, num_redacoes, *, separador_ano:bool=False):
    fig, ax = plt.subplots(1, 1, figsize=(20, 6))

    if separador_ano == True:
        separador = df_plot[["ano", "redacao"]]
        separador["mudanca_ano"] = df_plot[["ano"]] != df_plot[["ano"]].shift()
        mudanca_ano_indices = separador[separador["mudanca_ano"] == True]
        mudanca_ano_indices = mudanca_ano_indices["redacao"].to_list()

        for sep in range(0, len(mudanca_ano_indices)-1):
            if sep%2 == 0:
                continue
            plt.axvspan(mudanca_ano_indices[sep]-1, mudanca_ano_indices[sep+1]-2, color="#CBCBCB4C")

    df_plot["redacao"] = "C" + df_plot["redacao"].astype(str)

    sns.lineplot(
        data=df_plot,
        x="redacao",
        y="nota_final_model",
        hue="prompt",
        marker="o",
        palette=["#11F9DE", "#FFD918", "#A3FF22"],
        ax=ax
    )

    # Pega uma linha por redação para a nota humana
    df_human = df_plot.drop_duplicates(subset="redacao")[["redacao", "nota_final_human"]]

    sns.lineplot(
        data=df_human,
        x="redacao",
        y="nota_final_human",
        marker="o",
        color="#FF6B6B",
        label="Nota Humana",
        ax=ax
    )

    ax.set_title(f"Comparação de Nota Gerada e Nota Humana por Candidato\n{model_name}", fontsize=16)
    ax.set_xlabel("Candidatos")
    ax.set_ylabel("Nota Final")
    ax.set_ylim(30, 70)
    ax.legend(bbox_to_anchor=(1, 1.1), loc="upper left")
    ax.spines[['top', 'right']].set_visible(True)
    ax.set_xlim(1, num_redacoes)
    ax.set_xticks(list(range(0, num_redacoes)))
    ax.tick_params(axis='x', labelrotation=45)

    plt.tight_layout(rect=[0, 0, 1.1, 0.95])
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def get_full_model_df(path_model_sheets, num_runs):
    list_path_model_sheets = os.listdir(path_model_sheets)
    list_path_model_sheets.sort()

    sheet_list = []
    for sheet_path in list_path_model_sheets:
        sheet_full_path = os.path.join(path_model_sheets, sheet_path)

        #Hardcoded, alta propensão a erros, verificar nome dado a pasta dos modelos (separar o nome do modelo com - e as características da geração com _)
        year = sheet_path.split("_")[1]

        sheet = get_mean(sheet_full_path, num_runs)

        sheet.insert(len(sheet.columns), "ano", year)
        sheet_list.append(sheet)

    return pd.concat(sheet_list, ignore_index=True)

def get_full_human_df(path_human_sheets):
    
    list_path_human_sheets = os.listdir(path_human_sheets)
    list_path_human_sheets.sort()

    sheet_list = []
    for sheet_path in list_path_human_sheets:
        sheet_full_path = os.path.join(path_human_sheets, sheet_path)

        year = sheet_path.split("_")[-1]
        #year = 20XX.csv
        year = year.split(".")[0]

        sheet = pd.read_csv(sheet_full_path)
        sheet.drop(["1A", "1B", "1C", "CGPL"], axis=1)

        sheet.insert(len(sheet.columns), "ano", year)
        sheet_list.append(sheet)

    return pd.concat(sheet_list, ignore_index=True)

def full_report(num_runs, num_redacoes, model_name):
    path_model_sheets = os.path.join(os.getcwd(), "prompt_testing", "sheets", model_name)

    model_df = get_full_model_df(path_model_sheets, num_runs)

    path_human_sheets = os.path.join(os.getcwd(), "prompt_testing", "sheets", "notas_humanas")

    human_df = get_full_human_df(path_human_sheets)

    df = model_df.merge(human_df, on=["ano", "redacao"], how='inner', suffixes=("_model", "_human"))

    df.insert(len(df.columns), "val_squared_error", (df["nota_final_human"] - df["nota_final_model"])**2)

    cohen_kappa_df = quadratic_weighted_kappa(df, 5)

    output_path = os.path.join(os.getcwd(), "prompt_testing", "reports", model_name)
    plot_RMSE(df, model_name, output_path)
    plot_qwk(cohen_kappa_df, model_name, output_path)
    plot_corr(df, model_name, output_path)

    df_plot = df.copy()
    df_plot_decrescente = df_plot.sort_values(by=["nota_final_human", "redacao", "ano", "prompt"], ascending=[False, True, False, True])
    df_plot_ano = df_plot.sort_values(by=["ano", "nota_final_human", "redacao", "prompt"], ascending=[False, False, True, True])

    df_plot_ano["redacao"] = np.repeat(np.arange(1, num_redacoes + 1), num_runs)
    df_plot_ano["prompt"] = df_plot_ano["prompt"].astype(str)
    df_plot_ano["prompt"] = df_plot_ano["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão"})

    df_plot_decrescente["redacao"] = np.repeat(np.arange(1, num_redacoes + 1), num_runs)
    df_plot_decrescente["prompt"] = df_plot_decrescente["prompt"].astype(str)
    df_plot_decrescente["prompt"] = df_plot_decrescente["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão"})

    plot_comparacao_notas(df_plot_decrescente, model_name, f"{output_path}/comparacao_notas.png", num_redacoes)
    plot_comparacao_notas(df_plot_ano, model_name, f"{output_path}/comparacao_notas_ano.png", num_redacoes, separador_ano=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_runs", type=int, required=True)
    parser.add_argument("--num_redacoes", type=int, required=True)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()
    
    full_report(args.num_runs, args.num_redacoes, args.model)