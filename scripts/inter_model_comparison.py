from .full_report import get_full_model_df, get_full_human_df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import cohen_kappa_score

from .utils import print_full

def model_name_abbreviation(model_name):
    abbreviations = {
        "claude-opus-4-6": "claude",
        "gemma-4-31B-it": "gemma",
        "gpt-oss-120b": "gpt",
        "Qwen3.6-35B-A3B": "qwen",
        "sabia-4": "sabia"
    }

    return abbreviations.get(model_name)

def real_prompt_name(prompt_name):
    name_dict = {
        "7": "Nota por Critério",
        "8": "Nota Total",
        "9": "Nota por Faixa"
    }

    return name_dict.get(str(prompt_name))

def inter_model_correlation(complete_df, model_list):
    lista_prompts = complete_df["prompt"].unique()
    fig, axes = plt.subplots(len(lista_prompts), 2, figsize=(10, 10))

    scaler = MinMaxScaler()
    for prompt in range(len(lista_prompts)):
        temp_df = complete_df[complete_df["prompt"] == lista_prompts[prompt]]

        treated_df = pd.DataFrame()

        for model in model_list:
            treated_df[model_name_abbreviation(model)] = temp_df[temp_df["judge"] == model]["nota_final"].reset_index(drop=True)

        df_normalizado = scaler.fit_transform(treated_df)
        df_normalizado = pd.DataFrame(df_normalizado, columns=treated_df.columns)

        df_correlacao_pearson = df_normalizado.corr(method="pearson")
        df_correlacao_spearman = df_normalizado.corr(method="spearman")

        axes[prompt, 0] = sns.heatmap(df_correlacao_pearson, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".2f", ax=axes[prompt, 0], cbar=True)
        axes[prompt, 0].xaxis.tick_top()
        axes[prompt, 0].set_title(f"Pearson \n {real_prompt_name(lista_prompts[prompt])}")
        axes[prompt, 1] = sns.heatmap(df_correlacao_spearman, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".2f", ax=axes[prompt, 1], cbar=True)
        axes[prompt, 1].xaxis.tick_top()
        axes[prompt, 1].set_title(f"Spearman \n {real_prompt_name(lista_prompts[prompt])}")

    plt.subplots_adjust(wspace=0.175, hspace=0.4)

    plt.suptitle("Correlações Inter-Modelos", fontsize=15.0)
    plt.savefig(os.path.join("prompt_testing", "reports", "Correlacao_inter_modelos.png"))

