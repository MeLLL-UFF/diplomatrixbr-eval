import json
import csv
import os
import time

from utils import create_new_row

year = 2022
model = "sabia-4"
path_json_response = os.path.join(os.getcwd(), "prompt_testing", f"output_{model}_{year}_p7-9_3r.json")
data_atual = time.strftime("%d.%m.%Y-%H.%M.%S")

with open(path_json_response, 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)

filename = f'prompt_testing/sheets/{model}_{year}_p7-9_3r.csv'
with open(filename, 'w', newline='', encoding="utf-8") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["judge", "versao", "prompt", "temp", "redacao", "nota_final", "1A", "1B", "1C", "CGPL", "num_errors", "faixa"])
    writer.writeheader()

    for item in data:
        new_row = create_new_row(item)
        writer.writerow(new_row)

    output_file.close()