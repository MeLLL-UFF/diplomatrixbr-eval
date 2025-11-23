import os
from openai import OpenAI
from pydantic import BaseModel
import csv
import json
import yaml

SABIA_API_KEY="api-key"
client = OpenAI(
    api_key=SABIA_API_KEY,
    base_url="https://chat.maritaca.ai/api",
)
temp = [0.0, 0.5, 0.9]

class respostaPorCriterio(BaseModel):
  nota_1A: float
  nota_1B: float
  nota_1C: float
  numero_de_erros_gramaticais: int
  erros_gramaticais: list[str]
  feedbacks: list[str]

class respostaFinal(BaseModel):
  nota_final: float
  numero_de_erros_gramaticais: int
  erros_gramaticais: list[str]
  feedbacks: list[str]  

class respostaEmFaixa(BaseModel):
  faixa: str
  numero_de_erros_gramaticais: int
  erros_gramaticais: list[str]
  feedbacks: list[str] 

jsonGerado = []
root_path = os.getcwd()

path_prompts = os.path.join(root_path, "prompt_testing", "prompts.yaml")
path_essays = os.path.join(root_path, "prompt_testing", "sheets", "redacoes2022.csv")

with open(path_prompts, 'r', encoding='utf-8') as file:
    prompts_yaml = yaml.safe_load(file)
    prompts = prompts_yaml['prompts']

with open(path_essays, encoding='utf-8') as arquivo_referencia:

  tabela = csv.reader(arquivo_referencia, delimiter='|')
  numero_redacao = 0

  for linha in tabela:
    numero_redacao += 1
    redacao = linha[0]

    for prompt in prompts:

      # Definir aqui intervalo de prompts a serem testados
      if prompt['id'] >= 7 and prompt['id'] <= 12:
        prompt_formatado = prompt['prompt'] + redacao
        prompt_formatado += "\n\n" + prompt['extras'] if 'extras' in prompt else ''

        print(f"Redação {numero_redacao} - Prompt {prompt['id']}")

        formato_resposta = None

        match prompt['id']:
            # ADICIONAR NOVOS CASOS NO SWITCH CASE CONFORME FOR INTERESSANTE

          case 7 | 10:
            formato_resposta = respostaPorCriterio
          case 8 | 11:
            formato_resposta = respostaFinal
          case 9 | 12:
            formato_resposta = respostaEmFaixa

        if formato_resposta is None:
          raise ValueError("Atribua um valor a \"formato_resposta\"")

        for i in (temp):
          for j in range(3):
            response = client.beta.chat.completions.parse(
                model="sabia-3.1",
                temperature=i,
                messages=[
                    #{"role": "system", "content": "Você é um corretor de redações que deverá avaliar uma redação que concorre ao cargo de diplomata brasileiro. Retorne sua resposta seguindo a estrutura passada."},
                    {"role": "user", "content": prompt_formatado},
                ],
                response_format=formato_resposta,
                max_tokens=2048
            )

            response = json.loads(response.choices[0].message.content)
            response['modelo'] = 'sabia-3.1'
            response['prompt'] = prompt['id']
            response['temp'] = i
            response['versao'] = j + 1
            response['essay'] = numero_redacao
            jsonGerado.append(response)

          print(f"Temperatura testada: {i}")

  output_path = os.path.join(os.getcwd(), "prompt_testing", f'output_{response["modelo"]}_LLM_prompt.json')
  with open(output_path, 'w', encoding="utf-8") as file:
    json.dump(jsonGerado, file, indent=2, ensure_ascii=False)
    file.close()