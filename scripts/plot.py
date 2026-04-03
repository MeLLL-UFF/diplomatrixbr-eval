import matplotlib.pyplot as plt
import textwrap
import math
import seaborn as sns

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

def plot_val_error(df, output_path):
    fig, ax = plt.subplots(figsize=(10, 6))

    df = df.copy()
    df["prompt"] = df["prompt"].astype(str)
    df["prompt"] = df["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão", "10":"10 - Critério COM padrão", "11":"11 - Total COM padrão", "12":"12 - Faixa COM padrão"})

    sns.lineplot(
        data=df,
        x="redacao",
        y="val_error",
        hue="prompt",
        style="temp",
        marker="o",
        palette=["#54B8D9", "#FF8400FF", "#7ED07E", "#3131BD", "#D41111", "#2E772E"],
        ax=ax
    )

    ax.set_title("Análise de Erro de Validação")
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

def plot_eval_human_scores(df, output_path):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    df = df.copy()
    df = df.sort_values(by=["prompt", "nota_humana"], ascending=[True, False])
    df["redacao"] = df["redacao"].astype(str)
    df["prompt"] = df["prompt"].astype(str)
    df["prompt"] = df["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão", "10":"10 - Critério COM padrão", "11":"11 - Total COM padrão", "12":"12 - Faixa COM padrão"})

    sns.lineplot(
        data=df,
        x="redacao",
        y="nota_final",
        hue="prompt",
        style="temp",
        marker="o",
        palette=["#54B8D9", "#FF8400FF", "#7ED07E", "#3131BD", "#D41111", "#2E772E"],
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

    plt.suptitle("Comparação de Nota Gerada e Nota Humana por Redação", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1.1, 0.95])
    plt.savefig(f"{output_path}/comparacao_notas.png", dpi=300, bbox_inches='tight')
    plt.close()

def plot_eval_human_num_errors(df_merged, df_human, output_path):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    df_human = df_human.copy()
    df_human = df_human.sort_values(by=["num_errors", "redacao"], ascending=[False, True])
    df_human["redacao"] = df_human["redacao"].astype(str)

    df_merged = df_merged.copy()
    df_merged = df_merged.sort_values(by=["erros_humano", "redacao"], ascending=[False, True])
    df_merged["redacao"] = df_merged["redacao"].astype(str)

    df_merged["prompt"] = df_merged["prompt"].astype(str)
    df_merged["prompt"] = df_merged["prompt"].replace({"7": "7 - Critério SEM padrão", "8":"8 - Total SEM padrão", "9":"9 - Faixa SEM padrão", "10":"10 - Critério COM padrão", "11":"11 - Total COM padrão", "12":"12 - Faixa COM padrão"})


    sns.lineplot(
        data=df_merged,
        x="redacao",
        y="num_errors",
        hue="prompt",
        style="temp",
        marker="o",
        palette=["#54B8D9", "#FF8400FF", "#7ED07E", "#3131BD", "#D41111", "#2E772E"],
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

    plt.suptitle("Comparação de Número de Erros Gerados e Humanos por Redação", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1.1, 0.95])
    plt.savefig(f"{output_path}/comparacao_num_erros.png", dpi=300, bbox_inches='tight')
    plt.close()
