import json
import math

with open("prompt_testing/outputs/Qwen3.6-35B-A3B/0.0_output_Qwen3.6-35B-A3B_2023_p7-9_3r.json", "r", encoding="utf-8") as f:
    dicionario = json.load(f)

qtd_prompt = 3
qtd_iter = 3

qtd_redacao = math.ceil(len(dicionario)/(qtd_iter*qtd_prompt))

iter_prompt = 0
for red in range(1, qtd_redacao+1):
    for prompt in range(7, 10):
        for iter_iter in range(0, qtd_iter):
            iterador = (red-1)*(qtd_iter*qtd_prompt) + (prompt%7)*3 + iter_iter%3
            if dicionario[iterador]["versao"] != iter_iter+1:
                print(f"{red} - {prompt} - {iter_iter+1}")
                iter_iter += 1
            elif dicionario[iterador]["prompt"] != prompt:
                print(f"{red} - {prompt} - {iter_iter+1}")
            elif dicionario[iterador]["essay"] != red:
                print(f"{red} - {prompt} - {iter_iter+1}")

            #print(f"{red} - {prompt} - {iter_iter+1}")
                