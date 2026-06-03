from .full_report import get_full_model_df
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
    fig, axes = plt.subplots(len(lista_prompts), 2, figsize=(12, 16))

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

        axes[prompt, 0] = sns.heatmap(df_correlacao_pearson, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".2f", ax=axes[prompt, 0], cbar=False)
        axes[prompt, 0].xaxis.tick_top()
        axes[prompt, 0].set_title(f"Pearson \n {real_prompt_name(lista_prompts[prompt])}")
        axes[prompt, 1] = sns.heatmap(df_correlacao_spearman, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".2f", ax=axes[prompt, 1], cbar=True)
        axes[prompt, 1].xaxis.tick_top()
        axes[prompt, 1].set_title(f"Spearman \n {real_prompt_name(lista_prompts[prompt])}")

    plt.subplots_adjust(hspace=0.3)

    plt.suptitle("Correlações Inter-Modelos", fontsize=30.0)
    plt.savefig(os.path.join("prompt_testing", "reports", "Correlacao_inter_modelos.png"))

def inter_model_QWK(complete_df, model_list, bins:int=5):
    lista_prompts = complete_df["prompt"].unique()
    fig, axes = plt.subplots(len(lista_prompts), 1, figsize=(6, 16))

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

        axes[prompt] = sns.heatmap(kappa_df, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", ax=axes[prompt])
        axes[prompt].set_title(f"{real_prompt_name(lista_prompts[prompt])}")
        axes[prompt].xaxis.tick_top()

    plt.subplots_adjust(hspace=0.3)

    plt.suptitle("QWK Inter-Modelos", fontsize=30.0)
    plt.savefig(os.path.join("prompt_testing", "reports", "QWK_inter_modelos.png"))

        
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

    inter_model_correlation(complete_df, model_list)
    inter_model_QWK(complete_df, model_list, 5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, nargs="+", required=True)
    parser.add_argument("--num_runs", type=int, required=True)
    args = parser.parse_args()
    
    main(args.models, args.num_runs)