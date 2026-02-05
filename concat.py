import os
import json
import re

#
# Esse código é apenas uma muleta pra caso percamos iterações em uma execução dos códigos de juiz
# O intuito aqui é juntar todos os arquivos remanescentes de /essay_dump
#

cur_dir = os.getcwd()

path_essays = os.path.join(cur_dir, "prompt_testing", "essay_dump")

concatenador = []

ano = "2020-2021"
modelo = "sabia-3.1"

for essay in os.listdir(path_essays):
    if re.search(r"2023", essay):
        continue
    if re.search(rf"{modelo}", essay) and re.search(rf"{ano}", essay):
        with open(os.path.join(path_essays, essay), "r", encoding="utf-8") as file:
            teste_json = json.load(file)
            for iter in teste_json:
                #Ajustar para pegar prompts específicos
                if iter["prompt"] < 10:
                    concatenador.append(iter)

output_file_name = f"output_{modelo}_{ano}_p7-9_3r.json"

with open(os.path.join(cur_dir, "prompt_testing", output_file_name), "w", encoding="utf-8") as f:
    json.dump(concatenador, f, ensure_ascii=False)