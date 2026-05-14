import json
import csv
import os
import requests

url = "https://raw.githubusercontent.com/MeLLL-UFF/diplomatrixbr-gen/main/Diplomatrix.json"
requisicao = requests.get(url)

if requisicao.status_code == 200:
  diplomatrix = requisicao.json()
else:
  raise ValueError("Não foi possível acessar o repositório")

year = "2024"

candidatos = diplomatrix["Candidates_Essays"][year]["Candidates"]

filename_path = os.path.join("prompt_testing", "sheets", "notas_humanas")
os.makedirs(filename_path, exist_ok=True)

filename = os.path.join(filename_path, f"notas_humanas_{year}.csv")
with open(filename, 'w', newline='', encoding="utf-8") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["judge", "redacao", "nota_final", "1A", "1B", "1C", "CGPL", "num_errors"])
    writer.writeheader()
    redacao = 1
    for cand in candidatos:
        dict_cand = {}
        dict_cand["judge"] = "humano"
        dict_cand["redacao"] = redacao
        dict_cand["nota_final"] = cand["Score"]
        dict_cand["1A"] = "-"
        dict_cand["1B"] = "-"
        dict_cand["1C"] = "-"
        dict_cand["CGPL"] = "-"
        dict_cand["num_errors"] = "-"
        writer.writerow(dict_cand)
        redacao += 1
    