import os
import pandas as pd

from utils import get_mean

def print_full(df):
    pd.set_option('display.max_rows', len(df))
    pd.set_option('display.max_columns', len(df.columns))
    pd.set_option('display.expand_frame_repr', False)
    print(df)
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.expand_frame_repr')

def full_report(model_name, num_runs):
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
    

full_report("gemma-4-31B-it", 3)