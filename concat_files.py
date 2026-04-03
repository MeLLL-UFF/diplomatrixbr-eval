import os
import json
import re

#
# Esse código é apenas uma muleta pra caso percamos iterações em uma execução dos códigos de juiz
# O intuito aqui é juntar todos os arquivos remanescentes de /essay_dump
#

def concat_files():
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

# Concatena iterações de diferentes arquivos em um arquivo final
def concat_iter_aux(file_path, **kwargs):
    if "prompts" in kwargs:
        prompts = kwargs["prompts"]
    else:
        prompts = None
    if "temps" in kwargs:
        temps = kwargs["temps"]
    else:
        temps = None
    
    concatenador = []
    path_to_iter = os.path.join(os.getcwd(), file_path)
    print(path_to_iter)
    with open(path_to_iter, "r", encoding="utf-8") as file:
        file_iter = json.load(file)
        for iter in file_iter:
            temp_ok = temps is None or temps == float(iter["temp"])
            prompt_ok = prompts is None or iter["prompt"] in prompts
            if temp_ok and prompt_ok:
                concatenador.append(iter)

    return concatenador

def concat_iter():
    #Matriz de requisições: Quais iterações serão concatenadas (arquivo, prompts, temperatura (opcional))
    matriz_reqs = [
        {"path": "prompt_testing\output_sabia-3.1_2022_p7-12_3r.json", "prompts" :[7, 8, 9]},
        {"path": "prompt_testing\\0.0_0.2_0.5_0.9_output_sabia-3.1_2022_p10-12_3r.json"}
    ]
    if "path" in matriz_reqs[0]:
        path = matriz_reqs[0]["path"]
    else:
        path = None

    if "prompts" in matriz_reqs[0]:
        prompts = matriz_reqs[0]["prompts"]
    else:
        prompts = None

    if "temps" in matriz_reqs[0]:
        temps = matriz_reqs[0]["temps"]
    else:
        temps = None

    json_concat = concat_iter_aux(path, prompts=prompts, temps=temps)
    i = 1
    while i < len(matriz_reqs):
        if "path" in matriz_reqs[i]:
            path = matriz_reqs[i]["path"]
        else:
            path = None

        if "prompts" in matriz_reqs[i]:
            prompts = matriz_reqs[i]["prompts"]
        else:
            prompts = None

        if "temps" in matriz_reqs[i]:
            temps = matriz_reqs[i]["temps"]
        else:
            temps = None

        templist = concat_iter_aux(path, prompts=prompts, temps=temps)

        for j in templist:
            json_concat.append(j)
        
        i += 1

    json_ordenado = sorted(json_concat, key=lambda item: item["essay"])

    with open("prompt_testing\\FIX_0.0_0.2_0.5_0.9_output_sabia-3.1_2022_p7-12_3r.json", "w", encoding="utf-8") as file:
        json.dump(json_ordenado, file, ensure_ascii=False)
        

concat_iter()