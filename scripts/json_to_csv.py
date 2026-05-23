import json
import csv
import os
import argparse
import requests

from utils import create_new_row

def convert(year, model):
    path_json_response = os.path.join(os.getcwd(), "prompt_testing", "outputs", model, f"output_{model}_{year}_p7-9_3r.json")

    with open(path_json_response, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)

    filename_path = os.path.join("prompt_testing", "sheets", model)
    os.makedirs(filename_path, exist_ok=True)
    filename = os.path.join(filename_path, f"{model}_{year}_p7-9_3r.csv")
    with open(filename, 'w', newline='', encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["judge", "versao", "prompt", "temp", "redacao", "nota_final", "1A", "1B", "1C", "CGPL", "num_errors", "faixa"])
        writer.writeheader()
        
        url = "https://raw.githubusercontent.com/MeLLL-UFF/diplomatrixbr-gen/main/Diplomatrix.json"
        requisicao = requests.get(url)

        if requisicao.status_code == 200:
            diplomatrix = requisicao.json()
        else:
            raise ValueError("Não foi possível acessar o repositório")
        
        max_score_2 = diplomatrix["Candidates_Essays"][year]["Criteria"]["2"]
        error_penalty = diplomatrix["Candidates_Essays"][year]["Criteria"]["error_penalty"]

        for item in data:
            new_row = create_new_row(item, year, max_score_2, error_penalty)
            writer.writerow(new_row)

        output_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to CSV")
    parser.add_argument("--model", help="Model name")
    parser.add_argument("--year", type=str, help="Year")
    args = parser.parse_args()

    if args.model and args.year:
        year = args.year
        model = args.model
        convert(year, model)