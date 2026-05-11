import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import textwrap
import math
import seaborn as sns
import pandas as pd

def print_full(df):
    pd.set_option('display.max_rows', len(df))
    pd.set_option('display.max_columns', len(df.columns))
    pd.set_option('display.expand_frame_repr', False)
    print(df)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.expand_frame_repr')

def plot_distribuicao_notas(df_eval, df_human, prompts, output_path):
    plot_ids = [0] + df_eval["prompt"].unique().tolist()
    num_plots = len(plot_ids)
    ncols = 3
    nrows = math.ceil(num_plots / ncols)
    
    fig, axes = plt.subplots(nrows, ncols, figsize=(18, 5 * nrows))
    axes = axes.flatten()

    for idx, i in enumerate(plot_ids):
        ax = axes[idx]
        
        # Seleção de dados e título (Lógica original)
        if i == 0:
            subset = df_human
            title = "Avaliação Humana"
        else:
            subset = df_eval[df_eval['prompt'] == i]
            desc = f"Prompt {i}: " + prompts[i+1]["description"]
            title = "\n".join(textwrap.wrap(desc, width=40))

        sns.histplot(subset["nota_final"], kde=True, ax=ax, color="#41ACCF" if i != 0 else "#1E9D1E")

        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_xlabel("Nota")
        ax.set_ylabel("Frequência")
        ax.set_xlim(40, 60)
        ax.set_ylim(0, 15)
        ax.spines[['top', 'right']].set_visible(False)

    # Remove eixos vazios
    for j in range(idx + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig(f"{output_path}/distribuicao_notas.png", dpi=300, bbox_inches='tight')
    plt.close()

def plot_val_error(df, output_path, year, *, temp=None, prompt=None):
    fig, ax = plt.subplots(figsize=(10, 6))

    df = df.copy()
    df["prompt"] = df["prompt"].astype(str)
    df["prompt"] = df["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão", "10":"10 - Critério COM padrão", "11":"11 - Total COM padrão", "12":"12 - Faixa COM padrão", "13":"13 - Critério COM genérico", "14":"14 - Total COM genérico", "15":"15 - Faixa COM genérico"})

    if prompt is None:
        sns.lineplot(
            data=df,
            x="redacao",
            y="val_error",
            hue="prompt",
            style="temp",
            marker="o",
            palette=["#11F9DE", "#FFD918", "#A3FF22", "#1995BF", "#FF8400FF", "#02B202", "#3131BD", "#D41111", "#2E772E"],
            ax=ax
        )
    else:
        sns.lineplot(
            data=df,
            x="redacao",
            y="val_error",
            hue="temp",
            marker="o",
            palette=["#444DFA", "#FA4743", "#FAD543", "#43FA7F"],
            ax=ax
        )

    title = f"Análise de Erro de Validação \n {year}"
    if temp is not None:
        title += f"\n Temperatura {temp}"
    if prompt is not None:
        title += f"\n Prompt {df.iloc[0, 1]}"
    ax.set_title(title)

    ax.set_xlabel("Redação")
    ax.set_ylabel("Erro")
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(bbox_to_anchor=(0.97, 0.8), loc="upper left")
    
    if (max(df["val_error"].to_list()) > 30):
        ax.set_ylim(0,30)
    else:
        ax.set_ylim()

    plt.tight_layout(rect=[0, 0, 1.1, 0.95])
    plt.savefig(f"{output_path}/area_val_error.png", dpi=300, bbox_inches='tight')
    plt.close()