def inter_model_QWK(complete_df, model_list, bins:int=5):
    lista_prompts = complete_df["prompt"].unique()
    fig, axes = plt.subplots(len(lista_prompts), 1, figsize=(5, 9))

    for prompt in range(len(lista_prompts)):
        temp_df = complete_df[complete_df["prompt"] == lista_prompts[prompt]]

        treated_df = pd.DataFrame()
        kappa_df = pd.DataFrame(index=list(map(model_name_abbreviation, model_list)))

        for model in model_list:
            treated_df[model_name_abbreviation(model)] = temp_df[temp_df["judge"] == model]["nota_final"].reset_index(drop=True)

        treated_df = (treated_df//bins).astype(int)

        nota_max = 70
        kappa_labels = [x//bins for x in range(0, nota_max, bins)]

        for model_ref in model_list:
            kappa_per_model = []
            for model_pred in model_list:
                kappa_per_model.append(cohen_kappa_score(treated_df[model_name_abbreviation(model_ref)], treated_df[model_name_abbreviation(model_pred)], weights="quadratic", labels=kappa_labels))
            
            kappa_df.insert(len(kappa_df.columns), model_name_abbreviation(model_ref), kappa_per_model)

        axes[prompt] = sns.heatmap(kappa_df, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", ax=axes[prompt], fmt=".2f")
        axes[prompt].set_title(f"{real_prompt_name(lista_prompts[prompt])}")
        axes[prompt].xaxis.tick_top()

    plt.subplots_adjust(hspace=0.3)

    plt.suptitle("QWK Inter-Modelos", fontsize=12.0)
    plt.savefig(os.path.join("prompt_testing", "reports", "QWK_inter_modelos.png"))

def inter_model_boxplot(complete_df):
    fig, ax = plt.subplots(1, figsize=(8, 6))
    human_df = get_full_human_df(os.path.join(os.getcwd(), "prompt_testing", "sheets", "notas_humanas"))
    
    complete_df["judge"] = complete_df["judge"].apply(model_name_abbreviation)
    complete_df["prompt"] = complete_df["prompt"].apply(real_prompt_name)
    complete_df = pd.concat([human_df, complete_df], ignore_index=True)
    complete_df.loc[complete_df["judge"] == "humano", "prompt"] = "Nota Humana"

    sns.boxplot(complete_df, x="judge", y="nota_final", hue="prompt", showfliers=False, palette=["#FF6B6B", "#11F9DE", "#FFD918", "#A3FF22"])

    ax.set_yticks(range(20, 71, 5))
    ax.set_xlabel("Avaliadores")
    ax.set_ylabel("Notas")
    sns.move_legend(ax, loc="best", title="")
    plt.suptitle("Boxplot das notas por modelo")
    plt.savefig(os.path.join("prompt_testing", "reports", "Boxplot_inter_modelos.png"))
        
def inter_model_error_scatterplot(complete_df):
    fig, ax = plt.subplots(figsize=(12, 12))

    human_df = get_full_human_df(os.path.join(os.getcwd(), "prompt_testing", "sheets", "notas_humanas"))
    complete_df = complete_df.merge(human_df, on=["redacao"], how='inner', suffixes=("_model", "_human"))

    complete_df["erro"] = complete_df["nota_final_model"] - complete_df["nota_final_human"]

    #complete_df = complete_df.loc[abs(complete_df["erro"]) < 100]

    #complete_df = complete_df.loc[(complete_df["judge_model"] == "gpt-oss-120b") | (complete_df["judge_model"] == "claude-opus-4-6") | (complete_df["judge_model"] == "Qwen3.6-35B-A3B")]

    complete_df["judge_model"] = complete_df["judge_model"].apply(model_name_abbreviation)
    complete_df["prompt"] = complete_df["prompt"].apply(real_prompt_name)

    complete_df = complete_df.rename(columns={"judge_model":"Modelos", "prompt":"Prompts"})

    tam_fonte=15.0

    #ax.set_yticks(range(-42, 32, 10), fontsize=tam_fonte-5)
    sns.scatterplot(complete_df, x="nota_final_human", y="erro", hue="Modelos", style="Prompts", markers=["o", "X", "D"], palette=["#FF9D00", "#61ADFF", "#BB0000", "#800B9B", "#2F8600"])
    sns.move_legend(ax, loc="best", title="", fontsize=tam_fonte-2)
    ax.set_ylim(-41, 30)
    ax.set_xlim(29.5, 70.5)
    ax.set_xlabel("Notas Humanas", fontsize=tam_fonte)
    ax.set_ylabel("Erro", fontsize=tam_fonte)

    plt.axhline(y=0, color='black', linestyle=(0, (1, 1)))

    inversa_afim_x = np.linspace(30, 70, 200)
    m = -1
    n = 50
    plt.plot(inversa_afim_x, m*inversa_afim_x+n, color="black", linestyle=(5, (10, 3)))

    plt.suptitle("Scatterplot do erro dos modelos", fontsize=tam_fonte+5)
    plt.savefig(os.path.join("prompt_testing", "reports", "Scatterplot_inter_modelos_erro.png"))

def inter_model_scores_scatterplot(complete_df):
    fig, ax = plt.subplots(figsize=(8, 8))

    human_df = get_full_human_df(os.path.join(os.getcwd(), "prompt_testing", "sheets", "notas_humanas"))
    complete_df = complete_df.merge(human_df, on=["redacao"], how='inner', suffixes=("_model", "_human"))

    complete_df["erro"] = complete_df["nota_final_model"] - complete_df["nota_final_human"]

    complete_df = complete_df.loc[complete_df["nota_final_model"] > 30]

    complete_df["judge_model"] = complete_df["judge_model"].apply(model_name_abbreviation)
    complete_df["prompt"] = complete_df["prompt"].apply(real_prompt_name)

    complete_df = complete_df.rename(columns={"judge_model":"Modelos", "prompt":"Prompts"})

    #ax.set_yticks(range(-max_value, max_value+1, 5))
    sns.scatterplot(complete_df, x="nota_final_human", y="nota_final_model", hue="Modelos", style="Prompts", markers=["o", "X", "D"], palette=["#FF9D00", "#61ADFF", "#BB0000", "#800B9B", "#2F8600"])
    sns.move_legend(ax, loc="best", title="", fontsize="x-small")
    ax.set_ylim(30, 70.5)
    ax.set_xlim(30, 70.5)
    ax.set_xticks(range(30, 71, 5))
    ax.set_xlabel("Notas Humanas")
    ax.set_ylabel("Notas Modelos")

    afim = np.linspace(30, 70.5, 200)
    ax.plot(afim, afim, color="black", linestyle="dashed")

    plt.suptitle("Scatterplot das notas dos modelos")
    plt.savefig(os.path.join("prompt_testing", "reports", "Scatterplot_inter_modelos_score.png"))

def main(model_list, num_runs):
    models_dfs = []
    for model in model_list:
        path_model_sheets = os.path.join(os.getcwd(), "prompt_testing", "sheets", model)
        full_model_df = get_full_model_df(path_model_sheets, num_runs)

        # As redações aqui estão ordenas pela "ordem de chegada"
        # Estão ordenadas de forma diferente de full_report
        # Porém, isso não deve ser um problema, visto que só queremos calcular a correlação

        num_redacoes = len(full_model_df["redacao"].tolist())//num_runs
        full_model_df["redacao"] = np.repeat(np.arange(1, num_redacoes + 1), num_runs)

        models_dfs.append(full_model_df)

    complete_df = pd.concat(models_dfs, ignore_index=True)
    complete_df["nota_final"] = complete_df["nota_final"].astype(float)

    #inter_model_correlation(complete_df, model_list)
    #inter_model_QWK(complete_df, model_list, 5)

    complete_df = complete_df[complete_df["nota_final"] > 0]
    #inter_model_boxplot(complete_df)
    inter_model_error_scatterplot(complete_df)
    inter_model_scores_scatterplot(complete_df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, nargs="+", required=True)
    parser.add_argument("--num_runs", type=int, required=True)
    args = parser.parse_args()
    
    main(args.models, args.num_runs)