from full_report import get_full_model_df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse
import os

from .utils import print_full

def main(model_list, num_runs):
    models_dfs = []
    for model in model_list:
        path_model_sheets = os.path.join(os.getcwd(), "prompt_testing", "sheets", model)
        
        treated_df = get_full_model_df(path_model_sheets, num_runs)
        treated_df["modelo"] = model

        models_dfs.append(get_full_model_df(path_model_sheets, num_runs))

    complete_df = pd.concat(models_dfs, ignore_index=True)

    print_full(complete_df)