def plot_eval_human_scores(df, output_path, year, *, temp=None, prompt=None):
    if temp == None and prompt == None:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    else:
        fig, axes = plt.subplots(figsize=(7, 5))
    
    df = df.copy()
    df = df.sort_values(by=["prompt", "nota_humana"], ascending=[True, False])
    df["redacao"] = df["redacao"].astype(str)
    df["prompt"] = df["prompt"].astype(str)
    df["prompt"] = df["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão", "10":"10 - Critério COM padrão", "11":"11 - Total COM padrão", "12":"12 - Faixa COM padrão", "13":"13 - Critério COM genérico", "14":"14 - Total COM genérico", "15":"15 - Faixa COM genérico"})

    if prompt is not None:
        df["temp"] = df["temp"].astype(str)
        mask_humano = df["judge"] == "humano"
        df.loc[mask_humano, "temp"] = "Humano"

    title = f"Comparação de Nota Gerada e Nota Humana por Redação \n {year}"

    if temp == None and prompt == None:
        sns.lineplot(
            data=df,
            x="redacao",
            y="nota_final",
            hue="prompt",
            style="temp",
            marker="o",
            palette=["#11F9DE", "#FFD918", "#A3FF22", "#1995BF", "#FF8400FF", "#02B202", "#3131BD", "#D41111", "#2E772E"],
            ax=axes[0],
            sort=False
        )
        axes[0].set_title("Análise de Nota Gerada por Redação")
        axes[0].set_xlabel("Redação")
        axes[0].set_ylabel("Nota Final")
        axes[0].set_ylim(35, 60)
        axes[0].legend(bbox_to_anchor=(0.97, 1.1), loc="upper left")
        axes[0].spines[['top', 'right']].set_visible(False)

        sns.lineplot(
            data=df,
            x="redacao",
            y="nota_humana",
            marker="o",
            ax=axes[1],
            sort=False
        )
        axes[1].set_title("Análise de Nota Humana por Redação")
        axes[1].set_xlabel("Redação")
        axes[1].set_ylabel("Nota Final")
        axes[1].set_ylim(35, 60)
        axes[1].spines[['top', 'right']].set_visible(False)

        plt.suptitle(title, fontsize=16)

    elif temp != None:
        sns.lineplot(
            data=df,
            x="redacao",
            y="nota_final",
            hue="prompt",
            marker="o",
            palette=["#11F9DE", "#FFD918", "#A3FF22", "#1995BF", "#FF8400FF", "#02B202", "#3131BD", "#D41111", "#2E772E", "#000000"],
            ax=axes,
            sort=False
        )
        axes.set_xlabel("Redação")
        axes.set_ylabel("Nota Final")
        axes.set_ylim(35, 60)
        axes.legend(bbox_to_anchor=(0.97, 1.1), loc="upper left")
        axes.spines[['top', 'right']].set_visible(False)
        plt.suptitle(f"{title}\n Temperatura: {temp}", fontsize=16)
    elif prompt != None:
        sns.lineplot(
            data=df,
            x="redacao",
            y="nota_final",
            hue="temp",
            marker="o",
            palette=["#444DFA", "#FA4743", "#FAD543", "#43FA7F", "#000000"],
            ax=axes,
            sort=False
        )
        axes.set_xlabel("Redação")
        axes.set_ylabel("Nota Final")
        axes.set_ylim(35, 60)
        axes.legend(bbox_to_anchor=(0.97, 1.1), loc="upper left")
        axes.spines[['top', 'right']].set_visible(False)
        plt.suptitle(f"{title}\n Prompt: {df.iloc[0, 1]}", fontsize=16)

    
    plt.tight_layout(rect=[0, 0, 1.1, 0.95])
    plt.savefig(f"{output_path}/comparacao_notas.png", dpi=300, bbox_inches='tight')
    plt.close()

def plot_eval_human_num_errors(df_merged, df_human, output_path, year, *, temp=None, prompt=None):
    if temp == None and prompt == None:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    else:
        fig, axes = plt.subplots(figsize=(7, 5))

    if temp is not None or prompt is not None:
        mask_humano = df_merged["judge"] == "humano"
        df_merged.loc[mask_humano, "erros_humano"] = df_merged.loc[mask_humano, "num_errors"]
    
    if prompt is not None:
        df_merged["temp"] = df_merged["temp"].astype(str)
        mask_humano = df_merged["judge"] == "humano"
        df_merged.loc[mask_humano, "temp"] = "Humano"

    df_human = df_human.copy()
    df_human = df_human.sort_values(by=["num_errors", "redacao"], ascending=[False, True])
    df_human["redacao"] = df_human["redacao"].astype(str)

    df_merged = df_merged.copy()
    df_merged = df_merged.sort_values(by=["erros_humano", "redacao"], ascending=[False, True])
    df_merged["redacao"] = df_merged["redacao"].astype(str)

    df_merged["prompt"] = df_merged["prompt"].astype(str)
    df_merged["prompt"] = df_merged["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão", "10":"10 - Critério COM padrão", "11":"11 - Total COM padrão", "12":"12 - Faixa COM padrão", "13":"13 - Critério COM genérico", "14":"14 - Total COM genérico", "15":"15 - Faixa COM genérico"})

    title = f"Comparação de Número de Erros Gerados e Humanos por Redação \n {year}"

    if temp == None and prompt == None:
        sns.lineplot(
            data=df_merged,
            x="redacao",
            y="num_errors",
            hue="prompt",
            style="temp",
            marker="o",
            palette=["#11F9DE", "#FFD918", "#A3FF22", "#1995BF", "#FF8400FF", "#02B202", "#3131BD", "#D41111", "#2E772E"],
            ax=axes[0]
        )
        axes[0].set_title("Análise de Número de Erros Gerados por Redação")
        axes[0].set_xlabel("Redação")
        axes[0].set_ylabel("Número de Erros")
        axes[0].set_yticks([0, 1, 2, 3, 4])
        axes[0].legend(bbox_to_anchor=(0.97, 1.1), loc="upper left")
        axes[0].spines[['top', 'right']].set_visible(False)

        sns.lineplot(
            data=df_human,
            x="redacao",
            y="num_errors",
            marker="o",
            ax=axes[1],
            sort=False
        )
        axes[1].set_title("Análise de Número de Erros Humanos por Redação")
        axes[1].set_xlabel("Redação")
        axes[1].set_ylabel("Número de Erros")
        axes[1].set_yticks([0, 1, 2, 3, 4, 5, 6])
        axes[1].set_ylim(-0.2, 6)
        axes[1].spines[['top', 'right']].set_visible(False)

        plt.suptitle(title, fontsize=16)
    elif temp != None:
        sns.lineplot(
            data=df_merged,
            x="redacao",
            y="num_errors",
            hue="prompt",
            marker="o",
            palette=["#11F9DE", "#FFD918", "#A3FF22", "#1995BF", "#FF8400FF", "#02B202", "#3131BD", "#D41111", "#2E772E", "#000000"],
            ax=axes,
            sort=False
        )
        axes.set_xlabel("Redação")
        axes.set_ylabel("Número de Erros")
        axes.set_yticks([0, 1, 2, 3, 4])
        axes.legend(bbox_to_anchor=(0.97, 1.1), loc="upper left")
        axes.spines[['top', 'right']].set_visible(False)
        plt.suptitle(f"{title}\n Temperatura: {temp}", fontsize=16)
    elif prompt != None:
        sns.lineplot(
            data=df_merged,
            x="redacao",
            y="num_errors",
            hue="temp",
            marker="o",
            palette=["#444DFA", "#FA4743", "#FAD543", "#43FA7F", "#000000"],
            ax=axes,
            sort=False
        )
        axes.set_xlabel("Redação")
        axes.set_ylabel("Número de Erros")
        axes.set_yticks([0, 1, 2, 3, 4])
        axes.legend(bbox_to_anchor=(0.97, 1.1), loc="upper left")
        axes.spines[['top', 'right']].set_visible(False)
        plt.suptitle(f"{title}\n Prompt: {df_merged.iloc[0, 1]}", fontsize=16)

    plt.tight_layout(rect=[0, 0, 1.1, 0.95])
    plt.savefig(f"{output_path}/comparacao_num_erros.png", dpi=300, bbox_inches='tight')
    plt.close()

