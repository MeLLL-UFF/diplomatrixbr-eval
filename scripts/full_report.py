import os
import pandas as pd
from sklearn.metrics import cohen_kappa_score
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
from sklearn.preprocessing import MinMaxScaler

from .utils import get_mean

def print_full(df):
    pd.set_option('display.max_rows', len(df))
    pd.set_option('display.max_columns', len(df.columns))
    pd.set_option('display.expand_frame_repr', False)
    print(df)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.expand_frame_repr')

def quadratic_weighted_kappa(df):
    prompts = df["prompt"].unique()
    years = sorted(df["ano"].unique())

    cohen_df = pd.DataFrame(index=prompts)

    for year in years:
        cohen_ano = []
        for prompt in prompts:
            df_format = df[(df["ano"] == year) & (df["prompt"] == prompt)]
            notas_modelos = df_format["nota_final_model"].astype(int).to_list()
            notas_humanos = df_format["nota_final_human"].astype(int).to_list()
            
            notas_modelos = list(map(round, notas_modelos))
            notas_humanos = list(map(round, notas_humanos))

            cohen_ano.append(cohen_kappa_score(notas_humanos, notas_modelos, weights='quadratic'))
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

def full_report(num_runs, model_name):
    path_model_sheets = os.path.join(os.getcwd(), "prompt_testing", "sheets", model_name)

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

    model_df = pd.concat(sheet_list, ignore_index=True)

    path_human_sheets = os.path.join(os.getcwd(), "prompt_testing", "sheets", "notas_humanas")

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

    human_df = pd.concat(sheet_list, ignore_index=True)

    df = model_df.merge(human_df, on=["ano", "redacao"], how='inner', suffixes=("_model", "_human"))

    df.insert(len(df.columns), "val_squared_error", (df["nota_final_human"] - df["nota_final_model"])**2)

    cohen_kappa_df = quadratic_weighted_kappa(df)

    output_path = os.path.join(os.getcwd(), "prompt_testing", "reports", model_name)
    plot_RMSE(df, model_name, output_path)
    plot_qwk(cohen_kappa_df, model_name, output_path)
    plot_corr(df, model_name, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_runs", type=int, required=True)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()
    
    full_report(args.num_runs, args.model)