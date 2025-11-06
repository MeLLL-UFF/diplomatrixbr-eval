import json
import csv
import os
import time

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

path_json_response = os.path.join(os.getcwd(), "prompt_testing", "output_sabia-3.1_p7-12.json")
path_notas_2022 = os.path.join(os.getcwd(), "prompt_testing", "sheets", "notas_humanas_2022.csv")
with open(path_json_response, 'r') as json_file:
    data = json.load(json_file)

data_atual = time.strftime("%d.%m.%Y-%H.%M.%S")
with open(path_notas_2022, 'r') as input_file, open(f'output_{data_atual}.csv', 'w', newline='') as output_file:
    notas_humanas = csv.reader(input_file)
    writer = csv.DictWriter(output_file, fieldnames=["judge", "versao", "prompt", "temp", "redacao", "nota_final", "1A", "1B", "1C", "CGPL", "num_errors", "faixa"])
    writer.writeheader()

    # for row in notas_humanas:
        # Incluir notas de humanos aqui

    for item in data:
        new_row = create_new_row(item)
        writer.writerow(new_row)

    output_file.close()