def plot_error_heatmap(df, outputpath, year):
    df_treated = df[["temp", "prompt", "val_error_squared"]]
    df_treated = df_treated.groupby(by=["temp", "prompt"]).mean()
    df_treated["val_error_squared"] = df_treated["val_error_squared"] ** 0.5
    df_treated = df_treated.reset_index()
    df_treated = df_treated.pivot(index="temp", columns="prompt", values="val_error_squared")
    fig, axes = plt.subplots(figsize=(10,6))
    axes = sns.heatmap(df_treated, annot=True, cmap="RdYlGn_r", vmin=1, vmax=9)
    plt.suptitle(f"RMSE notas {year}")
    plt.savefig(f"{outputpath}/RMSE_notas_heatmap.png")

def plot_corr_heatmap(df, outputpath, year):
    fig, axes = plt.subplots(1, 2, figsize=(12,10))
    df_corr_pearson = df.corr(method="pearson")
    df_corr_pearson = pd.DataFrame(df_corr_pearson["human"])
    df_corr_spearman = df.corr(method="spearman")
    df_corr_spearman = pd.DataFrame(df_corr_spearman["human"])
    axes[0] = sns.heatmap(df_corr_pearson, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".4f", ax=axes[0], cbar=False)
    axes[0].set_title("Correlação de Pearson")
    axes[1] = sns.heatmap(df_corr_spearman, annot=True, vmax=1, vmin=-1, cmap="RdYlGn", fmt=".4f", ax=axes[1])
    axes[1].set_title("Correlação de Spearman")
    plt.suptitle(f"Correlações {year}")
    plt.savefig(f"{outputpath}/correlacoes.png")

def plot_co_var_temp(df, year, model):
    fig, axes = plt.subplots(1, figsize=(8, 8))
    df_treated = df[["redacao", "prompt", "nota_final"]]
    df_std = df_treated.groupby(by=["prompt", "redacao"]).std()
    df_mean = df_treated.groupby(by=["prompt", "redacao"]).mean()

    df_result = (df_std/df_mean)*100
    df_result = df_result.rename(columns={"nota_final":"coeficiente de variacao"})

    sns.histplot(df_result, stat="count", ax=axes)
    axes.set_title(f"Coeficiente de variação das temperaturas \n {year} \n {model}")
    axes.set_xlabel("Coeficiente em %")
    axes.yaxis.set_major_locator(MaxNLocator(integer=True))

    #plt.show()

def plot_co_var_redacao(df, year, model):
    fig, axes = plt.subplots(1, figsize=(8, 8))
    df_treated = df[["temp", "prompt", "nota_final"]]
    df_std = df_treated.groupby(by=["prompt", "temp"]).std()
    df_mean = df_treated.groupby(by=["prompt", "temp"]).mean()

    df_result = (df_std/df_mean)*100
    df_result = df_result.rename(columns={"nota_final":"coeficiente de variacao"})

    sns.histplot(df_result, stat="count", ax=axes)
    axes.set_title(f"Coeficiente de variação das redações \n {year} \n {model}")
    axes.set_xlabel("Coeficiente em %")
    axes.yaxis.set_major_locator(MaxNLocator(integer=True))
    #plt.show()

def plot_co_var_human(df, year):
    df_treated = df[["nota_final"]]
    df_std = df_treated.std()
    df_mean = df_treated.mean()

    df_result = (df_std/df_mean)*100
    result = float(df_result.iloc[0])
    print(f"{year} - {result:.4f}")