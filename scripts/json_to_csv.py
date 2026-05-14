import json
import csv
import os
import argparse

from utils import create_new_row

def convert(year, model):
    path_json_response = os.path.join(os.getcwd(), "prompt_testing", "outputs", model, f"0.0_output_{model}_{year}_p7-9_3r.json")

    with open(path_json_response, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)

    filename_path = os.path.join("prompt_testing", "sheets", model)
    os.makedirs(filename_path, exist_ok=True)
    filename = os.path.join(filename_path, f"{model}_{year}_p7-9_3r.csv")
    with open(filename, 'w', newline='', encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["judge", "versao", "prompt", "temp", "redacao", "nota_final", "1A", "1B", "1C", "CGPL", "num_errors", "faixa"])
        writer.writeheader()

        for item in data:
            new_row = create_new_row(item)
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