import json
import csv
import os
import time

from utils import create_new_row

path_json_response = os.path.join(os.getcwd(), "prompt_testing", "output_sabia-3.1_p7-12_10r.json")
data_atual = time.strftime("%d.%m.%Y-%H.%M.%S")

with open(path_json_response, 'r') as json_file:
    data = json.load(json_file)

# path_notas = os.path.join(os.getcwd(), "prompt_testing", "sheets", "notas_humanas_2022.csv")
# with open(path_notas, 'r') as input_file:
# notas_humanas = csv.reader(input_file)

filename = f'output_{data_atual}.csv'
with open(filename, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["judge", "versao", "prompt", "temp", "redacao", "nota_final", "1A", "1B", "1C", "CGPL", "num_errors", "faixa"])
    writer.writeheader()

    for item in data:
        new_row = create_new_row(item)
        writer.writerow(new_row)

    output_file.close()