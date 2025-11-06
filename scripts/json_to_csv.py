import json
import csv
import os
import time

def create_new_row(data):
    new_row = {}
    new_row["judge"] = data["modelo"]
    new_row["versao"] = data["versao"]
    new_row["prompt"] = data["prompt"]
    new_row["temp"] = data["temp"]
    new_row["1A"] = data["nota_1A"]
    new_row["1B"] = data["nota_1B"]
    new_row["1C"] = data["nota_1C"]
    new_row["CGPL"] = data["nota_1C"] - (data["numero_de_erros_gramaticais"])*0.3
    new_row["nota_final"] = data["nota_1A"] + data["nota_1B"] + data["nota_1C"] + new_row["CGPL"]
    new_row["redacao"] = data["essay"]
    new_row["num_errors"] = data["numero_de_erros_gramaticais"]
    return new_row

path_output = os.path.join(os.getcwd(), "prompt_testing", "output_sabia-3.1_p1-5_criterios.json")
with open(path_output, 'r') as json_file:
    data = json.load(json_file)

data_atual = time.strftime("%d.%m.%Y-%H.%M.%S")
with open(f'output_{data_atual}.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["judge", "versao", "prompt", "temp", "redacao", "nota_final", "1A", "1B", "1C", "CGPL", "num_errors"])
    writer.writeheader()

    # Incluir notas de humanos aqui

    for item in data:
        new_row = create_new_row(item)
        writer.writerow(new_row)

    csv_file.close()