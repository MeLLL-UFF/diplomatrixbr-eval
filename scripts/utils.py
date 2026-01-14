import pandas as pd

mapping_faixas = {
    "Excepcional": 60,
    "Excelente": 55,
    "Ótimo": 50,
    "Boa": 45,
    "Regular": 40,
    "Fraco": 30,
}

def create_new_row(data: dict) -> dict:
    nota_final = data.get("nota_final", None)
    if nota_final is None:
        nota_final = "-" if data.get("faixa", None) is not None else data["nota_1A"] + data["nota_1B"] + data["nota_1C"] + data["nota_1C"] - data["numero_de_erros_gramaticais"]*0.3
        data["nota_final"] = nota_final   

    new_row = {}
    new_row["judge"] = data["modelo"]
    new_row["versao"] = data["versao"]
    new_row["prompt"] = data["prompt"]
    new_row["temp"] = data["temp"]
    new_row["redacao"] = data["essay"]
    new_row["nota_final"] = nota_final
    new_row["1A"] = data.get("nota_1A", "-")
    new_row["1B"] = data.get("nota_1B", "-")
    new_row["1C"] = data.get("nota_1C", "-")
    new_row["CGPL"] = (data["nota_1C"] - data["numero_de_erros_gramaticais"]*0.3) if data.get("nota_1C", None) is not None else "-"
    new_row["num_errors"] = data["numero_de_erros_gramaticais"]
    new_row["faixa"] = data.get("faixa", "-")
    return new_row

def get_mean(filepath: str, num_runs: int) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    cols_to_agg = ["nota_final", "1A", "1B", "1C", "CGPL", "num_errors", "faixa_numerica"]

    df["faixa_numerica"] = df["faixa"].replace(mapping_faixas)
    df[cols_to_agg] = df[cols_to_agg].apply(pd.to_numeric, errors='coerce')
    df["group"] = df.index // num_runs

    agg_dict = {col: "first" for col in df.columns if col not in cols_to_agg}
    for col in cols_to_agg:
        agg_dict[col] = "mean"

    df = df.groupby("group").agg(agg_dict).reset_index(drop=True).drop(columns=["group", "versao"]).round(4)
    df["nota_final"] = df["nota_final"].fillna(df["faixa_numerica"])
    df.drop(columns=["faixa_numerica"], inplace=True)
    df.drop(columns=["faixa"], inplace=True)

    return df
    